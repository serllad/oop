import abc
#声明一个类并指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    #定义抽象方法
    @abc.abstractmethod
    def smoking(clsself):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    #定义静态抽象类
    @abc.abstractstaticmethod
    def play():
        pass
