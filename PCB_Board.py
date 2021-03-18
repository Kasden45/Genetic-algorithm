import numpy as np

from Pair import Pair
from Point import Point


class PCB_Board:
    def __init__(self, board_txt = None):
        self._pairs = {}
        self._matrix = np.empty([0, 0])
        self._x = 0
        self._y = 0
        if board_txt is not None:
            self.read_board(board_txt)

    def points_in_pairs(self):
        points = []
        for pair, val in self._pairs.items():
            points.append(val.beg.coords())
            points.append(val.end.coords())
        return points

    def add_pair(self, pair):
        """
        Adds pair to the board
        :param pair: Pair object representing pair of points that should be connected on the board
        :return: None
        """
        self._pairs[len(self._pairs) + 1] = pair
        self._matrix[pair.beg.x][pair.beg.y] = len(self._pairs)
        self._matrix[pair.end.x][pair.end.y] = len(self._pairs)

    def print_board(self):
        """
        Prints the matrix of the board in readable form
        :return: formatted string
        """
        temp = ""
        for row in self._matrix:
            for elem in row:
                if elem is None:
                    temp += "X  "
                else:
                    temp += str(elem) + "  "
            temp += "\n"
        return temp

    def read_board(self, txt_file):
        """
        Reads board from .txt file
        :param txt_file:
        :return: None
        """
        with open(txt_file, "r") as f:
            file = f.readlines()
            counter = 0
        for line in file:
            data = line.split(";")
            if counter == 0:
                self._x = int(data[0])
                self._y = int(data[1])
                self._matrix = np.empty([self._x, self._y], dtype=np.object)
            else:
                self.add_pair(Pair(Point(int(data[0]), int(data[1])), Point(int(data[2]), int(data[3]))))
            counter += 1

    @property
    def x(self):
        return self._x

    @property
    def pairs(self):
        return self._pairs

    @property
    def y(self):
        return self._y

    def __str__(self):

        return "Board: \n{}\nPairs: {}".format(self.print_board(),
                                               list((number, str(pair)) for number, pair in self._pairs.items()))
