#!/usr/bin/env bash

SCANDIR="/eos/user/e/evanbrug/monosbb-50"
OUTDIR="monosbb"
XPARAM="mhs"
YPARAM="mzp"

for i in {01..12}
do
	if [ ! -f $SCANDIR/Events/run_${i}/run_${i}_tag_1_banner.txt ]; then
		echo "$i banner not found"
		continue
	fi
	if [ ! -f $SCANDIR/HTML/run_${i}/tag_1_MA5_HADRON_ANALYSIS_Recasting/Output/SAF/CLs_output_summary.dat ]; then
		echo "$i CL file not found"
		continue
	fi
	X=$(grep $XPARAM $SCANDIR/Events/run_${i}/run_${i}_tag_1_banner.txt | awk '{print $2}')
	printf -v X "%.f" "$X"
	X=${X%.*}
	Y=$(grep $YPARAM $SCANDIR/Events/run_${i}/run_${i}_tag_1_banner.txt | awk '{print $2}')
	printf -v Y "%.f" "$Y"
	Y=${Y%.*}
	XSEC=$(grep "Integrated weight" $SCANDIR/Events/run_${i}/run_${i}_tag_1_banner.txt | awk '{print $NF}')
	cp $SCANDIR/HTML/run_${i}/tag_1_MA5_HADRON_ANALYSIS_Recasting/Output/SAF/CLs_output_summary.dat $OUTDIR/scan-${X}-${Y}.dat
	echo $XSEC >> $OUTDIR/scan-${X}-${Y}.dat
	echo done $i
done
