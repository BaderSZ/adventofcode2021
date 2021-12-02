from enum import Enum

inp = []
x = y = aim = 0

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
    action, value = i[0], i[1]

    if action == Move_X.forward.value:
        y += value*aim
        x += value
    elif action == Move_Y.down.value:
        aim += value
    elif action == Move_Y.up.value:
        aim -= value


print("X = {}, Y = {}, Aim = {}".format(x, y, aim))
print("Product = {}".format(x * y))
