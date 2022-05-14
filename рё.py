
menu = {'pizza1':'100',
        'pizza2':'200'}

def add_pizza(name,price):
    if name in menu.keys():
        print('already there is')
    else:
        menu[name] = price
print('before')
print(menu)
add_pizza('pizza3',100)
print('after')
print(menu)


def remove_pizza(name):
    if name in menu.keys()
        print('delete')
        del menu[name]
    else:
        print('no pizza')


def order(name, price)
        if name in menu.keys()
            print('pizza is accepted')
            p

