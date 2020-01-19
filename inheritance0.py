class Person():
    """
    父类中的属性是私有的，子类根本不知道父类里的属性是什么。
    子类也不知道父类在初始化操作过程中做了哪些工作。
    所以谁的内容就交给谁去执行是最安全的。
    """
    def __init__(self, name):
        self.__name = name
        print('Peron init...')

    def get_name(self):
        return self.__name


class Father(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.__age = age
        print('Father init...')

    def get_age(self):
        return self.__age


class Son(Father):
    def __init__(self, name, age, gender):
        Father.__init__(self, name, age)
        self.__gender = gender
        print('Son init...')

    def get_gender(self):
        return self.__gender


s = Son('Tom', 18, '男')
print(s.get_name(), s.get_age(), s.get_gender())
