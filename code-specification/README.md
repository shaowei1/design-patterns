code specification

命名与注释（Naming and Comments）、代码风格（Code Style）和编程技巧（Coding Tips）

# 命名和注释

## 命名

> 以能准确达意为目标
>
> 换位思考，假设自己不熟悉这块代码，从代码阅读者的角度去考量命名是否足够直观。

### 包名、类名（github）

比较熟的词语使用缩写: Sec, str, doc, num

对于作用域比较小的变量，我们可以使用相对短的命名，比如一些函数内的临时变量。相反，对于类名这种作用域比较大的，我更推荐用长的命名方式

### 利用上下文简化命名

```java
public class User {
  private String userName;
  private String userPassword;
  private String userAvatarUrl;
  //...
}

// 在使用这些属性时候，我们能借助对象这样一个上下文，表意也足够明确
User user = new User();
user.getName(); // 借助user对象这个上下文

// 除了类之外，函数参数也可以借助函数这个上下文来简化命名

public void uploadUserAvatarImageToAliyun(String userAvatarImageUri);
//利用上下文简化为：
public void uploadUserAvatarImageToAliyun(String imageUri);
```

### 命名要可读、可搜索

我在 Google 参与过的一个项目，名叫 inkstone，虽然你不一定知道它表示什么意思，但基本上都能读得上来，不影响沟通交流，这就算是一个比较好的项目命名。

我们再来讲一下命名可搜索。我们在 IDE 中编写代码的时候，经常会用“关键词联想”的方法来自动补全和搜索。比如，键入某个对象“.get”，希望 IDE 返回这个对象的所有 get 开头的方法。再比如，通过在 IDE 搜索框中输入“Array”，搜索 JDK 中数组相关的类。所以，我们在命名的时候，最好能符合整个项目的命名习惯。大家都用“selectXXX”表示查询，你就不要用“queryXXX”；大家都用“insertXXX”表示插入一条数据，你就要不用“addXXX”，统一规约是很重要的，能减少很多不必要的麻烦。

### 如何命名接口和抽象类？

对于接口的命名，一般有两种比较常见的方式。一种是加前缀“I”，表示一个 Interface。比如 IUserService，对应的实现类命名为 UserService。另一种是不加前缀，比如 UserService，对应的实现类加后缀“Impl”，比如 UserServiceImpl。对于抽象类的命名，也有两种方式，一种是带上前缀“Abstract”，比如 AbstractConfiguration；另一种是不带前缀“Abstract”。实际上，对于接口和抽象类，选择哪种命名方式都是可以的，只要项目里能够统一就行。

## 注释

### 注释到底该写什么？

> 注释的目的就是让代码更容易看懂
>
> 做什么、为什么、怎么做

```java
/**
* (what) Bean factory to create beans. 
* 
* (why) The class likes Spring IOC framework, but is more lightweight. 
*
* (how) Create objects from different sources sequentially:
* user specified object > SPI > configuration > default object.
*/
public class BeansFactory {
  // ...
}
```



- 注释比代码承载的信息更多

命名的主要目的是解释“做什么”。比如，void increaseWalletAvailableBalance(BigDecimal amount) 表明这个函数用来增加钱包的可用余额，boolean isValidatedPassword 表明这个变量用来标识是否是合法密码。函数和变量如果命名得好，确实可以不用再在注释中解释它是做什么的。但是，对于类来说，包含的信息比较多，一个简单的命名就不够全面详尽了。这个时候，在注释中写明“做什么”就合情合理了。

- 注释起到总结性作用、文档的作用

在注释中，关于具体的代码实现思路，我们可以写一些总结性的说明、特殊情况的说明。这样能够让阅读代码的人通过注释就能大概了解代码的实现思路，阅读起来就会更加容易。

实际上，对于有些比较复杂的类或者接口，我们可能还需要在注释中写清楚“如何用”，举一些简单的 quick start 的例子，让使用者在不阅读代码的情况下，快速地知道该如何使用。

- 一些总结性注释能让代码结构更清晰

  对于逻辑比较复杂的代码或者比较长的函数，如果不好提炼、不好拆分成小的函数调用，那我们可以借助总结性的注释来让代码结构更清晰、更有条理。

  ```java
  public boolean isValidPasword(String password) {
    // check if password is null or empty
    if (StringUtils.isBlank(password)) {
      return false;
    }
  
    // check if the length of password is between 4 and 64
    int length = password.length();
    if (length < 4 || length > 64) {
      return false;
    }
      
    // check if password contains only a~z,0~9,dot
    for (int i = 0; i < length; ++i) {
      char c = password.charAt(i);
      if (!((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || c == '.')) {
        return false;
      }
    }
    return true;
  }
  ```

  

