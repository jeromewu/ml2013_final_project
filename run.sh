for i in 10
do
  sh img.sh $i $i
  ./trans.py img.convert $i $i test1.label.dat > test1.label.crop.1.($i)x($i).dat
  svm-train train.crop.1.($i)x($i).dat train.crop.1.($i)x($i).model
  svm-predict test1.label.crop.1.($i)x($i).dat train.crop.1.($i)x($i).model train.crop.1.($i)x($i).out
done
