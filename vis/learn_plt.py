# coding=utf-8
'''
@author=Wangminhao Gou
参考代码：https://stackoverflow.com/questions/51675940/converting-an-image-from-cartesian-to-polar-limb-darkening
'''
import cv2
import numpy as np
import pandas as pd
from ggplot import *
from matplotlib import pyplot as plt


def tranfer_polar():
    source = cv2.imread('/Users/tianyu/PycharmProjects/visHW1/src/res/result.jpeg', 1)

    # --- ensure image is of the type float ---
    img = source.astype(np.float32)

    # --- the following holds the square root of the sum of squares of the image dimensions ---
    # --- this is done so that the entire width/height of the original image is used to express the complete circular range of the resulting polar image ---
    value = np.sqrt(((img.shape[0] / 2.0) ** 2.0) + ((img.shape[1] / 2.0) ** 2.0))

    polar_image = cv2.linearPolar(img, (img.shape[0] / 2, img.shape[1] / 2), value, cv2.WARP_FILL_OUTLIERS)
    polar_image = polar_image.astype(np.uint8)

    plt.imshow(polar_image)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def learn_ggplot():
    df = pd.read_table('/Users/tianyu/PycharmProjects/visHW1/src/res/channel.csv', sep=',')
    p = ggplot(df, aes('h_channel', 'l_channel')) + geom_point() + ggtitle('mtcars') + coord_polar()
    print(p)


def test_ggplot():
    df = pd.read_table('/Users/tianyu/PycharmProjects/visHW1/src/res/channel.csv', sep=',')
    p = ggplot(df, aes('h_channel', 's_channel')) + geom_violin(alpha=1.0) + coord_polar()
    print(p)


if __name__ == "__main__":
    tranfer_polar()
