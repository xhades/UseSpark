> scala学习笔记

# Day01
## 0 scala解释器的使用
- REPL：read -> evaluation -> print -> loop。scala解释器也称为REPL，会快速将scala代码编写为字节码，然后交由Java虚拟机来运行
```shell
    promote:~ xhades$ scala
    Welcome to Scala 2.12.1 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_121).
    Type in expressions for evaluation. Or try :help.
scala>
```
- Java和Scala可以无缝互操作，Scala可以任意调用Java的代码

## 1 声明变量
- 声明val变量
常量声明之后，是无法改变它的值的
```shell
    scala> val a = 1 + 1
    a: Int = 2

```
- 声明var变量
如果要声明值可以改变的引用，可以使用var变量
```shell
    scala> var b = 2
    b: Int = 2
```
- 指定类型
无论声明var变量还是val变量，都可以手动指定其类型，如果指定的话，scala会自动根据值进行类型的推断
```shell
    scala> var name: String=null
    name: String = null
```
- 声明多个变量
可以将多个变量放在一起进行声明
```shell
    scala> val num1, num2 = 100
    num1: Int = 100
    num2: Int = 100
```

## 2 数据类型和操作符
- 基本的数据类型
Byte、Char、Short、Int、Long、Float、Double、Boolean  
    - Scala没有基本数据类型和包装类型的概念，统一都是类。scala自身会负责基本数据类型和引用类型的转换操作
    - 使用以上类型，直接接可以调用大量的函数
        ```shell
        scala> 1.toString
        res0: String = 1 
        ```

- 类型的加强版类型
scala使用很多加强类给数据类型增加了上百种增强的功能或函数
    - 例如，String通过StringOps增强了大量的函数
        ```shell
        scala> "Hello".intersect("World")
        res1: String = lo
        ```

## 3 函数调用
- 函数调用方式
  在scala中，函数调用也很简单  
  例如，import scala.math._，sqrt(2)  
  不同的一点是，如果调用函数时，不需要传递参数，则scala允许调用函数时省略括号，例如，"Hello World".distinct

- apply函数

## 4 if表达式
- if表达式的定义： 在scala中，if表达式是有值的，就是if或者else中最后一行语句返回的值
    - 例如：
        ```shell
        scala> val age=30
        age: Int = 30
        scala> if(age>18) 1 else 0
        res2: Int = 1
        ```
    - 可以将if表达式赋予一个变量，
        ```shell
        scala> val isAdult = if(age>18) 1 else 0
        isAdult: Int = 1
        ```
    - if表达式的类型推断
    由于if表达式是有值的，而if和else子句的值类型可能不同，此时if表达式的值类型scala会自动进行推断，取两个类型的公共父类型
        ```shelll
        scala> val isAdult = if(age>18) "adult" else 0
        isAdult: Any = adult
        ```
    - if放在多行中


# Day02
## 1 语句终结符、块表达式
- 默认情况下，scala不需要语句终结符，默认将每一行作为一个语句

- 一行放多条语句

- 块表达式： 块表达式指的是{}中的值，其中可以包含多条语句，最后一个语句的值就是块表达式的返回值
    ```shell
    scala> a
    res5: Int = 2

    scala> c
    res6: Int = 3

    scala> val d = if(a<10){b=b+1;c+1}
    d: AnyVal = 4
    ```

## 2 输入和输出
- print和println  
print打印时不会加换行符， 而println会加上一个换行符
- printf可以用格式化
- readLine

## 3 循环
- while do循环
- scala没有for循环，只能用while替代for循环，或者简易版的for语句
    - 简易版for语句
        ```shell
        scala> val n  = 10
        n: Int = 10

        scala> for(i <- 1 to n) print(i + " ")
        1 2 3 4 5 6 7 8 9 10
        ```
    - 或者使用until，表达式不到上限
        ```shell
        scala> for(i <- 1 until n) print(i + " ")
        1 2 3 4 5 6 7 8 9
        ```
- 跳出循环语句  
scala中没有提供类似于java的break语句
但是可以使用boolean类型变量、return或者Breaks的break函数来替代使用
    ```shell
    scala> import scala.util.control.Breaks._
    import scala.util.control.Breaks._

    scala> breakable{
        | var n = 10
        | for(c <- "Hello World"){
        | if(n==5) break;
        | print(c)
        | n -= 1
        | }
        | }
    Hello
    ```

## 4 高级for循环
- 多重for循环
- if守卫
- for推导式： yield构造集合
    ```shell
    scala> for(i <- 1 to 10) yield i
    res12: scala.collection.immutable.IndexedSeq[Int] = Vector(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    ```
## 5 定义函数
- 在scala中定义函数时，需要定义函数的函数名、参数、函数体  
- scala要求必须给出所有参数的类型，但是不一定给出函数返回值的类型，只要右侧的函数体中不包含递归的语句，scala就可以根据右侧的表达式推断出返回类型
## 6 递归函数

# Day03
## 1 函数默认参数
## 2 带名参数
## 3 变长参数
在scala中，有时我们需要将函数定义为参数个数可变的形式，则此时可以使用变长参数定义函数
    ```shell
    scala> def sum(nums: Int*) = {
        | var result = 0
        | for (num <- nums){
        | result += num
        | }
        | result
        | }
    sum: (nums: Int*)Int

    scala> sum(1,2,3)
    res18: Int = 6
    ```
## 4 使用序列调用变长参数
在如果想要将一个已有的序列直接调用变长参数函数，是不对的。比如val s = sum(1 to 5)。此时需要使用scala特殊的语法将参数定义为序列，让scala解释器能够识别。
    ```shell
    scala> val s = sum(1 to 5: _*)
    s: Int = 15
    ```
## 5 过程
在scala中，定义函数时，如果函数体直接包裹在了花括号里面，而没有使用=连接，则函数的返回值类型就是Unit。这样的函数被称之为`过程`。过程常用于不需要返回值的函数。  
过程还有一种写法，就是将函数的返回值类型定义为`Unit`
    ```shell
    scala> def sayHello(name: String){print("Hello"+ name)}
    sayHello: (name: String)Unit
    
    scala> def sayHello(name: String): Unit = "Hello"+ name
    sayHello: (name: String)Unit
    ```

## 6 lazy值
在scala中，提供了lazy值的特性，也就是说，如果将一个变量声明为lazy，则只有在第一次使用该变量时，变量对应的表达式才会发生计算，这种特性对于特别耗时的计算操作特别有用，比如打开文件进行IO，进行网络IO等
    ```shell
    scala> import scala.io.Source._
    import scala.io.Source._

    scala> lazy val lines = fromFile("/Usrs/xhades/tmp.txt")
    lines: scala.io.BufferedSource = <lazy>

    scala> lazy val lines = fromFile("/Usrs/xhades/tmp.txt").mkString
    lines: String = <lazy>

    scala> print(lines)
    java.io.FileNotFoundException: /Usrs/xhades/tmp.txt (No such file or directory) 
    at java.io.FileInputStream.open0(Native Method)
    at java.io.FileInputStream.open(FileInputStream.java:195)
    at java.io.FileInputStream.<init>(FileInputStream.java:138)
    at scala.io.Source$.fromFile(Source.scala:91)
    at scala.io.Source$.fromFile(Source.scala:76)
    at scala.io.Source$.fromFile(Source.scala:54)
    at .lines$lzycompute(<console>:17)
    at .lines(<console>:17)
    ... 29 elided
    ```

## 7 异常
case
## 8 Array
在scala中， Array代表长度不可变的数组，此外由于scala与java都是运行在jvm中，双方可以互相调用，因此scala数组的底层实际上是java数组