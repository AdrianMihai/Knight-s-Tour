class App:
    def __init__(self, algorithm):
        self.__algorithm = algorithm

    def run(self):
        results = self.__algorithm.runIterations()

        print("Best individual: \n")
        print(results[0].getFitnessValue())
        print(results[0].getChromosomes())