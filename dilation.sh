#!/bin/bash
rm dilation/*
cd img.convert
for img in `ls`
do
  convert $img -morphology Dilate Octagon ../dilation/$img
done
