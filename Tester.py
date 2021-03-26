import csv
import os
import pickle
import numpy as np
from Problem import Problem

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def txt_to_csv(name, csv_name):
    with open(f"{os.curdir}/Readable_results/{name}.txt", 'r') as f:
        results = f.readlines()
    fnames = ["Instance", "Best", "Worst", "Average", "Std"]
    with open(f'{os.curdir}/CSV_Results/{csv_name}.csv', 'w', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(fnames)
        for line in results:
            row = []
            splitted = line.split()
            for text in splitted[::2]:
                if isfloat(text):
                    row.append(float(text))
                else:
                    row.append(text)
            writer.writerow(row)

    pass

class Tester:
    def __init__(self, boards):
        pass
        self.iterations = None
        self.population_sizes = None
        self.tournament_sizes = None
        self.cross_probs = None
        self.mutation_probs = None
        self.problem = None
        self.boards = boards
        self.results = {}  # Name/parameters: [results]
        self.selections = ["Roulette"]  # ["Tournament"]

        self.default = {"px": 0.5, "pm": 0.5, "pop_size": 200, "iterations": 20, "selection": "Tournament", "n": 0.1}

    def do_testing_random(self, filename):
        """
        Tests random solutions
        :param filename: name of the file in which results will be stored
        :return:
        """
        self.results.clear()
        population_size = self.default["pop_size"]
        iteration = self.default["iterations"]
        for board in self.boards:
                print(f"Random generation: Board: {board} Size: {population_size*iteration*10}")
                # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                self.problem = Problem(size=population_size*iteration*10, board_file=board)
                params = "{}_{}_{}".format(population_size, iteration, board)
                print("NOW: {}".format(params))
                try:
                    result = self.problem.solve_problem_randomly()
                except Exception as e:
                    continue
                self.results[params] = result
                self.save_results(filename)
        self.random_results_to_txt(filename)
    def do_testing_iterations(self, filename):
        """
        Tests number of iterations
        :param filename: name of the file in which results will be stored
        :return:
        """
        logf = open("download.log", "w")
        self.results.clear()
        px = self.default["px"]
        pm = self.default["pm"]
        tournaments = self.default["n"]
        population_size = self.default["pop_size"]
        selection = self.default["selection"]
        for iteration in self.iterations:
            for board in self.boards:
                counter = 1
                while counter <= 10:
                    print(f"Iterations: {iteration} -> {counter}/10")
                    # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                    self.problem = Problem(px, pm, population_size, iteration, selection, board, tournaments)
                    params = "{}_{}_{}_{}_{}_{}_{}".format(px, pm, population_size, iteration, selection, board, tournaments)
                    print("NOW: {}".format(params))
                    try:
                        result = self.problem.solve_problem()
                    except Exception as e:
                        logf.write(f"ERROR: {e}")
                        continue
                    counter += 1
                    if params not in self.results.keys():
                        self.results[params] = [result]
                    else:
                        self.results[params].append(result)
                    self.save_results(filename)
            self.results_to_txt(filename)

    def do_testing_populations(self, filename):
        """
        Tests population size parameters
        :param filename: name of the file in which results will be stored
        :return:
        """
        logf = open("download.log", "w")
        self.results.clear()
        px = self.default["px"]
        pm = self.default["pm"]
        tournaments = self.default["n"]
        iteration = self.default["iterations"]
        selection = self.default["selection"]
        for pop_size in self.population_sizes:
            for board in self.boards:
                counter = 1
                while counter <= 10:
                    print(f"Populations: {pop_size} -> {counter}/10")
                    # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                    self.problem = Problem(px, pm, pop_size, iteration, selection, board, tournaments)
                    params = "{}_{}_{}_{}_{}_{}_{}".format(px, pm, pop_size, iteration, selection, board,
                                                           tournaments)
                    print("NOW: {}".format(params))
                    try:
                        result = self.problem.solve_problem()
                    except Exception as e:
                        logf.write(f"ERROR: {e}")
                        continue
                    counter += 1
                    if params not in self.results.keys():
                        self.results[params] = [result]
                    else:
                        self.results[params].append(result)
                    self.save_results(filename)
            self.results_to_txt(filename)

    def do_testing_pm(self, filename):
        """
        Tests mutation probability parameters
        :param filename: name of the file in which results will be stored
        :return:
        """
        logf = open("download.log", "w")
        self.results.clear()
        px = self.default["px"]
        pop_size = self.default["pop_size"]
        tournaments = self.default["n"]
        iteration = self.default["iterations"]
        selection = self.default["selection"]
        for pm in self.mutation_probs:
            for board in self.boards:
                counter = 1
                while counter <= 10:
                    print(f"Pm: {pm} -> {counter}/10")
                    # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                    self.problem = Problem(px, pm, pop_size, iteration, selection, board, tournaments)
                    params = "{}_{}_{}_{}_{}_{}_{}".format(px, pm, pop_size, iteration, selection, board,
                                                           tournaments)
                    print("NOW: {}".format(params))
                    try:
                        result = self.problem.solve_problem()
                    except Exception as e:
                        logf.write(f"ERROR: {e}")
                        continue
                    counter += 1
                    if params not in self.results.keys():
                        self.results[params] = [result]
                    else:
                        self.results[params].append(result)
                    self.save_results(filename)
            self.results_to_txt(filename)

    def do_testing_px(self, filename):
        """
        Tests crossover probability parameters
        :param filename: name of the file in which results will be stored
        :return:
        """
        logf = open("download.log", "w")
        self.results.clear()
        pm = self.default["pm"]
        pop_size = self.default["pop_size"]
        tournaments = self.default["n"]
        iteration = self.default["iterations"]
        selection = self.default["selection"]
        for px in self.cross_probs:
            for board in self.boards:
                counter = 1
                while counter <= 10:
                    print(f"Px: {px} -> {counter}/10")
                    # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                    self.problem = Problem(px, pm, pop_size, iteration, selection, board, tournaments)
                    params = "{}_{}_{}_{}_{}_{}_{}".format(px, pm, pop_size, iteration, selection, board,
                                                           tournaments)
                    print("NOW: {}".format(params))
                    try:
                        result = self.problem.solve_problem()
                    except Exception as e:
                        logf.write(f"ERROR: {e}")
                        continue
                    counter += 1
                    if params not in self.results.keys():
                        self.results[params] = [result]
                    else:
                        self.results[params].append(result)
                    self.save_results(filename)
            self.results_to_txt(filename)

    def do_testing_selection(self, filename):
        """
        Tests selection parameters
        :param filename: name of the file in which results will be stored
        :return:
        """
        logf = open("download.log", "w")
        self.results.clear()
        px = self.default["px"]
        pm = self.default["pm"]
        #tournaments = self.default["n"]
        iteration = self.default["iterations"]
        pop_size = self.default["pop_size"]
        for selection in self.selections:
            for tournaments in self.tournament_sizes:
                for board in self.boards:
                    counter = 1
                    while counter <= 10:
                        print(f"Selection: {selection} n={tournaments} -> {counter}/10")
                        # (self, px=0.5, pm=0.5, size=2000, iterations=40, selection="Tournament", board_file="zad1.txt", n=30)
                        self.problem = Problem(px, pm,pop_size, iteration, selection, board, tournaments)
                        params = "{}_{}_{}_{}_{}_{}_{}".format(px, pm, pop_size, iteration, selection, board, tournaments)
                        print("NOW: {}".format(params))
                        try:
                            result = self.problem.solve_problem()
                        except Exception as e:
                            logf.write(f"ERROR: {e}")
                            continue
                        counter += 1
                        if params not in self.results.keys():
                            self.results[params] = [result]
                        else:
                            self.results[params].append(result)
                        self.save_results(filename)
                    self.results_to_txt(filename)
        self.results_to_txt(filename)

    def set_iterations(self, _from, _to, _interval):
        self.iterations = np.arange(_from, _to+1, _interval)

    def set_population_size(self, _from, _to, _interval):
        self.population_sizes = np.arange(_from, _to+1, _interval)

    def set_tournament_size(self, _from, _to, _interval):
        self.tournament_sizes = np.arange(_from, _to+0.001, _interval)

    def set_cross_prob(self, _from, _to, _interval):
        self.cross_probs = np.arange(_from, _to+0.001, _interval)

    def set_mutation_prob(self, _from, _to, _interval):
        self.mutation_probs = np.arange(_from, _to+0.001, _interval)

    def save_results(self, name):
        filename = "Results_{}".format(name)
        try:
            with open(f"{os.curdir}/Results/{filename}", "wb") as f:
                pickle.dump(self.results, f)
        except Exception as e:
            print(e)
        print("RESULTS SAVED")

    def load_results(self, name):
        try:
            with open(f"{os.curdir}/Results/Results_{name}", "rb") as f:
                self.results = pickle.load(f)
        except Exception as e:
            print(e)


    def results_to_txt(self, name):
        with open("Readable_results/{}.txt".format(name), "w+") as f:
            for params, result in self.results.items():
                f.write(params)
                f.write(" Best {}".format(np.min([pair[0][1] for pair in result])))
                f.write(" Worst {}".format(np.max([pair[0][1] for pair in result])))
                f.write(" Avg {}".format(np.average([pair[0][1] for pair in result])))
                f.write(" Std {}".format(np.std([pair[0][1] for pair in result])))
                f.write("\n")

    def random_results_to_txt(self, name):
        with open("Readable_results/{}.txt".format(name), "w+") as f:
            for params, result in self.results.items():
                f.write(params)
                f.write(" Best {}".format(np.min([value[1] for rank, value in result.items()])))
                f.write(" Worst {}".format(np.max([value[1] for rank, value in result.items()])))
                f.write(" Avg {}".format(np.average([value[1] for rank, value in result.items()])))
                f.write(" Std {}".format(np.std([value[1] for rank, value in result.items()])))
                f.write("\n")
