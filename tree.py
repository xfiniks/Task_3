from enum import Enum
from extender import *
from rnd import generate_random_string
from rnd import generate_random_int


class Tree:
    def __init__(self):
        self.name = ""
        self.year = 0

    def read_str_array(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.name = str(strArray[i])
        self.year = (strArray[i + 1])
        i += 2
        return i

    def print(self):
        print("Tree: name = ", self.name, "year = ", self.year,
              "task = ", self.task())

    def write(self, ostream):
        ostream.write("Tree: name = {}, year = {}, task = {}".
                      format(self.name, self.year, self.task()))

    def random_print(self):
        self.name = generate_random_string(15)
        self.year = generate_random_int(1,2000)
        print("Tree: name = ", self.name, "year = ", self.year,
              "task = ", self.task())

    def random_write(self, ostream):
        ostream.write("Tree: name = {}, year = {}, task = {}".
                      format(self.name, self.year, self.task()))

    def task(self):
        e_count = self.name.count('e')
        y_count = self.name.count('y')
        u_count = self.name.count('u')
        i_count = self.name.count('i')
        o_count = self.name.count('o')
        a_count = self.name.count('a')

        return (e_count + y_count + u_count + i_count + o_count + a_count) / len(self.name)
