#!/usr/bin/env python2
import numpy as np
from sklearn.decomposition import PCA
from img_util import *
import sys

y,x = readraw(sys.argv[1])
yt,xt = readraw('test1.crop.1.28x28.bin.1.dat.raw')
pca = PCA(n_components=100)
X = pca.fit_transform(x)
Xt = pca.transform(xt)

outX = Xt
outY = yt
for i in range(0,len(outX)):
  output = str(int(outY[i]))+' '
  for j in range(0,len(outX[i])):
    output += str(j+1)+':'+str(outX[i,j])+' '
  print output
