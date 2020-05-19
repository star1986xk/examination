import base64
import cv2
import numpy as np
from ocr_dir.custom_pre import *


'''水平投影'''
def getHProjection(image):
    hProjection = np.zeros(image.shape, np.uint8)
    # 图像高与宽
    (h, w) = image.shape
    # 长度与图像高度一致的数组
    h_ = [0] * h
    # 循环统计每一行白色像素的个数
    for y in range(h):
        for x in range(w):
            if image[y, x] == 255:
                h_[y] += 1
    # 绘制水平投影图像
    for y in range(h):
        for x in range(h_[y]):
            hProjection[y, x] = 255
    return h_

def getVProjection(image):
    vProjection = np.zeros(image.shape, np.uint8);
    # 图像高与宽
    (h, w) = image.shape
    # 长度与图像宽度一致的数组
    w_ = [0] * w
    # 循环统计每一列白色像素的个数
    for x in range(w):
        for y in range(h):
            if image[y, x] == 255:
                w_[x] += 1
    # 绘制垂直平投影图像
    for x in range(w):
        for y in range(h - w_[x], h):
            vProjection[y, x] = 255
    return w_

def reverse_color(img):
    (x,y) = img.shape
    for i in range(x):
        for j in range(y):
            img[i, j] = 255 - img[i, j]
    return img

def b_img(img):
    (x,y) = img.shape
    for i in range(x):
        for j in range(y):
            if img[i, j]:
                img[i-1, j] = img[i, j]
                img[i, j-1] = img[i, j]
    return img

def split_img(imgData):
    #载入图片
    nparr = np.fromstring(base64.b64decode(imgData), np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #灰度化
    image = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #二值化
    retval, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    (h, w) = img.shape
    #保存切割后的每个图的4点坐标
    Position = []
    # 水平投影
    H = getHProjection(img)
    start = 0
    H_Start = []
    H_End = []
    # 根据水平投影获取垂直分割位置
    for i in range(len(H)):
        if H[i] > 0 and start == 0:
            H_Start.append(i)
            start = 1
        if H[i] <= 0 and start == 1:
            H_End.append(i)
            start = 0
    # 分割行，分割之后再进行列分割并保存分割位置
    for i in range(len(H_Start)):
        # 获取行图像
        cropImg = img[H_Start[i]:H_End[i], 0:w]
        # cv2.imshow('cropImg',cropImg)
        # 对行图像进行垂直投影
        W = getVProjection(cropImg)
        Wstart = 0
        Wend = 0
        W_Start = 0
        W_End = 0
        for j in range(len(W)):
            if W[j] > 0 and Wstart == 0:
                W_Start = j
                Wstart = 1
                Wend = 0
            if W[j] <= 0 and Wstart == 1:
                W_End = j
                Wstart = 0
                Wend = 1
            if Wend == 1:
                Position.append([W_Start, H_Start[i], W_End, H_End[i]])
                Wend = 0
    # 根据确定的位置分割字符
    imgList = []
    for m in range(len(Position)):
        cropImg = img[Position[m][1]-2:Position[m][3]+2, Position[m][0]-2:Position[m][2]+2]
        cropImg = cv2.resize(cropImg, (28,28))
        cropImg = b_img(cropImg)
        cropImg = reverse_color(cropImg)
        # cv2.imwrite(str(m)+'.png',cropImg)
        imgList.append(cropImg)
    return test(imgList)
