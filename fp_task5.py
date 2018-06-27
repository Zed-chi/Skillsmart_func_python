"""
fp_task5

"""
from pymonad import List, Just, Nothing, Maybe

# посадка птиц на левую сторону
to_left = lambda num: lambda x: Nothing if abs((x[0] + num) - x[1]) > 4 else Just((x[0] + num, x[1]))

# посадка птиц на правую сторону
to_right = lambda num: lambda x: Nothing if abs((x[1] + num) - x[0]) > 4 else Just((x[0], x[1] + num))

# банановая кожура
banana = lambda x: Nothing

# отображение результата
def show(Maybe):
    if Maybe == Nothing:
        return print("Will Fall")
    else:
        falled, pole = Maybe.getValue()
        return print("Will not Fall, birds on l.side:{}, birds on r.side:{}".format(falled,pole))

begin = lambda: Just((0,0))

show(begin()>>to_left(2)>>to_right(5)>>to_left(-2))
show(begin()>>to_left(2)>>to_right(5)>>to_left(-1))
show(begin()>>to_left(2)>>banana>>to_right(5)>>to_left(-1))
