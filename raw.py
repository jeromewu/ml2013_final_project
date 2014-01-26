#!/usr/bin/env python2
from svmutil import *
from img_util import *
import sys

HEIGHT=48
WIDTH=40

y,x=svm_read_problem(sys.argv[1])
size = len(x)
for i in range(0,size):
  output = ''
  img = to_img_array(x[i],HEIGHT,WIDTH)
  for j in range(0,len(img)):
    output += str(img[j])+' '
  output += str(int(y[i]))
  print output
