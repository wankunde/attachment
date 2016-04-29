
# Stop Hive MetaStore and Hive Server
 
> sudo service hive-metastore stop
> sudo service hive-server2 stop

# Dump myql数据

执行脚本 ： sh mysql_export.sh，
导出结果文件为data2.sql

# 数据灌入Oracle
拷贝data2.sql文件到oracle导入目录，执行数据导入程序
sqlplus meta_store/paic1234@JZTEST @load.sql
# 修改hive metastore为oracle
/etc/hive/conf/ hive-site.xml
```
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:oracle:thin:@10.20.19.78:1521:jztest</value>
    <description>the URL of the MySQL database</description>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>oracle.jdbc.driver.OracleDriver</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>META_STORE</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>paic1234</value>
  </property>
```

# Start Hive MetaStore and Hive Server

> sudo service hive-metastore start
> sudo service hive-server2 start

# Database data check
mysql 数据查询
> 
mysql -u hive -phive -h datanode3 --database=metastore -e "select 'CDS',COUNT(1) from CDS t UNION ALL 
select 'SDS',COUNT(1) from SDS t UNION ALL 
select 'TBLS',COUNT(1) from TBLS t UNION ALL 
select 'PARTITIONS',COUNT(1) from PARTITIONS t UNION ALL 
select 'FUNCS',COUNT(1) from FUNCS t"
 
oracle数据查询
进入sqlplus，查询
> 
select 'CDS',COUNT(1) from CDS t UNION ALL 
select 'SDS',COUNT(1) from SDS t UNION ALL 
select 'TBLS',COUNT(1) from TBLS t UNION ALL 
select 'PARTITIONS',COUNT(1) from PARTITIONS t UNION ALL 
select 'FUNCS',COUNT(1) from FUNCS t

# Schama备注

* [HIVE-7018][2] 在HIVE-7018中，mysql的schema中，TBLS表和PARTITIONS表的字段会有*LINK_TARGET_ID NUMBERLINK_TARGET_ID NUMBER*字段，hive没有使用这两个字段，这个在oracle等其他数据库的元数据库中没有，而且，后期mysql的元数据升级的时候会直接删除这两个字段。
https://github.com/apache/hive/blob/master/metastore/scripts/upgrade/mysql/021-HIVE-7018.mysql.sql
 
* SDS表中字段 IS_STOREDASSUBDIRECTORIES NUMBER(1) NOT NULL CHECK (IS_STOREDASSUBDIRECTORIES IN (1,0))在表中顺序在mysql schema和oracle schema不同，在迁移数据的时候需要特殊处理。

# 说明
* 在迁移过程中，mysql metastore会停止，dba如果支持的话，是否可以考虑设置为只读模式。
* 数据导入Oracle的过程还是很慢，使用了Append，Nologging，PL/SQL等技术优化，看dba支持吧。
 



[2]:(https://issues.apache.org/jira/browse/HIVE-7018 "HIVE-7018")
