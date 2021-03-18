import copy

from Populations import Population
from Fitness import Fitness
from Generator import RandomIndividualGenerator
from Individual import Individual
from PCB_Board import PCB_Board
from Pair import Pair
from Point import Point
from Problem import Problem
from Segment import Segment
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
    Testing segments
    """
    # s1 = Segment(Point(1, 5), Point(1, 9))
    # print(s1, "s1 Length:", len(s1))
    # # print(s1.middle_points())
    #
    # s2 = Segment(Point(4, 5), Point(1, 5))
    # print(s2, "s2 Length:", len(s2))
    #
    # s3 = Segment(Point(2, 3), Point(4, 3))
    #
    # s4 = Segment(Point(3, 1), Point(3, 5))
    #
    # print(s3, "s3 Length:", len(s3))
    # print(s4, "s4 Length:", len(s4))
    # print(s1.collisions(s2))
    # print(s2.collisions(s1))
    # print(s1.collisions(s3))
    # print(s2.collisions(s3))
    #
    # """
    #     Testing traces
    # """
    # t1 = Trace(Pair(Point(4, 5), Point(1, 9)), [s2, s1])
    #
    # t2 = Trace(Pair(Point(4, 5), Point(1, 9)), [s3])
    #
    # t3 = Trace(Pair(Point(4, 5), Point(1, 9)), [s4])
    # print(t1.print_trace_route())
    # """
    #     Testing individuals and fitness function
    # """
    # i1 = Individual(board0, [t1, t2])
    #
    # f1 = Fitness(10, 5, 3)
    # print("Collisions ", f1.collisions(i1))
    # print("Length ", f1.total_length(i1))
    # print("Segments ", f1.total_segments(i1))
    # # print("Out of bounds", f1.out_of_bounds(i1))
    # # print("Length out of bounds", f1.length_out_of_bounds(i1))
    #
    # print("t2 last\n", t2.last_point())
    # print("i1\n", str(i1))
    #
    # print("t1\n", str(t1))
    # t1.extend_last_segment(Point(1, 12))
    # print("t1\n", str(t1))
    # """
    # Generator test
    # """
    # rg = RandomIndividualGenerator(board0)

    """
    Actual population test
    """
    print("********************************* TEST **************************************")

    # lines = [[(0, 1), (1, 1)], [(2, 3), (8, 3)], [(1, 2), (1, 5)]]
    #
    #
    #
    # fig, ax = pl.subplots()
    # ax.add_collection(lc)
    # ax.autoscale()
    # ax.margins(0.1)
    # pl.grid()
    #
    # cir = pl.Circle((1, 2), 0.07, color=color, fill=True)
    # ax.add_patch(cir)
    # pl.show()

    # pop = Population()
    # pop.set_fitness(1000, 25, 2, 2000, 1000)
    #
    # profile = cProfile.Profile()
    # profile.runcall(lambda: pop.generate_population(board0, 50))
    # ps = pstats.Stats(profile)
    # ps.print_stats()

    #
    # pop.grade_population()
    # print(pop.best_individual())
    #
    #
    #
    # pop.best_individual().plot_segments()
    # #
    #
    #
    # print(pop.tournament_operator(5))
    # print(pop.roulette_operator())
    # print(pop.tournament_operator(8))


    problem = Problem()
    profile_problem = cProfile.Profile()
    profile_problem.runcall(lambda: problem.solve_problem())
    ps = pstats.Stats(profile_problem)
    ps.print_stats()

    s3 = Segment(Point(2, 3), Point(4, 3))

    s4 = Segment(Point(3, 1), Point(3, 5))

    tablica = [s3, s4]

