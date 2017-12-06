# class  Dog:
#     kind='canice'
#     def __init__(self,name):
#         self.name=name
#
# d=Dog('xiao')
# e=Dog('da')
# print(d.kind+':',d.name)
# print(e.kind+':',e.name)



#
# class dog001:
#     tricks = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d = dog001('xiao')
# e=dog001('da')
# e.add_trick('123')
# d.add_trick('asfaf')
# print(d.tricks)
# print(e.tricks)
# class dog002:
#
#     def __init__(self,name):
#         self.name=name
#         self.tricks = []
#     def add_trick(self,trick):
#         self.tricks.append(trick)
# d=dog002('xiao')
# e=dog002('da')
# d.add_trick('asfaf')
# e.add_trick('123')
# print(d.tricks)
# print(e.tricks)
# str = input("请输入：");
# print (str)
#
# class myclass:
#     i=5
#     def f(self):
#         return 'hello'
#     def z(self):
#         z=8
#         return z
# x=myclass()
# print(x.i)
# print(x.f())
# print(x.f)
# print(x.z())
#
# class test:
#     def prt(s):
#         print(s)
#         print(s.__class__)
# t=test()
# t.prt()

# class people:
#     name=''
#     age=0
#     __weight=0
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def speak(self):
#         print(self.name,self.age,self.__weight)
# p=people('wang',10,32)
# p.speak()
# class student(people):
#     grade=''
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade=g
#         self.__weight=0
#     def speak(self):
#         print(self.name,self.age,self.__weight,self.grade)
# s=student('ken',10,60,3)
# s.speak()
# import keyword
# print (keyword.kwlist)
# class people:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)
# a=people('xiaorenw',14)
# print(a)
#类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#
# #单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
#
# #另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
#
# #多重继承
# class sample(speaker,student):
#     a =''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
#
# test = sample("Tim",25,80,4,"Python")
# test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
a='iamsafsamafasf'
print(a.split('am'))
print(a.split('am',1))
print(a.split('am',2))
def count(s):
    s=s.replace(",","").replace('!','')
    b=s.split()
    return b
s='i am a boy , and safsa!!!!'
print (count(s))