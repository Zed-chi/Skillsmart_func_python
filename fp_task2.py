"""
Currying, Partial Task
note:there's a functools module
"""

def curry_conc(a=None, b=None):
    if a and b:
        return a+b
    if a and not b:
        return lambda x:a+x

hello = curry_conc("Hello")
b = " world"
print(hello(b))


def partial(word=None, x=None, y = None,name=None):
    if word and x and name and y:
        return word+x+name+y
    elif word and x and y:
        return lambda name: word+x+name+y
    elif word and x:
        return lambda y: partial(word,x,y)
    elif word:
        return lambda x :partial(word,x)
    else:
        return lambda word:partial(word)

final = partial("Hello")(",")("!")
print(final("Petya"))
