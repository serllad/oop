from sys import getrefcount
a=[1,2,3]
print(getrefcount(a))

b = a
print(getrefcount(b))
b.append(4)
print(a)
#__class__为当前类
class Person:
    name="None"
    pass
class student(Person):
    name="lele"
    __age=16
    def set(self,name,age):#self不是关键字，可任意替换
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
    def prt(self):#不带self的函数只能通过类名来访问，为绑定类函数
        print(super().name)

s=student()
s.set("lala",17)
student.prt(s)