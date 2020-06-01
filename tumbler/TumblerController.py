from TumblerModel import TumblerModel
from copy import deepcopy

class TumblerController:
    def __init__(self):
        tumblerModel = TumblerModel()
        self.__rows = tumblerModel.getRows()
        self.__columns = tumblerModel.getCols()

    def raiseTumbler(self, prevTumbler):
        tumbler = deepcopy(prevTumbler)
        for i in range(1, self.__rows):
            tumbler[i - 1][1] = tumbler[i][1]
            tumbler[i - 1][4] = tumbler[i][4]
        return tumbler

    def lowerTumbler(self, prevTumbler):
        tumbler = deepcopy(prevTumbler)
        for i in range(self.__rows - 2, -1, -1):
            tumbler[i + 1][1] = tumbler[i][1]
            tumbler[i + 1][4] = tumbler[i][4]
        tumbler[0][1] = ' '
        tumbler[0][4] = ' '
        return tumbler

    def rotateLeft(self, prevTumbler, upper, raised):
        tumbler = deepcopy(prevTumbler)
        row = 1 if upper else 3
        row -= 1 if raised else 0
        preserve1 = tumbler[row].pop(0)
        preserve2 = tumbler[row+1].pop(0)
        tumbler[row].append(preserve1)
        tumbler[row+1].append(preserve2)
        return tumbler

    def rotateRight(self, prevTumbler, upper, raised):
        tumbler = deepcopy(prevTumbler)
        row = 1 if upper else 3
        row -= 1 if raised else 0
        preserve1 = tumbler[row].pop(self.__columns-1)
        preserve2 = tumbler[row+1].pop(self.__columns-1)
        tumbler[row] = [preserve1] + tumbler[row]
        tumbler[row+1] = [preserve2] + tumbler[row+1]
        return tumbler
