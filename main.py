from Populations import Population
from Fitness import Fitness
from Generator import RandomIndividualGenerator
from Individual import Individual
from PCB_Board import PCB_Board
from Pair import Pair
from Point import Point
from Segment import Segment
from Trace import Trace

if __name__ == '__main__':
    """
    Initializing boards and reading data
    """
    board1 = PCB_Board()
    board1.read_board("zad0.txt")
    print(board1)

    board2 = PCB_Board()
    board2.read_board("zad1.txt")
    print(board2)

    board3 = PCB_Board()
    board3.read_board("zad2.txt")
    print(board3)

    board4 = PCB_Board()
    board4.read_board("zad3.txt")
    print(board4)

    """
    Testing segments
    """
    s1 = Segment(Point(1, 5), Point(1, 9))
    print(s1, "s1 Length:", len(s1))
    # print(s1.middle_points())

    s2 = Segment(Point(4, 5), Point(1, 5))
    print(s2, "s2 Length:", len(s2))

    s3 = Segment(Point(2, 3), Point(4, 3))

    s4 = Segment(Point(3, 1), Point(3, 5))

    print(s3, "s3 Length:", len(s3))
    print(s4, "s4 Length:", len(s4))
    print(s1.collisions(s2))
    print(s2.collisions(s1))
    print(s1.collisions(s3))
    print(s2.collisions(s3))

    """
        Testing traces
    """
    t1 = Trace(Pair(Point(4, 5), Point(1, 9)), [s2, s1])

    t2 = Trace(Pair(Point(4, 5), Point(1, 9)), [s3])

    t3 = Trace(Pair(Point(4, 5), Point(1, 9)), [s4])
    print(t1.print_trace_route())
    """
        Testing individuals and fitness function
    """
    i1 = Individual(board1, [t1, t2])

    f1 = Fitness(10, 5, 3)
    print("Collisions ", f1.collisions(i1))
    print("Length ", f1.total_length(i1))
    print("Segments ", f1.total_segments(i1))
    # print("Out of bounds", f1.out_of_bounds(i1))
    # print("Length out of bounds", f1.length_out_of_bounds(i1))

    print("t2 last\n", t2.last_point())
    print("i1\n", str(i1))

    print("t1\n", str(t1))
    t1.extend_last_segment(Point(1, 12))
    print("t1\n", str(t1))
    """
    Generator test
    """
    rg = RandomIndividualGenerator(board1)

    """
    Actual population test
    """
    pop = Population()
    pop.set_fitness(10, 5, 2, 20, 10)
    pop.generate_population(board1, 10)
    pop.grade_population()
    print(pop.best_individual())
