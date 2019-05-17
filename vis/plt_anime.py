# coding=utf-8
'''
@author=Wangminhao Gou
参考代码
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import animation

fig, ax = plt.subplots()

img = cv2.imread(r'/Users/tianyu/PycharmProjects/visHW1/src/res/profile.jpeg')
img_bgr_data = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)
h, l, s = cv2.split(img_bgr_data)
# 处理各个通道
h_process = (h / 8).astype('int32').ravel()
l_process = l.ravel()
s_process = s.ravel()
line = sns.violinplot(x=h_process, y=s_process, inner='point', palette=sns.hls_palette(32, l=.5, s=.9), linewidth=0,
                      saturation=0.5, width=0.1)
x_ax = np.arange(0, 33, 2)
for i in x_ax:
    plt.axvspan(i - 0.5, i + 0.5, facecolor='#666666', alpha=0.1)


def animate(i):
    line = sns.violinplot(x=h_process, y=s_process, inner='point', palette=sns.hls_palette(32, l=.5, s=.9), linewidth=0,
                          saturation=0.5, width=i * 0.3)
    return line,


def init():
    return line,


ani = animation.FuncAnimation(fig=fig, func=animate, frames=10,
                              init_func=init, interval=100, blit=False)
ani.save(r"/Users/tianyu/PycharmProjects/visHW1/src/res/animate_violin.gif", writer='pillow')
plt.show()
