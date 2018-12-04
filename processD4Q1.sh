sed s/'\['// D4Q1.txt > tmp1.txt
sed s/'\]'// tmp1.txt > tmp2.txt
sed s/'-'//g tmp2.txt > tmp3.txt
sed s/':'// tmp3.txt > tmp4.txt
sed s/' '// tmp4.txt > tmp5.txt
sort -k 1 -n tmp5.txt > tmp6.txt
