from Pair import Pair
from Point import Point


class Segment(Pair):
    def __init__(self, beginning, end):
        Pair.__init__(self, beginning, end)

    def middle_points(self):
        """
        Creates list with Points between beginning and the end of the Segment
        :return: list
        """
        if self.beg.x == self.end.x:
            lista = list(Point(self.beg.x, point) for point in
                         range(self.beg.y, self.end.y, 1 if self.beg.y < self.end.y else -1))
            lista.append(Point(self.end.x, self.end.y))
            return lista
        elif self.beg.y == self.end.y:
            lista = list(Point(point, self.beg.y) for point in
                         range(self.beg.x, self.end.x, 1 if self.beg.x < self.end.x else -1))
            lista.append(Point(self.end.x, self.end.y))
            return lista

    def direction(self):
        """

        :return: number representing segment's direction (0 - UP, 1 - LEFT, 2 - RIGHT, 3 - DOWN)
        """
        if self.beg.x == self.end.x:
            if self.beg.y > self.end.y:
                return 0
            else:
                return 3
        elif self.beg.y == self.end.y:
            if self.beg.x > self.end.x:
                return 2
            else:
                return 1

    def __str__(self):
        return super().__str__() + " = " + str(list(str(point) for point in self.middle_points()))

    def __len__(self):
        return len(self.middle_points()) - 1

    def collisions(self, other):
        """
        Count no. collisions between tho segments
        :param Segment other: other segment
        :return: no. collisions
        """
        return len(list(True for point in self.middle_points() if point in other.middle_points()))
