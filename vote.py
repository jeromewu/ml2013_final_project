#!/usr/bin/env python2
from svmutil import *
import sys

filelist = 'votelist'
Y = []
y_ans,x = svm_read_problem('ans1.dat')

acc = 0.0

for line in open(filelist,'r'):
  data = line.split()
  for i in range(0,len(data)):
    y,x = svm_read_problem(data[i])
    Y.append(y)
for i in range(0,len(Y[0])):
  tmp = []
  for j in range(0,len(Y)):
    tmp.append(Y[j][i])
  if y_ans[i] == max(set(tmp),key=tmp.count):
    acc += 1.0/len(Y[0])
print acc