### 注释是不是越多越好？

类和函数一定要写注释，而且要写得尽可能全面、详细，而函数内部的注释要相对少一些，一般都是靠好的命名、提炼函数、解释性变量、总结性注释来提高代码的可读性。

## sumarry

1. 关于命名
   - 命名的关键是能准确达意。对于不同作用域的命名，我们可以适当地选择不同的长度。作用域小的变量（比如临时变量），可以适当地选择短一些的命名方式。除此之外，命名中也可以使用一些耳熟能详的缩写。
   - 我们可以借助类的信息来简化属性、函数的命名，利用函数的信息来简化函数参数的命名。
   - 命名要可读、可搜索。不要使用生僻的、不好读的英文单词来命名。除此之外，命名要符合项目的统一规范，不要用些反直觉的命名。
   - 接口有两种命名方式：一种是在接口中带前缀“I”；另一种是在接口的实现类中带后缀“Impl”。对于抽象类的命名，也有两种方式，一种是带上前缀“Abstract”，一种是不带前缀。这两种命名方式都可以，关键是要在项目中统一。
2. 关于注释
   - 注释的目的就是让代码更容易看懂。只要符合这个要求的内容，你就可以将它写到注释里。总结一下，注释的内容主要包含这样三个方面：做什么、为什么、怎么做。对于一些复杂的类和接口，我们可能还需要写明“如何用”。
   - 注释本身有一定的维护成本，所以并非越多越好。类和函数一定要写注释，而且要写得尽可能全面、详细，而函数内部的注释要相对少一些，一般都是靠好的命名、提炼函数、解释性变量、总结性注释来提高代码可读性。

# Code Style

> 我们做到的，是在团队、项目中保持风格统一，让代码像同一个人写出来的，整齐划一。这样能减少阅读干扰，提高代码的可读性。这才是我们在实际工作中想要实现的目标

## 类、函数多大才合适？

- 如果要让一个函数的代码完整地显示在 IDE 中，那最大代码行数不能超过 50。
- 当一个类的代码读起来让你感觉头大了，实现某个功能时不知道该用哪个函数了，想用哪个函数翻半天都找不到了，只用到一个小功能要引入整个类（类中包含很多无关此功能实现的函数）的时候，这就说明类的行数过多了。

## 一行代码多长最合适？

[Java code style]: https://google.github.io/styleguide/javaguide.html
[Python code style]: https://github.com/google/styleguide/blob/gh-pages/pyguide.md



- 一行代码最长限制为 100 个字符
- 一行代码最长不能超过 IDE 显示的宽度。需要滚动鼠标才能查看一行的全部代码，显然不利于代码的阅读。当然，这个限制也不能太小，太小会导致很多稍长点的语句被折成两行，也会影响到代码的整洁，不利于阅读。

## 善用空行分割单元块

- 对于比较长的函数，如果逻辑上可以分为几个独立的代码块，在不方便将这些独立的代码块抽取成小函数的情况下，为了让逻辑更加清晰，除了上一节课中提到的用总结性注释的方法之外，我们还可以使用空行来分割各个代码块。
- 在类的成员变量与函数之间、静态成员变量与普通成员变量之间、各函数之间、甚至各成员变量之间，我们都可以通过添加空行的方式，让这些不同模块的代码之间，界限更加明确。写代码就类似写文章，善于应用空行，可以让代码的整体结构看起来更加有清晰、有条理。

## 四格缩进还是两格缩进？

- 还有一个选择的标准，那就是跟业内推荐的风格统一、跟著名开源项目统一。当我们需要拷贝一些开源的代码到项目里的时候，能够让引入的代码跟我们项目本身的代码，保持风格统一。
- 一定不要用 tab 键缩进。因为在不同的 IDE 下，tab 键的显示宽度不同，

## 大括号是否要另起一行？

```java

// PHP  左右括号可以垂直对齐，哪些代码属于哪一个代码块，更一目了然。
class ClassName
{
    public function foo()
    {
        // method body
    }
}

// Java  节省代码行数
public class ClassName {
  public void foo() {
    // method body
  }
}
```

## 类中成员的排列顺序

- 在 Google 编码规范中，依赖类按照字母序从小到大排列。
- 在类中，成员变量排在函数的前面。成员变量之间或函数之间，都是按照“先静态（静态函数或静态成员变量）、后普通（非静态函数或非静态成员变量）”的方式来排列的。除此之外，成员变量之间或函数之间，还会按照作用域范围从大到小的顺序来排列，先写 public 成员变量或函数，然后是 protected 的，最后是 private 的。
- 还有另外一种排列习惯，那就是把有调用关系的函数放到一块。比如，一个 public 函数调用了另外一个 private 函数，那就把这两者放到一块。

