#-*-coding:utf-8 -*-

import tensorflow as tf 
import torch
import torchvision
import cv2
import keras

print("cv2 version {},\ntorch version {}{},\ntf{},\n keras{}".format(
    cv2.__version__,torch.__version__,torch.__version__,tf.__version__
    ,keras.__version__))