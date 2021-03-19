import copy
import random

from Individual import Individual
from PCB_Board import PCB_Board
from Populations import Population
from Parameters import *
collisions_weight = 1000
total_len_weight = 25
total_segments_weight = 2
out_weight = 2000
len_out_weight = 1000

class Problem:
    def __init__(self, px=0.6, pm=0.5, size=50, iterations=10, selection="Tournament", board_file="zad2.txt", n=20):
        self.px = px
        self.pm = pm
        self.all_populations = []
        self.population_size = size
        self.iterations = iterations
        self.selection = selection  # Tournament, Roulette
        self.board = PCB_Board()
        self.board.read_board(board_file)
        self.best_solution = None
        self.tournament_n = n

    def crossover_operator(self, p1: Individual, p2: Individual):
        Px = 0.5
        new_traces_1 = []
        new_traces_2 = []
        for i in range(len(p1.traces)):
            if i % 2 == 0 and random.random() > Px:
                new_traces_1.append(copy.deepcopy(p2.traces[i]))
                new_traces_2.append(copy.deepcopy(p1.traces[i]))
            else:
                new_traces_1.append(copy.deepcopy(p1.traces[i]))
                new_traces_2.append(copy.deepcopy(p2.traces[i]))

        child1 = Individual(p1.board, traces=new_traces_1)

        child2 = Individual(p1.board, traces=new_traces_2)
        return child1, child2

    def mutation_operator(self, child, crossed, pm):
        if not crossed:
        #if True:
            mutable = copy.deepcopy(child)
        else:
            mutable = child
        #mutable.plot_segments()
        for i in range(len(mutable.traces)):
            # if mutate than mutate random segment in trace
            if random.random() < pm and len(mutable.traces[i].segments) > 1:

                segment_index = random.randint(0, len(mutable.traces[i].segments[:-1])-1)
                #print("trace: ", i, "segment:", segment_index)
                if random.random() < 0.5:
                    # Wydłużanie o 1
                    mutable.traces[i].lengthen_segment(segment_index)
                    #mutable.plot_segments()
                else:
                    pass
                    # Skracanie o 1
                    mutable.traces[i].shorten_segment(segment_index)
                    #mutable.plot_segments()
                mutable.traces[i].trace_route()
        # try:
        #     print("Mutable:", mutable)
        # except:
        #     pass

        return mutable

    def solve_problem(self):
        previous_population = Population()
        previous_population.set_fitness(collisions_weight, total_len_weight, total_segments_weight, out_weight,
                                        len_out_weight)
        previous_population.generate_population(self.board, self.population_size)
        previous_population.grade_population()
        self.best_solution = (
        copy.deepcopy(previous_population.best_individual()), previous_population.fitness_ranking[1][1])
        counter = 1
        for i in range(self.iterations):
            print("Iteration:", counter)
            counter += 1
            new_population = Population()
            new_population.set_fitness(collisions_weight, total_len_weight, total_segments_weight, out_weight,
                                       len_out_weight)
            while len(new_population.population) < self.population_size:
                p1 = None
                p2 = None
                if self.selection == "Roulette":
                    p1 = previous_population.roulette_operator()
                    p2 = previous_population.roulette_operator()
                elif self.selection == "Tournament":
                    p1 = previous_population.tournament_operator(self.tournament_n)
                    p2 = previous_population.tournament_operator(self.tournament_n)

                crossed = False
                child2 = None

                if random.random() < self.px:
                    child1, child2 = self.crossover_operator(p1, p2)
                    crossed = True
                else:
                    child1 = copy.deepcopy(random.choice([p1, p2]))

                new_population.add_individual(self.mutation_operator(child1, crossed, self.pm))
                if child2 is not None and len(new_population.population) < self.population_size:
                    new_population.add_individual(self.mutation_operator(child2, crossed, self.pm))

            new_population.grade_population()
            new_best_score = new_population.fitness_ranking[1][1]
            new_population.best_individual().plot_segments()
            print(counter, "pop best:", new_best_score, "ovr best", self.best_solution[1])

            if new_best_score < self.best_solution[1]:
                self.best_solution = (new_population.best_individual(), new_best_score)
            previous_population = new_population
        return self.best_solution
