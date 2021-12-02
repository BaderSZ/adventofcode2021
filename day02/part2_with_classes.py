from enum import Enum
from typing import List, Union

inp = []

class MoveY(Enum):
    down    = "down"
    up      = "up"

class MoveX(Enum):
    forward = "forward"

class Submarine():
    def __init__(self, aim: int = 0, x: int = 0, y: int = 0):
        self.aim= 0
        self.x = 0
        self.y = 0

    def move_x(self, i: int) -> None:
        self.y += i*self.aim
        self.x += i

    def move_y_down(self, i: int) -> None:
        self.aim += i

    def move_y_up(self, i: int) -> None:
        self.aim -= i

    def parse(self, arr: List[List[Union[int, str]]]) -> None:
        for i in arr:
            action, value = i[0], i[1]

            if action == MoveX.forward.value:
                self.move_x(value)
            elif action == MoveY.down.value:
                self.move_y_down(value)
            elif action == MoveY.up.value:
                self.move_y_up(value)

    def print(self) -> None:
        print("x = {}, y = {}".format(self.x, self.y))
        print("aim = {}".format(self.aim))
        print("product = {}".format(self.x*self.y))


with open("input", "r") as f:
    for l in f.readlines():
        l = l.rsplit()
        inp.append([l[0], int(l[1])])


sub = Submarine()
sub.parse(inp)
sub.print()
