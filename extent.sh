#!/bin/bash
rm extent/*
cd img.convert
for img in `ls`
do
  convert $img -gravity center -background black -extent 28x28 ../extent/$img
done
