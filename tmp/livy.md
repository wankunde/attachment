# 环境搭建

* 官网： http://livy.incubator.apache.org/
* [Download](http://mirrors.tuna.tsinghua.edu.cn/apache/incubator/livy/0.6.0-incubating/apache-livy-0.6.0-incubating-bin.zip)

```bash
export HADOOP_CONF_DIR=/etc/hadoop/conf
export SPARK_HOME=
export SPARK_CONF_DIR=...

unzip apache-livy-0.6.0-incubating-bin.zip
cd apache-livy-0.6.0-incubating-bin
./bin/livy-server start
```
服务启动后，访问页面：http://IP:8998/ui

任务的提交有如下两种：
* http方式提交Job，比较适合于 pySpark 和 SparkR 的程序 
* Java编程接口提交Job，比较适合于框架来调度Spark程序