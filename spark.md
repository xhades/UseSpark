Ubuntu16.04中配置Spark运行环境(`Python2.7.12`)
======== 

- 安装`JAVA8`
- 安装`Spark2.1.0`
    - 官网下载`Spark2.1.0`压缩包
    - 解压
        ```shell
        tar -xf spark-2.1.0-bin-hadoop2.7.tgz 
        ```
    - 删除压缩包，重命名文件
        ```shell
        sudo mv spark-2.1.0-bin-hadoop2.7 spark
        rm spark-2.1.0-bin-hadoop2.7.tgz 
        ```
    - 将解压文件移动至`~/spark`文件夹下
        ```shell
        sudo mv spark-2.1.0-bin-hadoop2.7.tgz ~/spark
        ```
    - 至此`Spark`安装完成，使用以下命令测试安装是否有错
        ```shell
        # test spark
        xhades@Cybertron:~/spark$ ./bin/pyspark 
        Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
        [GCC 5.4.0 20160609] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
        Setting default log level to "WARN".
        To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
        17/04/07 18:29:22 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
        17/04/07 18:29:22 WARN Utils: Your hostname, Cybertron resolves to a loopback address: 127.0.1.1; using 192.168.8.23 instead (on interface enp0s31f6)
        17/04/07 18:29:22 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
        17/04/07 18:29:25 WARN ObjectStore: Failed to get database global_temp, returning NoSuchObjectException
        Welcome to
            ____              __
            / __/__  ___ _____/ /__
            _\ \/ _ \/ _ `/ __/  '_/
        /__ / .__/\_,_/_/ /_/\_\   version 2.1.0
            /_/

        Using Python version 2.7.12 (default, Nov 19 2016 06:48:10)
        SparkSession available as 'spark'.
        >>> 

        ```
    - 配置环境变量(待做)

- 运行`WordCount`例子
    - 用`README.md`演示
        ```Python
        >>> textFile = sc.textFile("README.md")
        >>> textFile.count()  # Number of items in this RDD
        104
        >>> textFile.first()  # First item in this RDD
        u'# Apache Spark'
        # Now let’s use a transformation. We will use the filter transformation to return a new RDD with a subset of the items in the file.
        >>> textFile.filter(lambda line: "Spark" in line).count()  # How many lines contain "Spark"?  
        20

        ```
