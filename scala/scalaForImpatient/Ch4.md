## 映射和元组
- `->`操作符用来创建对偶，映射是一种将键映射成值的函数，通常的函数返回值，但是映射只做查询
- 构造一个映射，值不可被改变
    ```scala
    scala> val scores=Map("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
    scores: scala.collection.immutable.Map[String,Int] = Map(Alice -> 10, Bob -> 3, Cindy -> 8)
    ```
- 构造一个可变映射
     ```scala   
    scala> val Mscores=scala.collection.mutable.Map("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
    Mscores: scala.collection.mutable.Map[String,Int] = Map(Bob -> 3, Alice -> 10, Cindy -> 8)
    ```

- 获取键中的值，用`()`来查找某个键对应的值
    - 如果映射中不包含请求中使用的键，自会抛出异常
    - 检查映射中是否有某个制定的键，可以用`contains`方法
        ```scala
        scala> val bobsScore = if (scores.contains("Bob")) scores("Bob") else 0
        bobsScore: Int = 3
        ```
    - 快捷方法，如果映射中包含指定键就返回对应的值，否则返回固定默认值
        ```scala
        scala> val bobsScore = scores.getOrElse("xhades", "not contain")
        bobsScore: Any = not contain
        ```
    -  `映射.get()`返回一个`Option`对象，要么是`Some`，要么是`None`
        ```scala
        scala> val bobsScore = scores.get("Bob")
        bobsScore: Option[Int] = Some(3)

        scala> val bobsScore = scores.get("xhades")
        bobsScore: Option[Int] = None
        ```

- 更新映射中的值  
    - 可变映射中，映射(键)=新的值或者也可以使用`+=`添加多个关系
        ```scala
        scala> Mscores
        res0: scala.collection.mutable.Map[String,Int] = Map(Bob -> 3, Alice -> 10, Cindy -> 8)

        scala> Mscores("Bob") = 4

        scala> Mscores
        res2: scala.collection.mutable.Map[String,Int] = Map(Bob -> 4, Alice -> 10, Cindy -> 8)

        scala> Mscores+=("David" -> 15)
        res3: Mscores.type = Map(Bob -> 4, Alice -> 10, David -> 15, Cindy -> 8)
        ```
    - 移除某个键对应的值，使用`-=`

    - 更新不可变的映射
        ```scala
        scala> scores
        res4: scala.collection.immutable.Map[String,Int] = Map(Alice -> 10, Bob -> 3, Cindy -> 8)

        scala> val newScores = scores + ("Bob" -> 5)
        newScores: scala.collection.immutable.Map[String,Int] = Map(Alice -> 10, Bob -> 5, Cindy -> 8)
        ```

- 已排序映射
    - 映射有两种常见的实现策略：`哈希表`和`平衡树`。哈希表使用键的哈希码来划定位置，因此遍历会以一种不可预期的顺序交出元素，Scala默认给你的是基于哈希表的映射
    - 如果需要按照顺序依次访问映射中的键，可以使用`SortedMap`
        ```scala
        scala> val scores=scala.collection.mutable.SortedMap("Alice" -> 10, "Fred" -> 5, "Bob" -> 4)
        scores: scala.collection.mutable.SortedMap[String,Int] = TreeMap(Alice -> 10, Bob -> 4, Fred -> 5)
        ```
    - 按照插入顺序访问所有键，使用`LinkedHashMap`

- 元组  
    元组是不同类型的值得聚集

- 拉链操作
```scala
scala> val symbols=Array("<", "-",">")
symbols: Array[String] = Array(<, -, >)

scala> val counts = Array(2,20,2)
counts: Array[Int] = Array(2, 20, 2)

scala> val pairs = symbols.zip(counts)
pairs: Array[(String, Int)] = Array((<,2), (-,20), (>,2))
```