#!/usr/bin/env python2
from svmutil import *
from img_util import *
import math
import numpy as np
import sys

#y, x = svm_read_problem('ml2013final_train.dat')
#for i in range(0,len(x)):
#  x[i] = shift_and_flip(x[i],20)
#  x[i] = to_binary_image(x[i],0.7)
#  x[i] = dilation(x[i],kernel,k_size)
#  output(y[i],x[i])

y, x = svm_read_problem(sys.argv[1])
#y, x = svm_read_problem('train.small.dat')
for i in range(0,len(x)):
  img = to_img_array(x[i],122,105)
  img_bin = to_binary_image(img,0.1,122,105)
  img,h,w =  crop(img_bin)
  output_bmp(img,'img/'+str(i)+'.bmp',h,w)
