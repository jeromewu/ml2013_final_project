#!/bin/bash
rm binary/*
cd $1
for img in `ls`
do
  convert $img -threshold 10% ../binary/$img
done
