class cls1:
    b=18
    def __init__(self,x,y):

        self.x = x
        self.y = y
    def f1(self):
        z = self.x+self.y
        return z
    def f2(self):
        return self.b
a=2
ci1=cls1(a,3)
# a=ci1.f1()
print(a)
z=32
ci1.x=10
# ci1.b=20
cmd="cls1.b="+str(ci1.b) +'   cls1.x='+str(ci1.x)
print(cmd)
print(str(ci1.f1()))
