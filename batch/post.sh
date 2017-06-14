#!/bin/bash

d=`date +%Y%m%d`
file=./output/${d}

declare -A price_map=()
price_map["has_pr_0"]=`grep "_0\\$" ${file} | wc -l`
price_map["has_pr_1"]=`grep "_01_0\\$" ${file} | wc -l`
price_map["has_pr_2"]=`grep "_02_0\\$" ${file} | wc -l`
price_map["has_pr_3"]=`grep "_03_0\\$" ${file} | wc -l`
price_map["has_pr_4"]=`grep "_04_0\\$" ${file} | wc -l`
price_map["has_pr_5"]=`grep "_05_0\\$" ${file} | wc -l`
price_map["has_pr_6"]=`grep "_06_0\\$" ${file} | wc -l`
price_map["has_pr_7"]=`grep "_07_0\\$" ${file} | wc -l`
price_map["has_pr_8"]=`grep "_08_0\\$" ${file} | wc -l`
price_map["has_pr_9"]=`grep "_09_0\\$" ${file} | wc -l`
price_map["has_pr_10"]=`grep "_10_0\\$" ${file} | wc -l`
price_map["has_pr_11"]=`grep "_11_0\\$" ${file} | wc -l`
price_map["has_pr_12"]=`grep "_12_0\\$" ${file} | wc -l`

price_map["all_0"]=`cat ${file} | wc -l`
price_map["all_1"]=`grep "_01_" ${file} | wc -l`
price_map["all_2"]=`grep "_02_" ${file} | wc -l`
price_map["all_3"]=`grep "_03_" ${file} | wc -l`
price_map["all_4"]=`grep "_04_" ${file} | wc -l`
price_map["all_5"]=`grep "_05_" ${file} | wc -l`
price_map["all_6"]=`grep "_06_" ${file} | wc -l`
price_map["all_7"]=`grep "_07_" ${file} | wc -l`
price_map["all_8"]=`grep "_08_" ${file} | wc -l`
price_map["all_9"]=`grep "_09_" ${file} | wc -l`
price_map["all_10"]=`grep "_10_" ${file} | wc -l`
price_map["all_11"]=`grep "_11_" ${file} | wc -l`
price_map["all_12"]=`grep "_12_" ${file} | wc -l`

declare -A rate=()
for ((i=0;i<13;i++));
do
    if [ ${price_map["all_"$i]} -gt 0 ];then 
        rate[$i]=`echo "scale=2; ${price_map["has_pr_"$i]}/${price_map["all_"$i]}" | bc | awk '{printf "%.2f", $0}'`
    else
        rate[$i]=0.0
    fi
done

# to mysql
HOSTNAME="192.168.14.170"
PORT="3306"
USERNAME="spider"
PASSWORD="spider2013"
DBNAME="price"

today=`date +%Y-%m-%d`
insert_table_sql="
  REPLACE INTO list_cache_price VALUES (
  \"${today}\",${rate[0]},${rate[1]},${rate[2]},${rate[3]},${rate[4]},${rate[5]},${rate[6]},${rate[7]},${rate[8]},${rate[9]},${rate[10]},${rate[11]},${rate[12]});"

# echo ${insert_table_sql}
mysql -h${HOSTNAME} -P${PORT} -u${USERNAME} -p${PASSWORD} ${DBNAME} -e "${insert_table_sql}"
