import random

from src.model.individual import Individual


class Population:
    def __init__(self, size):
        self.__size = size
        self.__individuals = []
        self.__lastSelectionPoint = 0

    def createPopulation(self, problem):

        for _ in range(0, self.__size):
            i = Individual()
            i.generateChromosomesRandomly()
            i.calculateFitness(problem)
            self.__individuals.append(i)

        #print(self.__individuals[0].getChromosomes())
        #print(self.__individuals[1].getChromosomes())
        #print(self.__individuals[0].crossover(self.__individuals[1], problem).getChromosomes())

    def getSize(self):
        return self.__size

    def getIndividuals(self):
        return self.__individuals

    def __getitem__(self, key):
        return self.__individuals[key]

    def __setitem__(self, key, value):
        self.__individuals[key] = value

    def selection(self):
        #self.__individuals.sort(key = lambda i: i.getFitnessValue(), reverse = True)
        self.__lastSelectionPoint = random.randint(0, int(len(self.__individuals) / 4))

        selectedIndices = random.choices(
            [i for i in range(0, len(self.__individuals))],
            [ind.getFitnessValue() for ind in self.__individuals],
            k = int(self.__size / 4)
        )

        selectedIndices = list(dict.fromkeys(selectedIndices))
        return selectedIndices

    def order(self):
        self.__individuals.sort(key=lambda i: i.getFitnessValue(), reverse=True)