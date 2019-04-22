from src.controller.algorithm import Algorithm
from src.tests.tests import runTests
from src.view.app import App
import numpy as np
import matplotlib.pyplot as plt

runTests()

algorithm = Algorithm("param.in")
algorithm.readParameters()
app = App(algorithm)
app.run()


