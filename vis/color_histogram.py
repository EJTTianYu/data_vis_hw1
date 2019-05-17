# coding=utf-8
'''
@author=Wangminhao Gou
参考代码：https://blog.csdn.net/zxfhahaha/article/details/80116157
参考代码：https://blog.csdn.net/sunny2038/article/details/9097989
'''

import cv2
from matplotlib import pyplot as plt


# 绘制传入图片的HSL空间颜色直方图
def draw_hsl(path):
    img = cv2.imread(path)
    img_bgr_data = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)
    plt.figure(figsize=(15, 5))  # 设置画布的大小
    # H通道 直方图
    ax1 = plt.subplot(131)
    ax1.hist(img_bgr_data[:, :, 0].ravel(), bins=50, color='black', alpha=0.5)
    plt.xlabel("Hue")
    # S通道 直方图
    ax2 = plt.subplot(132)
    ax2.hist(img_bgr_data[:, :, 1].ravel(), bins=50, color='black', alpha=0.5)
    plt.xlabel("Saturation")
    # L通道 直方图
    ax3 = plt.subplot(133)
    ax3.hist(img_bgr_data[:, :, 2].ravel(), bins=50, color='black', alpha=0.5)
    plt.xlabel("Lightness")
    plt.show()


if __name__ == '__main__':
    draw_hsl(r'/Users/tianyu/PycharmProjects/visHW1/src/res/profile.jpeg')
