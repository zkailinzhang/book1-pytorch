#-*- coding:utf-8 -*-

from __future__ import print_function

import numpy as np 
import warnings

from keras import layers
import keras.layers as KL
import keras.engine as kE 
import keras.models as KM 
import keras.backend as K 

from keras.preprocessing import image

from keras.utils import layer_utils
from keras.utils.data_utils import get_file

from keras.applications import imagenet_utils

def identity_block(input_tensor,kernel_size,filters,stage,block):

    filter1,filter2,filter3 = filters
    if K.image_data_format() == 'channel_last':
        bn_axis = 3
    else:
        bn_axis =1
    
    conv_name_base = 'res' + str(stage)+block +'_branch'

    bn_name_base = 'bn' + str(stage) + block +'_branch'

    x = KL.Conv2D(filter1,(1,1),name=conv_name_base, '2a')(input_tensor)
    x = KL.BatchNormalization(axis= bn_axis, name=bn_name_base,+'2a')(x)

    








