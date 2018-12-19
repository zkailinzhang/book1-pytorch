#-*- coding:utf-8 -*-

from __future__ import print_function

import torch 
import torch.nn as nn
import torch.nn.functional as 

import os 
dirname,filename = os.path.split(os.path.abspath(__file__))
os.chdir(dirname)


class ResidualBlock(nn.Module):
    def __init__(self,inchannel,outchannel,stride=1,shortcut=None):
        super(ResidualBlock,self).__init__()

        self.left = nn.Sequential(
            nn.Conv2d(in_channels,out_channels,3,stride,1,bias=False)
            


        )
