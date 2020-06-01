class TumblerModel:
    def __init__(self):
        self.__uniqueTumbler = [
            [ 'U', ' ', 'V', 'W', ' ' ],
            [ 'A', 'B', 'C', 'D', 'E' ],
            [ 'F', 'G', 'H', 'I', 'J' ],
            [ 'K', 'L', 'M', 'N', 'O' ],
            [ 'P', 'Q', 'R', 'S', 'T' ],
            [ 'X', ' ', 'X', 'X', ' ' ]
        ]

        self.__rows = len(self.__uniqueTumbler)
        self.__cols = len(self.__uniqueTumbler[0])

    def getBaseTumbler(self):
        return self.__uniqueTumbler

    def getRows(self):
        return self.__rows

    def getCols(self):
        return self.__cols
    
    def checkStatus(self, tumbler, mode, pieces):
        diffs = 0

        if mode == 'all':
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__uniqueTumbler[i][j] != tumbler[i][j]:
                        diffs += 1
                        if diffs > pieces:
                            return False
        elif mode == 'pins':
            for j in range(self.__cols):
                if self.__uniqueTumbler[0][j] != tumbler[0][j]:
                    diffs += 1
                    if diffs > pieces:
                        return False
        elif mode == 'top':
            for i in range(2):
                for j in range(self.__cols):
                    if self.__uniqueTumbler[i][j] != tumbler[i][j]:
                        diffs += 1
                        if diffs > pieces:
                            return False
        else:
            for j in range(self.__cols):
                if self.__uniqueTumbler[4][j] != tumbler[4][j]:
                    diffs += 1
                    if diffs > pieces:
                        return False

        return diffs > 0
