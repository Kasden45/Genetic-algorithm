class Pair:
    def __init__(self, beginning, end):
        self.beg = beginning
        self.end = end

    def __str__(self):
        return "({},{}) -> ({},{})".format(self.beg.x, self.beg.y, self.end.x, self.end.y)

    def __eq__(self, other):
        return self.beg == other.beg and self.end == other.end
