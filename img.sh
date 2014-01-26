#!/bin/bash
rm img.convert/*
cd img
for img in `ls`
do
  convert $img -resize $1x$2! ../img.convert/$img
done
