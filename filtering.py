#filter function
a = ['my', 'name', 'is', 'vera']
sub = list(filter(lambda x:x.lower().startswith('v'), a))
print(sub)
endstring =list(filter(lambda x: x.lower().endswith('e'),a))
print(endstring)
#map function
values =[1,2,3,4,5,6,7]
a= list(map(lambda x:x*2,values))
print(a)
#reduce
from functools import reduce
b =reduce(lambda x,y:x*y,values)
print(b)
def sum(a,b):
    print(f'a={a},b={b},{a}+{b}={a+b}')
    return a+b
reduce(sum,values)
#Generators
#yield
def gen():
    n=1
    print('First yield')
    yield n
    n+=1
    print('Second yield')
    yield n
    n+=1
    print('Third yield')
    yield n
a= gen()
next(a)
next(a)
next(a)
#next(a)💀