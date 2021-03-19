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

    # pop.generate_population(board0, 1000)
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

    # print(pop.best_individual())

    """
    TESTOWANIE PROBLEMU
    """
    problem = Problem()
    result = problem.solve_problem()
    result[0][0].plot_segments("Best solution overall", result[1])

    """
        TESTOWANIE OPERATORÓW
    """
    def generate_trace(lista):
        points = []
        for pair in lista:
            points.append(Point(pair[0], pair[1]))
        segments = []
        for i in range(len(points) - 1):
            segments.append(Segment(points[i], points[i + 1]))
        trace = Trace(Pair(points[0], points[-1]))
        for segment in segments:
            trace.add_segment(segment)
        return trace
    # 1. (1,3) -> (5,3)
    # 2. (3,1) -> (3,3)

    i1 = Individual(board0)
    i2 = Individual(board0)
    i3 = Individual(board0)
    i4 = Individual(board0)
    i5 = Individual(board0)

    t1_1 = Trace(Pair(Point(1, 3), Point(5, 3)))
    t1_2 = Trace(Pair(Point(3, 1), Point(3, 3)))

    s1 = Segment(Point(1, 3), Point(1, 4))
    s2 = Segment(Point(1, 4), Point(4, 4))
    s3 = Segment(Point(4, 4), Point(4, 5))
    s4 = Segment(Point(4, 5), Point(5, 5))
    s5 = Segment(Point(5, 5), Point(5, 3))

    t1_1.add_segment(s1)
    t1_1.add_segment(s2)
    t1_1.add_segment(s3)
    t1_1.add_segment(s4)
    t1_1.add_segment(s5)

    s6 = Segment(Point(3, 1), Point(4, 1))
    s7 = Segment(Point(4, 1), Point(4, 3))
    s8 = Segment(Point(4, 3), Point(3, 3))

    t1_2.add_segment(s6)
    t1_2.add_segment(s7)
    t1_2.add_segment(s8)

    i1.add_trace(t1_1)
    i1.add_trace(t1_2)

    t2_1 = generate_trace([(1, 3), (1, 5), (3, 5), (3, 3), (5, 3)])
    t2_2 = generate_trace([(3, 1), (2, 1), (2, 3), (3, 3)])
    i2.add_trace(t2_1)
    i2.add_trace(t2_2)

    t3_1 = generate_trace([(1, 3), (1, 5), (4, 5), (4, 4), (5, 4), (5, 3)])
    t3_2 = generate_trace([(3, 1), (3, 3)])
    i3.add_trace(t3_1)
    i3.add_trace(t3_2)

    t4_1 = generate_trace([(1, 3), (3, 3), (3, 6), (5, 6), (5, 3)])
    t4_2 = generate_trace([(3, 1), (3, 3)])
    i4.add_trace(t4_1)
    i4.add_trace(t4_2)

    t5_1 = generate_trace([(1, 3), (1, 4), (4, 4), (4, 3), (5, 3)])
    t5_2 = generate_trace([(3, 1), (2, 1), (2, 3), (3, 3)])
    i5.add_trace(t5_1)
    i5.add_trace(t5_2)

    f1 = Fitness(100, 10, 5, 100, 50)

    i1.plot_segments("", f1)
    i2.plot_segments("", f1)
    i3.plot_segments("", f1)
    i4.plot_segments("", f1)
    i5.plot_segments("", f1)

    p1 = Population()
    p1.add_individual(i1)
    p1.add_individual(i2)
    p1.add_individual(i3)
    p1.add_individual(i4)
    p1.add_individual(i5)

    p1.fitness = f1
    p1.grade_population()

    p1.tournament_operator(3, True)
    p1.tournament_operator(3, True)

    p1.roulette_operator(True)
    p1.roulette_operator(True)

    problem = Problem()
    i1.plot_segments("i1 Przed mutacją", f1)
    mutated = problem.mutation_operator(i1, False, 0.9)  # 4 wydłużyć
    mutated.plot_segments("i1 Po mutacji", f1)

    i2.plot_segments("i2 Przed mutacją", f1)
    mutated = problem.mutation_operator(i2, True, 0.9)  # 4 wydłużyć
    i2.plot_segments("i2 Po mutacji", f1)


    # pop.generate_population(board0, 50)

    # result = problem.mutation_operator(pop.best_individual(), True, 0.9)
    # result.plot_segments()

