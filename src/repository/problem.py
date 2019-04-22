
class Problem:
    def __init__(self, size):
        self.__size = size
        self.__testBoard = []
        self.__positionMapping = {}

        self.initializeTestBoard()

    def initializeTestBoard(self):
        self.__testBoard.append([0 for _ in range(0, self.__size + 4)])
        self.__testBoard.append([0 for _ in range(0, self.__size + 4)])

        positionCounter = 1

        for i in range(2, self.__size + 2):
            self.__testBoard.append([])
            for j in range(0, self.__size + 4):
                if j < 2 or j > self.__size + 1:
                    self.__testBoard[i].append(0)
                else:
                    self.__testBoard[i].append(positionCounter)
                    self.__positionMapping[positionCounter] = {}
                    self.__positionMapping[positionCounter]['correspondingIndices'] = (i, j)

                    positionCounter += 1

        self.__testBoard.append([0 for _ in range(0, self.__size + 4)])
        self.__testBoard.append([0 for _ in range(0, self.__size + 4)])

        positionCounter = 1
        for i in range(2, self.__size + 2):
            for j in range(2, self.__size + 2):
                self.__positionMapping[positionCounter]['availablePositions'] = self.generateAvailableMoves((i, j))
                positionCounter += 1

        #Debug:
        #print(self.__positionMapping)
        #for i in range(0, self.__size + 4):
        #    print(self.__testBoard[i])

    def generateAvailableMoves(self, pos):
        """
            Generates a list of the available moves of a knight on a chess board
            given the current position of the knight.
        :param pos: tuple with 2 elements (pos[0] -> row index, pos[1] -> column index)
        :return: list containing the available moves as integers ranging from 1 to the size of the chess board squared.
        """
        availablePositions = []

        row = pos[0]
        col = pos[1]

        availablePositions.append(self.__testBoard[row - 2][col + 1])
        availablePositions.append(self.__testBoard[row - 1][col + 2])
        availablePositions.append(self.__testBoard[row + 1][col + 2])
        availablePositions.append(self.__testBoard[row + 2][col + 1])
        availablePositions.append(self.__testBoard[row + 2][col - 1])
        availablePositions.append(self.__testBoard[row + 1][col - 2])
        availablePositions.append(self.__testBoard[row - 1][col - 2])
        availablePositions.append(self.__testBoard[row - 2][col - 1])

        availablePositions = [p for p in filter(lambda x: not x == 0, availablePositions)]

        return availablePositions

    def getCorrespondingIndices(self, pos):
        return self.__positionMapping[pos]['correspondingIndices']

    def getAvailableMoves(self, pos):
        return self.__positionMapping[pos]['availablePositions']

    def getSize(self):
        return self.__size

    def getPositionMapping(self):
        return self.__positionMapping




