from enum import Enum

inp = []
x = y = 0

class Move_Y(Enum):
    down    = "down"
    up      = "up"

class Move_X(Enum):
    forward = "forward"


with open("input", "r") as f:
    for l in f.readlines():
        l = l.rsplit()
        inp.append([l[0], int(l[1])])


for i in inp:
    action, value  = i[0], i[1]
        #y -= value

    if action == Move_X.forward.value:
        x += value
    elif action == Move_Y.down.value:
        y += value
    elif action == Move_Y.up.value:
        y -= value


print("X = {}, Y = {}".format(x, y))
print("Product = {}".format(x * y))
