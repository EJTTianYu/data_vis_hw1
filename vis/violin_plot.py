# coding=utf-8
'''
@author=Wangminhao Gou
参考代码
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# 分离通道
def split_hsl(path):
    img = cv2.imread(path)
    img_bgr_data = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)
    h, l, s = cv2.split(img_bgr_data)
    return h, l, s


# 小提琴图绘制示例
def violin_plot(h, s, l):
    # 绘制H和S通道的小提琴图
    plt.subplot(211)
    ax = sns.violinplot(x=h, y=s, inner='point', palette=sns.hls_palette(32, l=.5, s=.9), linewidth=0,
                        saturation=0.5, width=1.6)
    x_ax = np.arange(0, 33, 2)
    for i in x_ax:
        plt.axvspan(i - 0.5, i + 0.5, facecolor='#666666', alpha=0.1)
    plt.xticks([])
    plt.yticks([])
    plt.xlim(-1, 32)
    plt.ylim((-30, 250))
    ax1 = plt.gca()
    ax1.spines['right'].set_color('none')
    ax1.spines['left'].set_color('none')
    plt.xlabel('Hue')
    plt.ylabel('Saturation')
    # 绘制H和L通道的小提琴图
    plt.subplot(212)
    ax1 = sns.violinplot(x=h, y=l, inner='point', palette=sns.hls_palette(32, l=.5, s=.9), linewidth=0,
                         saturation=0.5, width=1.6)
    x_ax = np.arange(0, 33, 2)
    for i in x_ax:
        plt.axvspan(i - 0.5, i + 0.5, facecolor='#666666', alpha=0.1)
    plt.xticks([])
    plt.yticks([])
    plt.xlim(-1, 32)
    plt.ylim((-30, 300))
    plt.xlabel('Hue')
    plt.ylabel('Lightness')
    plt.savefig(r'/Users/tianyu/PycharmProjects/visHW1/src/res/result2.jpeg')
    plt.show()


if __name__ == '__main__':
    h, l, s = split_hsl(r'/Users/tianyu/PycharmProjects/visHW1/src/res/profile.jpeg')
    # 处理各个通道
    h_process = (h / 8).astype('int32').ravel()
    l_process = l.ravel()
    s_process = s.ravel()
    violin_plot(h_process, s_process, l_process)
