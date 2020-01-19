依赖注入（Dependency Injection）又称控制反转（Inversion of Control）主要用来实现不同模块或类之间的解耦，可以根据需要动态地把某种依赖关系注入到对象中，使得模块的设计更加独立。同时，依赖注入也是多态的一种实现方式。常用的依赖注入途径有接口注入、Set注入和构造注入三种。另外，反射也属于比较常用的依赖注入技术之一，可以根据给定的不同信息创建不同类型的对象。

（1）接口注入

该技术首先定义一个接口类，然后在继承了该接口的类中实现特定的接口方法，而在接口方法中根据传入参数的不同做出不同的行为。

class Itest:  #接口

 def injection(self, testClass):

        ''''''

class Test(Itest): #继承接口

 def injection(self, testObject): #实现接口方法

        self.object = testObject

 def show(self):  #普通方法

 print(self.object)

class A:  #类A和B是测试用的

 pass

class B:

 pass

t = Test()

t.injection(A()) #传入不同类型的对象

t.show()

t.injection(B())

t.show()

上面代码运行结果为：

<__main__.A object at 0x00000000033F6B70>

<__main__.B object at 0x000000000339B470>

（2）Set注入

这种注入方式是通过类本身提供的一个方法用来注入不同类型的对象来设置自身对象和其他对象的依赖关系。

class Test:

 def setObject(self, testObject):#可实现依赖注入

        self.object = testObject

 def show(self):

 print(self.object)

class A:

 pass

class B:

 pass

t = Test()

t.setObject(A()) #传入不同类型的对象

t.show()

t.setObject(B())

t.show()

（3）构造注入

这种注入方式是在创建类的实例时为构造方法传入不同类型的对象实现的。

class Test:

 def __init__(self, testObject): #通过构造方法实现依赖注入

        self.object = testObject

 def show(self):

 print(self.object)

class A:

 pass

class B:

 pass

t1 = Test(A())#为构造方法传入不同类型的对象

t1.show()

t2 = Test(B())

t2.show()

（4）反射

通过反射技术可以根据传入信息（例如类的名字）的不同来创建不同类型的对象，从而实现多态和依赖注入。

class Animal: #定义一个类

 def __init__(self, name):

        self.name = name

 def show(self):

 print(self.name)

class Person(Animal): #继承Animal类，也可以是一个普通的新类

 pass

a = globals()['Animal']('dog') #简单形式的反射

a.show()

p = globals()['Person']('Zhangsan') #根据类的名字不同来创建不同的对象

p.show()

下面代码演示了反射的另一种方式：

class Animal: #定义一个类

 def __init__(self, name):

        self.name = name

 def show(self):

 print(self.name)

class Person(Animal): #继承Animal类，也可以是一个普通的新类

 pass

def createObject(testClass, name):

 return testClass(name)

a = createObject(Animal, 'dog') #创建不同类型的对象

a.show()

p = createObject(Person, 'Zhangsan')

p.show()