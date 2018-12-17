#-*-coding:utf-8 -*-

from __future__ import print_function

import numpy as np 
import torch
import torch as nn
import torch.nn.functional as F

import math,copy,time

from torch.autograd import Variable

import matplotlib.pyplot as plt
import seaborn

seaborn.set_context(context="talk")