"""
# 多态（英语：Polymorphism），
     是指物件导向程式执行时，
     相同的讯息可能会送給多个不同的类別之物件，
     而系统可依剧物件所属类別，引发对应类別的方法，而有不同的行为。
     简单来说，所谓多型意指相同的讯息給予不同的物件会引发不同的动作称之。

# duck typing
在程序设计中，鸭子类型（英语：duck typing）是动态类型的一种风格。
在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。
“鸭子测试”可以这样表述：“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”


# example
1. obj.count(some) 统计 obj中some的个数
>>> "This is a book".count("s")
2
>>> [1,2,4,3,5,3].count(3)
2

2. + 号的强大
>>> f = lambda x,y:x+y
>>> f(2,3)
5
>>> f("qiw","sir")
'qiwsir'
>>> f(["python","java"],["c++","lisp"])
['python', 'java', 'c++', 'lisp']
>>> f("qiw", 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: cannot concatenate 'str' and 'int' objects

"""


class Logger:
    """

    """

    def record(self):
        print("I write a log into file.")


class DB:
    def record(self):
        print("I insert data into db")


def test(recorder):
    recorder.record()


def demo():
    logger = Logger()
    db = DB()
    test(logger)
    test(db)


if __name__ == '__main__':
    demo()
