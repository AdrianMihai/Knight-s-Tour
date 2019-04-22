from random import randint

from matplotlib import animation

from src.repository.problem import Problem
from src.repository.population import Population
from src.model.individual import Individual
import matplotlib.pyplot as plt
class Algorithm:
    def __init__(self, inputFile, population = None, problem = None, noIterations = None, pM = None ):
        self.__inputFile = inputFile
        self.__population = population
        self.__problem = problem
        self.__noIterations = noIterations
        self.__pM = pM

    def readParameters(self):

        with open("../src/inputData/" + self.__inputFile, "r") as file:
            lines = [line[:len(line) - 1] for line in file.readlines()]
            self.__problem = Problem(int(lines[0]))
            self.__pM = float(lines[1])
            self.__population = Population(int(lines[2]))
            self.__noIterations = int(lines[3])

        self.__generateInitialPermutation()
        self.__population.createPopulation(self.__problem)

    def __generateInitialPermutation(self):
        boardSize = self.__problem.getSize() * self.__problem.getSize()
        Individual.initialPermutation = []

        while len(Individual.initialPermutation) < boardSize:
            gene = randint(1, boardSize)
            if not gene in Individual.initialPermutation:
                Individual.initialPermutation.append(gene)

    def getMutationProbability(self):
        return self.__pM

    def operator(self, i1, i2):
        p1 = self.__population[i1]
        p2 = self.__population[i2]

        offsprings = p1.crossover(p2, self.__problem)
        offsprings[0] = offsprings[0].mutate(self.__pM)
        offsprings[1] = offsprings[1].mutate(self.__pM)

        f1 = p1.getFitnessValue()
        f2 = p2.getFitnessValue()
        of1 = offsprings[0].getFitnessValue()
        of2 = offsprings[1].getFitnessValue()


        if of1 > f1 and f2 > f1:
            self.__population[i1] = offsprings[0]

        if of2 > f2 and f1 > f2:
            self.__population[i2] = offsprings[1]

    def __iteration(self):
        selectedIndices = self.__population.selection()

        for i in range(0, len(selectedIndices), 2):
            try:
                self.operator(selectedIndices[i], selectedIndices[i + 1])
            except IndexError:
                pass

        self.__population.order()

    def runIterations(self):

        self.__population.order()
        bestIndividuals = []

        #while not self.__population[0].getFitnessValue() == (self.__problem.getSize() * self.__problem.getSize() - 1):
        for i in range(self.__noIterations):
            print("Best individual: " + str(self.__population[0].getFitnessValue()))
            bestIndividuals.append(self.__population[0].getFitnessValue())
            self.__iteration()

        self.__statistics(bestIndividuals)
        results = sorted(self.__population.getIndividuals(), key = lambda i: i.getFitnessValue(), reverse = True)
        return results

    def __statistics(self, bestIndividuals):
        #individuals = []
        #fitnessValues = []

        #for i in range(0, self.__population.getSize()):
        #    individuals.append(i)
        #    fitnessValues.append(self.__population[i].getFitnessValue())

        iterationCounter = [i for i in range(self.__noIterations)]
        plt.ion()
        #plt.xlim(0, self.__population.getSize() - 1)
        #plt.ylim(0, (self.__problem.getSize() * self.__problem.getSize()) - 1)

        line = plt.plot(iterationCounter, bestIndividuals)[0]
        plt.show()
        plt.ioff()
        #fig.canvas.draw()
        #fig.canvas.flush_events()
