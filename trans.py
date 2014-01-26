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

y, x = svm_read_problem(sys.argv[4])
#y, x = svm_read_problem('train.small.dat')
for i in range(0,len(x)):
  try:
    img = input_bmp(sys.argv[1]+'/'+str(i)+'.bmp')
    #img = to_binary_image(img,0.7,48,40)
    output(y[i],img,int(sys.argv[3]),int(sys.argv[2]))
  except Exception as e:
    print '0 1:0'
    continue
