- 声明变量，变量或函数的类型总是写在变量或函数名称的后面
    ```scala
    scala> val greeting: String = "hello"
    greeting: String = hello
    ```
- scala常用数据类型：七种数值类型：`Byte`、`Char`、`Short`、`Int`、`Long`、`Float`和`Double`以及一个`Boolean`类型。这些类型都是类。Scala并不可以区分基本类型和引用类型，可以对数字执行方法
    ```scala
    scala> 1.to(10)
    res2: scala.collection.immutable.Range.Inclusive = Range 1 to 10
    ```

- Scala中操作符也是方法  
a 方法 b 通常是 a.方法(b)的简写

- apply方法

