import copy
import random
import numpy as np
import pylab as pl
from matplotlib import collections as mc, ticker
from Fitness import Fitness
from Generator import RandomIndividualGenerator
from Individual import Individual


class Population:
    def __init__(self):
        self.population = []
        self.fitness = None
        self.fitness_ranking = {}  # place: (individual, score)

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
        self.population = []
        self.generator.set_board(board)
        for i in range(size):
            self.population.append(self.generator.generate())

    def grade_population(self):
        """
        Uses fitness function to grade every individual in the population, saves and prints the result
        :return:
        """
        temp_ranking = []
        counter = 1
        for individual in self.population:
            score = self.fitness.count_fitness(individual)
            # print("{}.".format(counter), "Individual:\n", individual, "\nScore", score)
            temp_ranking.append((individual, score))
            # print("LOOB:", self.fitness.length_out_of_bounds(individual))
            # print("OOB:", self.fitness.out_of_bounds(individual))
            counter += 1
        temp_ranking.sort(key=lambda ind: ind[1])
        for i in range(len(temp_ranking)):
            self.fitness_ranking[i+1] = temp_ranking[i]
        # print(self.fitness_ranking) ------------ WRÓCIC

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
        return self.fitness_ranking[1][0]

    def tournament_operator(self, n, show_plot=False):
        rands = []
        tournament_participants = []
        while len(tournament_participants) < n:
            rand = random.choice(list(self.fitness_ranking.items()))
            rands.append(rand)
            if any([True for rank, value in tournament_participants if rank == rand[0]]):
                continue
            else:
                tournament_participants.append(rand)

        tournament_participants.sort(key=lambda part: part[0])
        if show_plot:
            self.plot_tournament(rands, tournament_participants)
        return tournament_participants[0][1][0]

    def get_roulette_weight(self, number):
        total = sum([ind[1] for _, ind in self.fitness_ranking.items()])
        return number/total

    def roulette_operator(self, show_roulette=False):
        rand = random.random()
        weights = []
        probabilities = []
        segments = {}  # rank: (from, to)
        for i in range(len(self.fitness_ranking)):
            weights.append(1 / self.fitness_ranking[i + 1][1])
        weights_sum = sum(weights)

        for i in range(len(self.fitness_ranking)):
            probabilities.append(weights[i] / weights_sum)
        #print("Suma pstw =", sum(probabilities))
        section_start = 0
        for i in range(len(self.fitness_ranking)):
            section_end = section_start + probabilities[i]
            segments[i+1] = section_start, section_end
            section_start = section_end

        for rank, segment in segments.items():
            if segment[0] < rand <= segment[1]:
                if show_roulette:
                    print(rand, "is in", "({:.3f}, {:.3f})".format(segment[0], segment[1]))
                    print("Segments:", segments)
                return self.fitness_ranking[rank][0]



    def plot_tournament(self, guesses, participants):

        fig, ax = pl.subplots()
        repeated = [guess for guess in guesses if guesses.count(guess[0])>1]
        losers_participants = participants[1:]
        winner = participants[0]
        pl.grid()
        lines = []
        c = np.array(["red"])
        for loser in losers_participants:
            lines.append([(loser[0], 0), (loser[0], loser[1][1])])

        lc = mc.LineCollection(lines, colors=c, linewidths=2)
        ax.add_collection(lc)
        lines.clear()

        c = np.array(["green"])
        lines.append([(winner[0], 0), (winner[0], winner[1][1])])
        lc = mc.LineCollection(lines, colors=c, linewidths=2)
        ax.add_collection(lc)

        ax.margins(0.1)
        #ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

        # pl.ylim([0, self.board.y])
        pl.xlim([0, len(self.fitness_ranking)])
        pl.draw()
        pl.waitforbuttonpress(0)

        pass

