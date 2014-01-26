#!/usr/bin/env python2.7
from svmutil import *
import math
import numpy as np
import sys
import copy

height = 122
width = 105

def to_img_array(x_i,_height,_width):
  img = []
  for i in range(0,_width*_height):
    img.append(x_i.get(i+1,0))
  return img

def to_binary_image(img,threshold,_height,_width):
  for j in range(0,_width*_height):
    if img[j] > threshold:
      img[j] = 1.0
    else:
      img[j] = 0.0
  return img

def readraw(filename):
  Y = []
  X = []
  for line in open(filename,'r'):
    data = map(float,line.split())
    Y.append(data.pop())
    X.append(data)
  return Y,X

def output(y,img,_height,_width):
  output = str(int(y))+' '
  for i in range(0,_height):
    for j in range(0,_width):
      if img[i*_width+j] != 0:
        output = output + str(int(i*_width+j+1))+':'+str(img[i*_width+j])+' '
  print output

def output_bmp(img,filename,_height,_width):
  BMHEADER = bytearray([
  66, 77,  # BM identifier
  #200, 195, 1, 0,  # size of file in bytes
  0,0,0, 0,   # size of file in bytes
  0, 0, 0, 0,  # unused
  54, 0, 0, 0,  # offset where the data can be found
  40, 0, 0, 0,  # no. of bytes in DIB header from here
  _width, 0, 0, 0,  # bitmap width in pixels
  _height, 0, 0, 0,  # bitmap height in pixels
  1, 0,  # number of colour planes
  24, 0,  # number of bits per pixel (R=G=B=8 bits)
  0, 0, 0, 0,  # no compression
  0, 0, 0, 0,  # size of the raw data
  19, 11, 0, 0,  # horizontal resolution
  19, 11, 0, 0,  # vertical resolution
  0, 0, 0, 0,  # number of colours in the palette
  0, 0, 0, 0,  # all colours important
  ])
  bmp = open(filename,'wb')
  bmp.write(BMHEADER)
  padding = (4 - _width*3%4)%4
  for h in range(0,_height):
    for w in range(0,_width):
      byte = np.uint8(math.ceil((img[(_height-h-1)*_width+w])*255))
      bmp.write(bytearray([byte,byte,byte]))
    for i in range(0,padding):
      bmp.write(bytearray([0]))
  bmp.close()

def input_bmp(filename):
  img = []
  bmp = open(filename,'rb')
  header = bmp.read(138)
  data = bmp.read(1)
  while data != "":
    img.append(int(data.encode('hex'),16)/255.0)
    data = bmp.read(2)  #duplicate part
    data = bmp.read(1)
  bmp.close()
  return img

def crop(img):
  new_img = []
  edge_up = 0
  edge_bottom = 0
  edge_left = 0
  edge_right = 0
  for i in range(0,height):
    for j in range(0,width):
      if img[i*width+j] == 1 and edge_up == 0:
        edge_up = i-1
      if img[(height-i-1)*width+j] == 1 and edge_bottom == 0:
        edge_bottom = height-i
  for i in range(0,width):
    for j in range(0,height):
      if img[j*width+i] == 1 and edge_left == 0:
        edge_left = i-1
      if img[j*width+width-i-1] == 1 and edge_right == 0:
        edge_right = width-i

  for i in range(edge_up,edge_bottom):
    for j in range(edge_left,edge_right):
      new_img.append(img[i*width+j])
  h = edge_bottom-edge_up
  w = edge_right-edge_left
  return new_img,h,w

def cnt_dot(img,grid_size,h,w,_width,threshold):
  total_dot = 0
  for i in range(0,grid_size):
    for j in range(0,grid_size):
      if img[(h+i)*_width+j+w] > threshold:
        total_dot += 1
  return float(total_dot)

def grid(img,grid_size,_height,_width,threshold):
  img_grid = []
  _sum = 0.0
  for h in range(0,_height,grid_size):
    for w in range(0,_width,grid_size):
        img_grid.append(cnt_dot(img,grid_size,h,w,_width,threshold))
        _sum += img_grid[len(img_grid)-1]
  for i in range(0,len(img_grid)):
    img_grid[i] /= _sum
  return img_grid
