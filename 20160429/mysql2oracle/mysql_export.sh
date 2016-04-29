#!/bin/bash

mysql_user=hive
mysql_password=hive123
mysql_host=26.6.0.31

# uat
# mysql_user=hive
# mysql_password=hive
# mysql_host=datanode3

rm -rf data1.sql
rm -rf data2.sql
mysqldump -u ${mysql_user}  \
        -p${mysql_password}  \
        -h ${mysql_host} \
        --no-create-info \
        --compact \
        --compatible=oracle  \
        --skip-add-locks  \
        --extended-insert=false \
        metastore > data1.sql
python tool.py
