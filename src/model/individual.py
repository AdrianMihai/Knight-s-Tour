from math import floor
from random import sample, randint, shuffle
from random import random

class Individual:

    initialPermutation = []

    def __init__(self):
        self.__chromosomes = []
        self.__fitnessValue = 0

    def getFitnessValue(self):
        return self.__fitnessValue

    def getChromosomes(self):
        return self.__chromosomes

    def setChromosomes(self, other):
        self.__chromosomes = other[:]

    def generateChromosomesRandomly(self):
        self.__chromosomes = sample(Individual.initialPermutation, len(Individual.initialPermutation))

    def calculateFitness(self, problem):
        f = 0

        #print(len(set(self.__chromosomes)))
        boardSize = problem.getSize()
        previousAvailableMoves = problem.getAvailableMoves(self.__chromosomes[0])
        #testSet = set()
        for i in range(1, boardSize * boardSize):

        #    if not self.__chromosomes[i] in testSet:
            if self.__chromosomes[i] in previousAvailableMoves:
                f += 1
        #        testSet.add(self.__chromosomes[i])

            previousAvailableMoves = problem.getAvailableMoves(self.__chromosomes[i])

        self.__fitnessValue = f

    def crossover(self, other, problem):
        boardSize = problem.getSize() * problem.getSize()
        firstCutPoint = randint(0, boardSize)
        secondCutPoint = randint(0, boardSize)

        while firstCutPoint == secondCutPoint:
            secondCutPoint = randint(0, boardSize)

        if secondCutPoint < firstCutPoint:
            firstCutPoint, secondCutPoint = secondCutPoint, firstCutPoint

        #print(firstCutPoint, secondCutPoint)

        offspring1 = Individual()
        offspring2 = Individual()

        offspring1.__chromosomes = [0 for _ in range(0, len(self.__chromosomes))]
        offspring2.__chromosomes = [0 for _ in range(0, len(self.__chromosomes))]

        for i in range(firstCutPoint, secondCutPoint):
            offspring1.__chromosomes[i] = self.__chromosomes[i]
            offspring2.__chromosomes[i] = other.__chromosomes[i]

        # create the first offspring
        currentParentPosition = secondCutPoint
        currentOffspringPosition = secondCutPoint

        while 0 in offspring1.__chromosomes:

            if currentOffspringPosition >= boardSize:
                currentOffspringPosition = 0

            if currentParentPosition >= boardSize:
                currentParentPosition = 0

            #print(other.__chromosomes[currentParentPosition] in offspring1.__chromosomes)
            if not other.__chromosomes[currentParentPosition] in offspring1.__chromosomes:
                offspring1.__chromosomes[currentOffspringPosition] = other.__chromosomes[currentParentPosition]
                #print(offspring1)
                currentOffspringPosition += 1
            currentParentPosition += 1

        # create the second offspring
        currentParentPosition = secondCutPoint
        currentOffspringPosition = secondCutPoint

        while 0 in offspring2.__chromosomes:

            if currentOffspringPosition >= boardSize:
                currentOffspringPosition = 0

            if currentParentPosition >= boardSize:
                currentParentPosition = 0

            #print(other.__chromosomes[currentParentPosition] in offspring1.__chromosomes)
            if not self.__chromosomes[currentParentPosition] in offspring2.__chromosomes:
                offspring2.__chromosomes[currentOffspringPosition] = self.__chromosomes[currentParentPosition]
                currentOffspringPosition += 1
            currentParentPosition += 1

        #print(offspring1)
        offspring1.calculateFitness(problem)
        offspring2.calculateFitness(problem)

        return [offspring1, offspring2]

    def mutate(self, mutationProbability):
        if random() < mutationProbability:
            newIndividual = Individual()
            i1 = randint(0, len(self.__chromosomes) - 1)
            i2 = randint(0, len(self.__chromosomes) - 1)

            while i1 == i2:
                i2 = randint(0, len(self.__chromosomes) - 1)

            if i1 > i2:
                i1, i2 = i2, i1

            newChromosomes = self.__chromosomes[:]
            geneSelection = self.__chromosomes[i1:i2 + 1]
            geneSelection.reverse()

            #print("Mutated")
            #print(newChromosomes)
            for i in range(i1, i2 + 1):
                newChromosomes[i] = geneSelection[i - i1]

            #print(newChromosomes)
            shuffle(newChromosomes)
            newIndividual.setChromosomes(newChromosomes)

            return newIndividual
        return self

    def __str__(self):
        return str(self.__chromosomes)