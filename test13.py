import copy

c=[1,2]

def f2(d):
    e=d
    e.append(3)
    print('function d=', d)
    print('function e=', e)

def f3(d):
    e=copy.deepcopy(d)
    e.append(3)
    print('function d=', d)
    print('function e=', e)

f3(c)
print('original c=', c)


print('-----------------------------------')

aa=[1,2,3]

cc=copy.deepcopy(aa)
bb=cc
bb.append(5)

print('aa=',aa)
print('bb=',bb)
print('cc=',cc)

s0='123'
s1=s0
s2=copy.deepcopy(s0)
s1=s1+'456'
print(s0,s1,s2)

