import random
from src.model.individual import Individual
from src.repository.problem import Problem

def inidividualTest():
    print("Running tests for individual. \n")
    i2 = Individual()

    initialPermutation = [random.randint(1, 64) for _ in range(0, 64)]
    Individual.initialPermutation = initialPermutation

    #print("Initial permutation: \n" + str(Individual.initialPermutation))

    i2.generateChromosomesRandomly()
    assert len(i2.getChromosomes()) == len(Individual.initialPermutation)

def problemTest():
    print("Running tests for problem. \n")
    boardSize = 8
    p1 = Problem(boardSize)

    i1 = Individual()
    initialPermutation = [random.randint(1, boardSize * boardSize) for _ in range(0, boardSize * boardSize)]
    Individual.initialPermutation = initialPermutation
    i1.generateChromosomesRandomly()
    i1.calculateFitness(p1)

    #print(i1.getFitnessValue())
    #print(i1.getChromosomes())
    #print(i1)
    #print(i1.mutate(1))
    #print(p1.generateAvailableMoves((6, 4)))
    assert p1.generateAvailableMoves((2, 2)) == [11, 18]
    assert p1.generateAvailableMoves((6, 4)) == [20, 29, 45, 52, 50, 41, 25, 18]

def runTests():
    inidividualTest()
    problemTest()