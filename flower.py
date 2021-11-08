from enum import Enum
from extender import *
from rnd import generate_random_string


class Flower:
    def __init__(self):
        self.name = ""
        self.type = Enum("type", "Domestic Wild Garden", start=1)

    def read_str_array(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.name = str(strArray[i])
        self.type = (strArray[i + 1])
        i += 2
        return i

    def print(self):
        print("Flower: name = ", self.name, "type = ", self.type,
              "task = ", self.task())

    def write(self, ostream):
        ostream.write("Flower: name = {}, type = {}, task = {}".
                      format(self.name, self.type, self.task()))

    def random_print(self, types):
        if types == 1:
            self.type = "Domestic"
        elif types == 2:
            self.type = "Wild"
        else:
            self.type = "Garden"

        self.name = generate_random_string(15)

        print("Flower: name = ", self.name, "type = ", self.type,
              "task = ", self.task())

    def random_write(self, ostream):
        ostream.write("Flower: name = {}, type = {}, task = {}".
                      format(self.name, self.type, self.task()))

    def task(self):
        e = self.name.count('e')
        y = self.name.count('y')
        u = self.name.count('u')
        i = self.name.count('i')
        o = self.name.count('o')
        a = self.name.count('a')

        return (e + y + u + i + o + a) / len(self.name)
