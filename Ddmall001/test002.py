class myclass:
    """"a ahsghaio"""
    i=123123
    def f(self):
        return 'hello'

class a:
    def __init__(self,b,c):
        self.r=b
        self.i=c
x=a(3.0,-4.5)
print(x.i+x.r)
x.counter=1
while x.counter<10:
    x.counter=x.counter*2
print(x.counter)
del x.counter
z=myclass()
zf=z.f
while true:
    print(zf())