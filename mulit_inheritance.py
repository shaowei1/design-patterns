class Person():
    """
    钻石继承，解决多继承多次初始化共同父类的初始化
    1. mro Method Resolution Order 方法解析顺序， 使用的是广度优先算法
    2. show order: print(Son.__mro__)
    3. Son(A, B) A, B的顺序会影响 __mro__的顺序
    """

    def __init__(self, name):
        self.__name = name
        print('Peron init...')

    def get_name(self):
        return self.__name


class Father(Person):
    def __init__(self, age, *args):
        super(Father, self).__init__(*args)
        self.__age = age
        print('Father init...')

    def get_age(self):
        return self.__age


class Mother(Person):
    def __init__(self, job, *args):
        super(Mother, self).__init__(*args)
        self.__job = job
        print('Mother init...')

    def get_job(self):
        return self.__job


class Son(Father, Mother):
    def __init__(self, name, age, gender, job):
        # super(Son, self).__init__(age, job, name)
        super().__init__(name, age, job)
        self.__gender = gender
        print('Son init...')

    def get_gender(self):
        return self.__gender


s = Son('Tom', 18, '男', '老师')
print(s.get_name(), s.get_age(), s.get_gender(), s.get_job())

# class Person():
#     def __init__(self, name):
#         self.__name = name
#         print('Peron init...')
#
#     def get_name(self):
#         return self.__name
#
#
# class Mother(Person):
#     def __init__(self, name, job):
#         Person.__init__(self, name)
#         self.__job = job
#         print('Mother init...')
#
#     def get_job(self):
#         return self.__job
#
#
# class Father(Person):
#     def __init__(self, name, age):
#         Person.__init__(self, name)
#         self.__age = age
#         print('Father init...')
#
#     def get_age(self):
#         return self.__age
#
#
# class Son(Mother, Father):
#     def __init__(self, name, age, gender, job):
#         Mother.__init__(self, name, job)
#         Father.__init__(self, name, age)
#         self.__gender = gender
#         print('Son init...')
#
#     def get_gender(self):
#         return self.__gender
#
#
# s = Son('Tom', 18, '男', '老师')
# print(s.get_name(), s.get_age(), s.get_gender(), s.get_job())
