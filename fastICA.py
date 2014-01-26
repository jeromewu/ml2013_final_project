#!/usr/bin/env python2
import numpy as np
from sklearn.decomposition import FastICA
from img_util import *

y,x = readraw('train.crop.1.8x8.dat.raw')
x = x[:20]

ica = FastICA()
S = ica.fit_transform(x)
print S
