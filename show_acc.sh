for i in `ls *.acc`
do
  acc=`cat $i | grep Cross`
  echo $i,$acc
done
