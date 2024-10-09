#!/bin/bash
source activate JUN
#修改种子函数
function alter(){
for seed in `seq 1 1000`
	do
		s=$[42400+$seed*20]
		eval "sed -i '126,126cfix             ins all pour 1000 1 $s region insreg &' in.funnel"
		#echo "sed -n '126,126p' in.funnel"
		eval "bsub -o funnel.log lmp_serial -in in.funnel"
        	sleep 600
		eval "bsub -o move.log mv funnel_z.dump funnel_z.txt"
		      sleep 20
    eval "bsub -o sort.log python sort.py"
		      sleep 30
		eval "bsub -o result.log python a.py"
		      sleep 30
		echo "$s"
		eval "rm -f funnel_z.txt"
		eval "rm -f funnel_z.csv"
	done
}
alter
