import os
import pickle
import numpy as np
from Problem import Problem


class Tester:
    def __init__(self):
        pass
        self.iterations = None
        self.population_sizes = None
        self.tournament_sizes = None
        self.cross_probs = None
        self.mutation_probs = None
        self.problem = None
        self.boards = ["zad0.txt", "zad1.txt", "zad2.txt", "zad3.txt"]
        self.results = {}  # Name/parameters: [results]

    def do_testing(self):
        px = self.cross_probs[0]
        pm = self.mutation_probs[0]
        tournaments = self.tournament_sizes[0]
        selection = "Tournament" # Roulette
        for iters in self.iterations:
            for pop_size in self.population_sizes:
                for board in self.boards:
                    for i in range(10):
                        # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                        self.problem = Problem(px, pm,pop_size, iters, selection, board, tournaments)
                        params = "{}_{}_{}_{}_{}_{}_{}".format(px, pm, pop_size, iters, "Tournament", board, tournaments)
                        print("NOW: {}".format(params))
                        result = self.problem.solve_problem()
                        if params not in self.results.keys():
                            self.results[params] = [result]
                        else:
                            self.results[params].append(result)
                        self.save_results()

    def set_iterations(self, _from, _to, _interval):
        self.iterations = np.arange(_from, _to+1, _interval)

    def set_population_size(self, _from, _to, _interval):
        self.population_sizes = np.arange(_from, _to+1, _interval)

    def set_tournament_size(self, _from, _to, _interval):
        self.tournament_sizes = np.arange(_from, _to+1, _interval)

    def set_cross_prob(self, _from, _to, _interval):
        self.cross_probs = np.arange(_from, _to+0.001, _interval)

    def set_mutation_prob(self, _from, _to, _interval):
        self.mutation_probs = np.arange(_from, _to+0.001, _interval)

    def save_results(self):
        filename = "Results_{}".format(3)
        try:
            with open(f"{os.curdir}/Results/{filename}", "wb") as f:
                pickle.dump(self.results, f)
        except Exception as e:
            print(e)
        print("RESULTS SAVED")

    def load_results(self):
        filename = input("Chose file with results (Results_{}):")
        try:
            with open(f"{os.curdir}/Results/{filename}", "rb") as f:
                self.results = pickle.load(f)
        except Exception as e:
            print(e)

    def results_to_txt(self):
        with open("Readable_results/res_3.txt", "w+") as f:
            for params, result in self.results.items():
                f.write(params)
                f.write(" Best {}".format(np.max([pair[0][1] for pair in result])))
                f.write(" Worst {}".format(np.min([pair[0][1] for pair in result])))
                f.write(" Avg {}".format(np.average([pair[0][1] for pair in result])))
                f.write(" Std {}".format(np.std([pair[0][1] for pair in result])))
                f.write("\n")
