#!/bin/bash
rm edge/*
cd dilation
for img in `ls`
do
  convert $img -edge 1 ../edge/$img
done
