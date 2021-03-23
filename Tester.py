import os
import pickle


class Tester:
    def __init__(self, problem):
        pass
        self.iterations = None
        self.population_sizes = None
        self.tournament_sizes = None
        self.cross_probs = None
        self.mutation_probs = None
        self.problem = problem
        self.boards = ["zad0.txt", "zad1.txt", "zad2.txt", "zad3.txt"]
        self.results = {}  # Name/parameters: [results]

    def do_testing(self):
        pass

    def set_iterations(self, _from, _to, _interval):
        self.iterations = range(_from, _to, _interval)

    def set_population_size(self, _from, _to, _interval):
        self.population_sizes = range(_from, _to, _interval)

    def set_tournament_size(self, _from, _to, _interval):
        self.tournament_sizes = range(_from, _to, _interval)

    def set_cross_prob(self, _from, _to, _interval):
        self.cross_probs = range(_from, _to, _interval)

    def set_mutation_prob(self, _from, _to, _interval):
        self.mutation_probs = range(_from, _to, _interval)

    def save_results(self):
        filename = "Results_{}".format(1)
        try:
            with open(f"{os.curdir}/Results/{filename}", "wb") as f:
                pickle.dump(self.results, f)
        except Exception as e:
            print(e)

    def load_results(self):
        filename = input("Chose file with results (Results_{}):")
        try:
            with open(f"{os.curdir}/Results/{filename}", "wb") as f:
                self.results = pickle.load(f)
        except Exception as e:
            print(e)