"""
fp_task3
currying
pymonad module
"""

from pymonad import curry


###Версия попроще
@curry
def tag_1(tag, value):
    return "<{}>{}</{}>".format(tag,value,tag)

@curry
def tag_2(tag,attr,value):
    at = ""
    for k in attr:
        at+=" {}='{}'".format(k,attr[k])
    return "<{}{}>{}</{}>".format(tag,at,value,tag)


bold = tag_1("b")
italic = tag_1("i")
li = tag_2('li', {'class': 'list-group'}, 'item 23')
##print(bold("The bold text"))
##print(italic("The italic text"))
##print(li)


###Версия посложнее
@curry
def tag(t):
    return t

@curry
def attr(t,a):
    return [t,a]

@curry
def val(arr,v):
    s = ""
    for i in arr[1]:
        s+="{}='{}'".format(i, arr[1][i])
    return "<{} {}>{}</{}>".format(arr[0],s,v,arr[0])

@curry
def wrap(x,y,z):
    return val(attr(tag(x),y),z)

print(wrap("div")({"class":"jumbotron"})("Text"))