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

    def lengthen_segment(self):
        direction = self.direction()
        if direction == 0:
            self.end = Point(self.end.x, self.end.y-1)
        elif direction == 1:
            self.end = Point(self.end.x - 1, self.end.y)
        elif direction == 2:
            self.end = Point(self.end.x + 1, self.end.y)
        elif direction == 3:
            self.end = Point(self.end.x, self.end.y+1)

    def shorten_segment(self):
        direction = self.direction()
        if direction == 0:
            self.end = Point(self.end.x, self.end.y+1)
        elif direction == 1:
            self.end = Point(self.end.x + 1, self.end.y)
        elif direction == 2:
            self.end = Point(self.end.x - 1, self.end.y)
        elif direction == 3:
            self.end = Point(self.end.x, self.end.y-1)


    def cut_segment_back(self):
        direction = self.direction()
        if direction == 0:
            self.beg = Point(self.beg.x, self.beg.y-1)
        elif direction == 1:
            self.beg = Point(self.beg.x-1, self.beg.y)
        elif direction == 2:
            self.beg = Point(self.beg.x+1, self.beg.y)
        elif direction == 3:
            self.beg = Point(self.beg.x, self.beg.y+1)

    def extend_segment_back(self):
        direction = self.direction()
        if direction == 0:
            self.beg = Point(self.beg.x, self.beg.y+1)
        elif direction == 1:
            self.beg = Point(self.beg.x+1, self.beg.y)
        elif direction == 2:
            self.beg = Point(self.beg.x-1, self.beg.y)
        elif direction == 3:
            self.beg = Point(self.beg.x, self.beg.y-1)



    def move_in_direction(self, direction):

        if direction == 0:
            self.beg = Point(self.beg.x, self.beg.y-1)
            self.end = Point(self.end.x, self.end.y-1)
        elif direction == 1:
            self.beg = Point(self.beg.x-1, self.beg.y)
            self.end = Point(self.end.x-1, self.end.y)
        elif direction == 2:
            self.beg = Point(self.beg.x + 1, self.beg.y)
            self.end = Point(self.end.x + 1, self.end.y)
        elif direction == 3:
            self.beg = Point(self.beg.x, self.beg.y + 1)
            self.end = Point(self.end.x, self.end.y + 1)

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
                return 1
            else:
                return 2

    def __str__(self):
        return super().__str__() + " = " + str(list(str(point) for point in self.middle_points()))

    def __len__(self):
        direction = self.direction()
        if direction == 0 or direction == 3:
            return abs(self.end.y - self.beg.y)
        elif direction == 1 or direction == 2:
            return abs(self.end.x - self.beg.x)


    def collisions(self, other):
        """
        Count no. collisions between tho segments
        :param Segment other: other segment
        :return: no. collisions
        """
        return len(list(True for point in self.middle_points() if point in other.middle_points()))
