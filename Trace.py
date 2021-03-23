import copy

from Segment import Segment
from Parameters import *
class Trace:
    def __init__(self, pair, segments=None):
        if segments is None:
            segments = []
        self.segments = segments  # segment is an array of connected points in straight line
        self.pair = pair
        self.connected_pair = False

    def add_segment(self, segment):
        """
        Adds segment to the trace
        :param Segment segment: segment to be added
        :return:
        """

        self.segments.append(segment)
        if segment.end == self.pair.end:
            self.connected_pair = True

    def extend_last_segment(self, point):
        """
        Extends last segments to the given point
        :param Point.Point point: point to which the last segment will be extended
        :return:
        """
        self.segments[-1] = Segment(self.segments[-1].beg, point)
        if self.segments[-1].end == self.pair.end:
            self.connected_pair = True

    def last_point(self):
        return self.trace_route()[-1] if len(self.segments) > 0 else self.pair.beg

    def last_segment(self):
        return self.segments[-1]

    def last_direction(self):
        return self.segments[-1].direction() if len(self.segments) > 0 else None

    def trace_route(self):
        route = [self.segments[0].beg]
        for segment in self.segments:
            try:
                route.extend(segment.middle_points()[1:])
            except Exception:
                print("ERROR OCCURRED")
                for segment in self.segments:
                    print("({},{})".format(segment.beg, segment.end))
        return route

    def chek_solution_again(self):
        for i in range(len(self.segments)-1):
            if self.segments[i].end == self.pair.end:
                self.segments = self.segments[:i+1]
                return

    def lengthen_segment(self, i):
        segment = self.segments[i]
        segment.lengthen_segment()
        next = self.segments[i+1]
        next.move_in_direction(segment.direction())
        if i+1 == len(self.segments)-1:
            # Dodawanie
            self.add_segment(Segment(next.end, self.pair.end))
        else:
            next_next = self.segments[i+2]
            if next_next.direction() == segment.direction():
                if len(next_next) > 1:
                    # Skracanie
                    #print("Skracanie")
                    next_next.cut_segment_back()
                elif next_next == self.segments[-1]:
                    # Usuwanie
                    #print("Usuwanie")
                    self.segments.remove(next_next)
                else:
                    # Laczenie
                    #print("Laczenie")
                    if 3 - self.segments[i+3].direction() != next.direction():
                        self.segments[i+3].beg = copy.deepcopy(next.beg)
                        self.segments.remove(next)
                        self.segments.remove(next_next)
                    else:
                        # Cofka
                        next.move_in_direction(3 - segment.direction())
                        segment.shorten_segment()
            else:
                #print("Other direction")
                next_next.extend_segment_back()
        self.chek_solution_again()

    def shorten_segment(self, i):
        segment = self.segments[i]
        if len(segment) == 1:
            return
        segment.shorten_segment()
        next = self.segments[i+1]
        if segment.end.coords() != next.beg.coords():
            next.move_in_direction(3-segment.direction())  # przesuń w odwrotną stronę
        if i+1 == len(self.segments)-1:  # Jeżeli przesunięto ostatni fragment
            # Dodawanie
            self.add_segment(Segment(next.end, self.pair.end))
        else:
            next_next = self.segments[i+2]
            if next_next.direction() != segment.direction():
                if len(next_next) > 1:
                    # Skracanie
                    next_next.cut_segment_back()
                elif next_next == self.segments[-1]:
                    # Usuwanie
                    self.segments.remove(next_next)
                else:
                    # Laczenie
                    if 3 - self.segments[i+3].direction() != next.direction():
                        self.segments[i+3].beg = next.beg
                        self.segments.remove(next)
                        self.segments.remove(next_next)
                    else:
                        # Cofka
                        next.move_in_direction(segment.direction())
                        segment.lengthen_segment()

            else:
                # W te sama
                next_next.extend_segment_back()
        self.chek_solution_again()
    def print_trace_route(self):
        """
        Creates string with readable form of all segments creating the trace
        :return:
        """
        if len(self.segments) == 0:
            return ""
        else:
            temp = ""
            for point in self.trace_route():
                temp += str(point) + (" -> " if point != self.trace_route()[-1] else "")

            return temp

    def __str__(self):
        temp = ""
        for segment in self.segments:
            temp += str(segment) + (" \n-->\n " if segment != self.segments[-1] else "")
        return temp

    def __eq__(self, other):
        return self.pair == other.pair

    def __hash__(self):
        return hash(self.pair.beg) ^ hash(self.pair.end)
