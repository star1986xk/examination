# coding:utf-8
# import tensorflow as tf
import cv2
from PIL import Image
import numpy as np
import os

train_txt = './data/train.txt'
x_train_savepath = './data/x_train.npy'
y_train_savepath = './data/y_train.npy'

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


def split_img(img_path):
    # 载入图片
    img_np = cv2.imread(img_path, cv2.IMREAD_COLOR)
    # 灰度化
    image = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    # 二值化
    retval, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    # 保存切割后的每个图的4点坐标
    # 水平投影
    H = getHProjection(img)

    start = 0
    H_Start = 0
    H_End = 0
    # 根据水平投影获取垂直分割位置
    for i in range(len(H)):
        if H[i] > 0 and start == 0:
            H_Start = i
            start = 1
        if H[i] <= 0 and start == 1:
            H_End = i
            start = 0
            break

    # 对行图像进行垂直投影
    W = getVProjection(img)
    Wstart = 0
    W_Start = 0
    W_End = 0
    for j in range(len(W)):
        if W[j] > 0 and Wstart == 0:
            W_Start = j
            Wstart = 1
        if W[j] <= 0 and Wstart == 1:
            W_End = j
            Wstart = 0
            image = image[H_Start: H_End, W_Start:W_End]
            break
    image = cv2.resize(image, (28, 28))
    name = img_path.split('/')[-1]
    cv2.imwrite('aaa/'+name, image)
    return image


# 自定义图片读取函数
def generateds(txt):
    f = open(txt, 'r')
    contents = f.readlines()
    f.close()
    x, y_ = [], []
    for content in contents:
        try:
            # 以空格分开，图片路径为value[0] , 标签为value[1] , 存入列表
            value = content.split()
            # 拼出图片路径和文件名
            img_path = value[0]
            # 读入图片
            img = split_img(img_path)

            # 数据归一化 （实现预处理）
            img = img / 255.
            # 归一化后的数据，贴到列表x
            x.append(img)
            # 标签贴到列表y_
            y_.append(value[1])
            # 打印状态提示
            print('loading : ' + content)
        except:
            continue

    # 变为np.array格式
    x = np.array(x)  # (None,28,28)
    y_ = np.array(y_).astype(np.int64)
    return x, y_


print('-------------生成数据-----------------')
x_train, y_train = generateds(train_txt)
print(x_train.shape)

print('-------------保存数据-----------------')
# (None,28,28) ==>  (None,784)
x_train_save = np.reshape(x_train, (len(x_train), -1))
np.save(x_train_savepath, x_train_save)
np.save(y_train_savepath, y_train)
