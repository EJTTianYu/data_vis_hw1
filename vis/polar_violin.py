# coding=utf-8
'''
@author=Wangminhao Gou
参考代码
'''
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def violin_polar_plot(path1, path2):
    pil_violin = Image.open(path1)
    pil_picture = Image.open(path2)
    # pil_violin.show()
    pil_picture.thumbnail((200, 200))
    # pil_picture.show()
    box = (210, 110, 410, 310)
    pil_violin.paste(pil_picture, box)
    # pil_violin.show()
    plt.imshow(pil_violin)
    plt.plot([310, 620], [210, 210], color='k')
    plt.annotate(r'>', xy=(620, 210), xycoords='data', xytext=(-5, -4),
                 textcoords='offset points', fontsize=16)
    plt.annotate(r'Lightness', xy=(620, 210), xycoords='data', xytext=(-70, +2),
                 textcoords='offset points', fontsize=16)
    t = np.linspace(np.pi, -np.pi * 1 / 2)
    x = 310 + 230 * np.cos(t)
    y = 210 + 230 * np.sin(t)
    plt.plot(x, y, color='k')
    plt.annotate(r'^', xy=(80, 210), xycoords='data', xytext=(-6, -4),
                 textcoords='offset points', fontsize=16)
    plt.annotate(r'Hue', xy=(80, 210), xycoords='data', xytext=(-15, +10),
                 textcoords='offset points', fontsize=16)
    plt.show()


if __name__ == '__main__':
    violin_polar_plot('/Users/tianyu/PycharmProjects/visHW1/src/res/result3.jpeg',
                      '/Users/tianyu/PycharmProjects/visHW1/src/res/profile.jpeg')
