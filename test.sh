#!/bin/bash

for i in /home1/scratch/shabtes/data_share/daily/*hdf
do 
	out=$(echo $i | sed 's/hdf/png/' | sed 's/daily/daily_png/')
	python PngGenerator.py -f $i  -m test/chlor_a_gcoos_mask.png -c np.log10\(data+1\)/0.00519 -o $out -s chlor_a -u NaN -l NaN
done
#$python PngGenerator.py -f /home1/scratch/shabtes/data_share/daily/AQUA.20120531.0000.gcoos.oc.hdf  -m test/chlor_a_gcoos_mask.png -c np.log10\(data+1\)/0.00519 -o test/test/chlor_a.png -s chlor_a -u NaN -l NaN
