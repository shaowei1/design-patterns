"""
接口继承实质上是要求“做出一个良好的抽象，这个抽象规定了一个兼容接口，使得外部调用者无需关心具体细节，
可一视同仁的处理实现了特定接口的所有对象”——这在程序设计上，叫做归一化。


1.多继承问题
在继承抽象类的过程中，我们应该尽量避免多继承；
而在继承接口的时候，我们反而鼓励你来多继承接口

2.方法的实现
在抽象类中，我们可以对一些抽象方法做出基础实现；
而在接口类中，任何方法都只是一种规范，具体的功能需要子类实现

"""

from abc import abstractmethod, ABCMeta  # 接口类中定义了一些接口名：Pay，且并未实现接口的功能，子类继承接口类，并且实现接口中的功能


class Payment:
    def pay(self):
        raise NotImplementedError  # 手动抛异常


class Payment(metaclass=ABCMeta):  # 抽象出的共同功能Pay
    """
    利用ABC抛异常
    """

    @abstractmethod
    def pay(self, money): pass  # 这里面的pay 来源于下面类中的方法pay,意思把这个方法规范为统一的标准，另外建一个规范类Payment


class Alipay(Payment):
    def paying(self, money):  # 这里出现paying和我们规范的pay不一样，那么在实例化 Alipay的时候就会报错
        print('支付宝支付了')


class Weichat(Payment):
    def pay(self, money):
        print('微信支付了')


def pay(pay_obj, money):
    pay_obj.pay(money)


# p = Alipay()  # 实例化的时候就会报错  Can't instantiate abstract class Alipay with abstract methods pay 之前两个例子都是在执行的时候报错，这里不一样的是实例化就会知道是哪里发生错误了

"""
接口类多继承
"""
from abc import abstractmethod, ABCMeta


class Walk_animal(meteaclass=ABCMeta):
    """
    TypeError: __init_subclass__() takes no keyword arguments
    """

    @abstractmethod
    def walk(self):
        print('walk')


class Swim_animal(meteaclass=ABCMeta):
    @abstractmethod
    def swim(self): pass


class Fly_animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self): pass


# 如果正常一个老虎有跑和跑的方法的话，我们会这么做
class Tiger:
    def walk(self): pass

    def swim(self): pass


# 但是我们使用接口类多继承的话就简单多了，并且规范了相同功能
class Tiger(Walk_animal, Swim_animal):
    pass


# 如果此时再有一个天鹅swan,会飞，走，游泳 那么我们这么做
class Swan(Walk_animal, Swim_animal, Fly_animal): pass
# 这就是接口多继承
