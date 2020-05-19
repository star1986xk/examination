# coding:utf-8
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation
from tensorflow.keras import Model
from PIL import Image
import os
from matplotlib import pyplot as plt

# train_txt = './data/train.txt'
# x_train_savepath = './data/x_train.npy'
# y_train_savepath = './data/y_train.npy'
#
# print('-------------load data----------------')
# x_train_save = np.load(x_train_savepath)
# y_train = np.load(y_train_savepath)
# # (None,784) ==>  (None,28,28)
# x_train = np.reshape(x_train_save, (len(x_train_save), 28, 28))
# train_imgs = np.zeros(shape=(x_train.shape[0],x_train.shape[1],x_train.shape[2],3),dtype=np.float32)
# # 转换成三通道数据
# train_imgs[:,:,:,0] = x_train[:,:]
# train_imgs[:,:,:,1] = x_train[:,:]
# train_imgs[:,:,:,2] = x_train[:,:]
# print(train_imgs.shape)  # (3410,28,28,1)

item = {
    '0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'A',
    '11':'B','12':'C','13':'D','14':'E','15':'F','16':'G','17':'H','18':'I','19':'J','20':'K','21':'L','22':'M',
    '23':'N','24':'O','25':'P','26':'Q','27':'R','28':'S','29':'T','30':'U','31':'V','32':'W','33':'X','34':'Y',
    '35':'Z'
}




# resnet网络框架
class ResnetBlock(Model):
    def __init__(self, filters, strides=1, residual_path=False):
        super(ResnetBlock, self).__init__()
        self.filters = filters
        self.strides = strides
        self.residual_path = residual_path

        self.c1 = Conv2D(filters, (3, 3), strides=strides, padding='same', use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')

        self.c2 = Conv2D(filters, (3, 3), strides=1, padding='same', use_bias=False)
        self.b2 = BatchNormalization()

        # residual_path为True时，对输入进行下采样，即用1x1的卷积核做卷积操作，保证x能和F(x)维度相同，顺利相加
        if residual_path:
            self.down_c1 = Conv2D(filters, (1, 1), strides=strides, padding='same', use_bias=False)
            self.down_b1 = BatchNormalization()

        self.a2 = Activation('relu')

    def call(self, inputs):
        # residual等于输入值本身，即residual=x
        residual = inputs
        # 将输入通过卷积、BN层、激活层，计算F(x)
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)

        x = self.c2(x)
        y = self.b2(x)

        if self.residual_path:
            residual = self.down_c1(inputs)
            residual = self.down_b1(residual)

        out = self.a2(y + residual)  # 最后输出的是两部分的和，即F(x)+x或F(x)+Wx,再过激活函数
        return out
class ResNet18(Model):

    def __init__(self, block_list, initial_filters=64):  # block_list表示每个block有几个卷积层
        super(ResNet18, self).__init__()
        self.num_blocks = len(block_list)  # 共有几个block
        self.block_list = block_list
        self.out_filters = initial_filters
        self.c1 = Conv2D(self.out_filters, (3, 3), strides=1, padding='same', use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')
        self.blocks = tf.keras.models.Sequential()
        # 构建ResNet网络结构
        for block_id in range(len(block_list)):  # 第几个resnet block
            for layer_id in range(block_list[block_id]):  # 第几个卷积层

                # 对除第一个block以外的每个block的输入进行下采样
                if block_id != 0 and layer_id == 0:
                    block = ResnetBlock(self.out_filters, strides=2, residual_path=True)
                else:
                    block = ResnetBlock(self.out_filters, residual_path=False)
                self.blocks.add(block)  # 将构建好的block加入resnet

            # 下一个block的卷积核数是上一个block的2倍
            self.out_filters *= 2
        self.p1 = tf.keras.layers.GlobalAveragePooling2D()
        self.f1 = tf.keras.layers.Dense(36, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, inputs):
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)
        x = self.blocks(x)
        x = self.p1(x)
        y = self.f1(x)
        return y


# 自定义预测
def custom_predict(model,img):
    # img = Image.open(path)
    # img = img.resize((28, 28), Image.ANTIALIAS)  # 抗锯齿
    # img.show()
    # 图片变为8位宽灰度值的np.array格式
    # img = np.array(img.convert('L'))  # (28,28)

    # # 将 黑白底 转换
    # for i in range(28):
    #     for j in range(28):
    #         if img[i][j] < 200:
    #             img[i][j] = 255
    #         else:
    #             img[i][j] = 0

    img = img / 255.

    img = np.reshape(img, (1, 28, 28, 1))

    # text_image = np.zeros(shape=(1,img.shape[0],img.shape[1],3),dtype=np.float32)
    # text_image[:, :, :, 0] = img[:, :]
    # text_image[:, :, :, 1] = img[:, :]
    # text_image[:, :, :, 2] = img[:, :]

    print(img.shape)
    result = model.predict(img)
    pred = np.argmax(result, axis=1)
    pred = str(pred[0])
    res = item[pred]
    print('\n')
    print(pred + " " + res)
    return res

def test(imgList):
    model = ResNet18([2, 2, 2, 2])
    # checkpoint 保存当前的训练状态，下次启动时继续运行
    checkpoint_save_path = "./ocr_dir/model/mnist62.ckpt"
    if os.path.exists(checkpoint_save_path + '.index'):
        print('-------------load the model-----------------')
        model.load_weights(checkpoint_save_path)
        result =[]
        for img in imgList:
            char = custom_predict(model,img)
            result.append(char)
    return '\n'.join(result)




