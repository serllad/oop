class Fib(object):
    def __init__(self,max):
        super().__init__()
        self.max=max
    def __iter__(self):
        self.a=0
        self.b=1
        return self
    def __next__(self):
        fib=self.b
        if fib>self.max:
            raise StopIteration
        self.a,self.b=self.b,self.a+self.b
        return fib
def main():
    fib=Fib(100)
    for i in fib:
        print(i)
if __name__=='__main__':
    main()
'''
在本类的实现中，定义了一个_iter_(self)方法，这个方法是在for循环遍历时被iter()调用，返回一个迭代器。
因为在遍历的时候，是直接调用的python内置函数iter()，由iter()通过调用_iter_(self)获得对象的迭代器。
有了迭代器，就可以逐个遍历元素了。
而逐个遍历的时候，也是使用内置的next(）函数通过调用对象的_next_(self)方法对迭代器对象进行遍历。
所以要实现_iter_(self)和_next_(self)这两个方法。
而且因为实现了_next_(self)方法，所以在实现_iter_(self)的时候，直接返回self就可以。

总结一句话就是：
在循环遍历自定义容器对象时,会使用python内置函数iter()调用遍历对象的_iter_(self)获得一个迭代器,之后再循环对这个迭代器使用next()调用迭代器对象的_next_(self)。

注意点：_iter_(self)只会被调用一次,而_next_(self)会被调用 n 次，直到出现StopIteration异常。
可迭代对象和迭代器的区别
    可迭代对象是可以用for循环遍历的，有__iter__()方法，但是不能通过python内置方法next()访问，list,dict,set,tuple,str等都是可迭代对象
    迭代器对象必须有__iter__(),__next__()方法，可以通过obj.next得到下一个元素，list等类型不属于迭代器，因为没__next__()方法，
可通过iter(可迭代的)来获得一个可迭代对象
迭代器和生成器的区别
    生成器是迭代器的子类，可以节省内存空间，通过yield来生成值
生成器和协程
    x=yeild y
    协程对象可以调用send()方法来进行通信
'''
