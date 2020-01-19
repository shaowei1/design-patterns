def overrides(interface_class):
    def overrider(method):
        assert (method.__name__ in dir(interface_class))
        return method

    return overrider


class MySuperInterface(object):
    roles = 'cosplayer'

    def my_method(self):
        print('hello world!')


class ConcreteImplementer(MySuperInterface):
    @overrides(MySuperInterface)
    def my_method(self):
        print('hello kitty!')


# class ConcreteFaultyImplementer(MySuperInterface):
#     @overrides(MySuperInterface)
#     def your_method(self):
#         print('bye bye!')


my = ConcreteImplementer()
my.my_method()
print(my.roles)
