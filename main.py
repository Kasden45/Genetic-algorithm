import copy
import pickle

import numpy as np

from Populations import Population
from Fitness import Fitness
from Generator import RandomIndividualGenerator
from Individual import Individual
from PCB_Board import PCB_Board
from Pair import Pair
from Point import Point
from Problem import Problem
from Segment import Segment
from Tester import Tester, txt_to_csv
from Trace import Trace
import cProfile
import pstats

if __name__ == '__main__':
    """
    Initializing boards and reading data
    """
    board0 = PCB_Board()
    board0.read_board("zad0.txt")
    print("Board_0", board0)

    board1 = PCB_Board()
    board1.read_board("zad1.txt")
    print("Board_1", board1)

    board2 = PCB_Board()
    board2.read_board("zad2.txt")
    print("Board_2", board2)

    board3 = PCB_Board()
    board3.read_board("zad3.txt")
    print("Board_3", board3)

    """
    Testing problem solving
    """
    problem = Problem()
    result = problem.solve_problem()

    result[0][0].plot_segments("Best solution overall", result[1])

    """
    Testing different coefficients
    """
    tester = Tester(["zad1.txt", "zad2.txt", "zad3.txt"])
    # tester = Tester(["zad0.txt"])
    tester.set_iterations(10, 40, 5)
    tester.set_population_size(10, 90, 10)
    tester.set_cross_prob(0.3, 0.7, 0.1)
    tester.set_mutation_prob(0.2, 0.8, 0.6)
    tester.set_tournament_size(0.40, 0.70, 0.05)

    tester.default["pop_size"] = 50
    print("Testing SELECTIONS")
    tester.do_testing_selection("selection")
    print("Testing ITERATIONS")
    tester.do_testing_iterations("iteration")
    print("Testing PMS")
    tester.do_testing_pm("pms")
    print("Testing PXS")
    tester.do_testing_px("pxs")
    print("Testing POPULATIONS")
    tester.do_testing_populations("population")

    tester.do_testing_random("Random_200_10_10")

    # Saving to csv format
    txt_to_csv("pms", "pms_csv")
    txt_to_csv("iteration", "iteration_csv")
    txt_to_csv("population", "population_csv")
    txt_to_csv("selection", "selection_csv")