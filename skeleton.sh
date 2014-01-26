#!/bin/bash
rm skeleton/*
cd img.convert
for img in `ls`
do
  convert $img -morphology Thinning:-1 Skeleton ../skeleton/$img
done
