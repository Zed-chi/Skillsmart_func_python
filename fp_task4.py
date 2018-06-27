"""
fp_task4
just_nothing_list

"""

from pymonad import Just,List,Nothing, curry

@curry
def add(x, y):
    return x + y
@curry
def add10(x):
    return add()*Just(10)&x

print(add10(List(12,56,0,3)))
print(add10(Just(8)))
print(add10()(Nothing))