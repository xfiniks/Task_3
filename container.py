import random

from extender import *
from shrub import Shrub


class Container:
    __length = 0

    def __init__(self):
        self.storage = []

    def print(self):
        print("Container is store", len(self.storage), "plants:")
        for plants in self.storage:
            plants.print()
            self.__length = self.__length + 1
        print("Shell Sorting  = ", )

    def write(self, ostream):
        ostream.write("Container is store {} plants:\n".format(len(self.storage)))
        for plants in self.storage:
            plants.write(ostream)
            ostream.write("\n")
        self.shell()

    def shell_print(self):
        for plants in self.storage:
            plants.print()

    def shell_write(self, ostream):
        ostream.write("Sorted {} plants:\n".format(len(self.storage)))
        for plants in self.storage:
            plants.write(ostream)
            ostream.write("\n")

    def random_print(self, count):
        for i in range(int(count)):
            random_1 = random.randint(1, 3)
            random_2 = random.randint(1, 12)
            digit = random.randint(1, 3)
            if digit == 1:
                tree = Tree()
                tree.random_print()
                self.storage.append(tree)
            elif digit == 2:
                shrub = Shrub()
                shrub.random_print(random_2)
                self.storage.append(shrub)
            elif digit == 3:
                flower = Flower()
                flower.random_print(random_1)
                self.storage.append(flower)
            self.__length = self.__length + 1

    def random_write(self, ostream):
        ostream.write("Container is store {} plants:\n".format(len(self.storage)))
        for plants in self.storage:
            plants.random_write(ostream)
            ostream.write("\n")
        self.shell()

    def shell_random_print(self):
        print("\n")
        print("\n")
        for plants in self.storage:
            plants.random_print()

    def shell_random_write(self, ostream):
        ostream.write("Sorted {} plants:\n".format(len(self.storage)))
        self.shell()
        for plants in self.storage:
            plants.write(ostream)
            ostream.write("\n")

    def shell(self):
        length = len(self.storage)
        s = length // 2
        while s > 0:
            for i in range(length):
                for j in range(i + s, length, s):
                    if self.storage[i].task() > self.storage[j].task():
                        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
            s //= 2
