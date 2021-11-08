from enum import Enum
from extender import *

class Shrub:
    def __init__(self):
        self.name = ""
        self.type = Enum("type", "January February March April May June July August September October November December", start=1)

    def read_str_array(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.name = str(strArray[i])
        self.type = (strArray[i + 1])
        i += 2
        return i

    def print(self):
        print("Shrub: name = ", self.name, "type = ", self.type,
              "task = ", self.task())

    def write(self, ostream):
        ostream.write("Shrub: name = {}, type = {}, task = {}".
                      format(self.name, self.type, self.task()))

    def random_print(self, types):
        if types == 1:
            self.type = "January"
        elif types == 2:
            self.type = "February"
        elif types == 3:
            self.type = "March"
        elif types == 4:
            self.type = "April"
        elif types == 5:
            self.type = "May"
        elif types == 6:
            self.type = "June"
        elif types == 7:
            self.type = "July"
        elif types == 8:
            self.type = "August"
        elif types == 9:
            self.type = "September"
        elif types == 10:
            self.type = "October"
        elif types == 11:
            self.type = "November"
        elif types == 12:
            self.type = "December"

        self.name = generate_random_string(15)

        print("Shrub: name = ", self.name, "type = ", self.type,
              "task = ", self.task())

    def random_write(self, ostream):
        ostream.write("Shrub: name = {}, type = {}, task = {}".
                      format(self.name, self.type, self.task()))

    def task(self):
        e = self.name.count('e')
        y = self.name.count('y')
        u = self.name.count('u')
        i = self.name.count('i')
        o = self.name.count('o')
        a = self.name.count('a')

        return (e + y + u + i + o + a) / len(self.name)
