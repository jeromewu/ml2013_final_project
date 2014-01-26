#!/usr/bin/env python2

from svmutil import *

y_ans,x_blank = svm_read_problem('ans1.dat')

i = 0
for line in open('ml2013final_test1.nolabel.dat','r'):
  output = str(int(y_ans[i])) + ' '
  data = line.split()
  for j in range(1,len(data)):
    output += data[j] +' '
  i += 1
  print output
