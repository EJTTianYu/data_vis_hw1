# coding=utf-8
'''
@author=Wangminhao Gou
参考代码
'''
import csv

import cv2


# 分离通道
def split_hsl(path):
    img = cv2.imread(path)
    img_bgr_data = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)
    h, l, s = cv2.split(img_bgr_data)
    return h, l, s


if __name__ == '__main__':
    h, l, s = split_hsl(r'/Users/tianyu/PycharmProjects/visHW1/src/res/profile.jpeg')
    # 处理各个通道
    # 处理各个通道
    h_process = (h / 8).astype('int64').ravel()
    l_process = l.ravel()
    s_process = s.ravel()
    with open(r'/Users/tianyu/PycharmProjects/visHW1/src/res/channel.csv', 'w') as output:
        writer = csv.writer(output, dialect='excel')
        title = ['h_channel', 'l_channel', 's_channel']
        writer.writerow(title)
        for i in range(h_process.size):
            line = []
            line.append(str(h_process[i]))
            line.append(str(l_process[i]))
            line.append(str(s_process[i]))
            writer.writerow(line)
