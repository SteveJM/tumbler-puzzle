from TumblerModel import TumblerModel

tumblerModel = TumblerModel()

class TumblerView():
    def __init__(self):
        self.__rows = tumblerModel.getRows()
        self.__columns = tumblerModel.getCols()
        self.__base = tumblerModel.getBaseTumbler()

    def printDelta(self, tumbler, mode):
            for i in range(self.__rows):
                if mode == 'all' \
                   or (mode == 'pins' and i < 1) \
                   or (mode == 'top' and i < 2) \
                   or (mode == 'bottom' and i == 4):
                    print(self.__base[i], "   ", tumbler[i])
                else:
                    print(self.__base[i], "    ['*', '*', '*', '*', '*']")
