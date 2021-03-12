from Fitness import Fitness
from Generator import RandomIndividualGenerator


class Population:
    def __init__(self):
        self.population = []
        self.fitness = None
        self.fitness_ranking = []  # (individual, score)

        self.generator = RandomIndividualGenerator()

    def add_individual(self, individual):
        """
        Adds individual to population
        :param individual:
        :return: None
        """
        self.population.append(individual)

    def generate_population(self, board, size):
        """
        Generates pseudo randomly 'size' number of individuals
        :param PCB_Board.PCB_Board board: board that should be solved by individual
        :param int size: number of individuals to be generated
        :return: None
        """
        self.generator.set_board(board)
        for i in range(size):
            self.population.append(self.generator.generate())

    def grade_population(self):
        """
        Uses fitness function to grade every individual in the population, saves and prints the result
        :return:
        """
        counter = 1
        for individual in self.population:
            score = self.fitness.count_fitness(individual)
            # print("{}.".format(counter), "Individual:\n", individual, "\nScore", score)
            self.fitness_ranking.append((individual, score))
            print("LOOB:", self.fitness.length_out_of_bounds(individual))
            print("OOB:", self.fitness.out_of_bounds(individual))
            counter += 1
        self.fitness_ranking.sort(key=lambda ind: ind[1])
        print(self.fitness_ranking)

    def set_fitness(self, col=10, tot_len=5, tot_seg=3, out=1, len_out=1):
        """
        Sets weight of fitness function parts
        :param col: no. collisions
        :param tot_len: total length of traces
        :param tot_seg: total no. segments
        :param out: number of traces that went 'out of bounds'
        :param len_out: length of 'out of bounds' parts
        :return:
        """
        self.fitness = Fitness(col, tot_len, tot_seg, out, len_out)

    def best_individual(self):
        """
        returns best individual in population
        :return:
        """
        return self.fitness_ranking[0][0]
