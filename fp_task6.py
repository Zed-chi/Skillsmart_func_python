"""
State Monad

Пример с покупками
    есть:
    - условный человек = {корзина, счет}
    - перечень продуктов = []
    - условный результат покупок (человек, кол.покупок)
"""

from pymonad import curry, State, unit

@curry
def buy(what, to):
    @State
    def state_computation(old_state):
        if what in items and to["money"]-items[what]>0:
            to["items"].append(what)
            to["money"]-=items[what]
            return (to, old_state + 1)
        else:
            return (to,old_state)
    return state_computation



items = {"apples":70,
         "wine":300,
         "milk":80,
         "chips":100
}

user = {"items":[],"money":2000}

shoping = unit(State, user) >> buy("apples") >> buy("wine") >> buy("chips") >> buy("dasda")

print("Вы купили {0[1]} товар(а) - {0[0][items]}, у вас осталось {0[0][money]} монет"
      .format(shoping(0)))

