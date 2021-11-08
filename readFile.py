import tree
import shrub
import flower
from extender import *


def read_str_array(container, strArray):
    array_len = len(strArray)
    i = 0
    plantNum = 0
    while i < array_len:
        str = strArray[i]
        key = int(str)
        if key == 1:
            i += 1
            plant = tree.Tree()
            i = plant.read_str_array(strArray, i)
        elif key == 2:
            i += 1
            plant = shrub.Shrub()
            i = plant.read_str_array(strArray, i)
        elif key == 3:
            i += 1
            plant = flower.Flower()
            i = plant.read_str_array(strArray, i)
        else:
            return plantNum

        if i == 0:
            return plantNum
        plantNum += 1
        container.storage.append(plant)
    return plantNum
