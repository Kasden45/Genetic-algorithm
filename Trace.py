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
        """
        All points from trace's segments in order of the trace
        :return: Ordered points
        """
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
        """
        Cheks if the solution hasn't been achieved befeore the end of trace
        :return:
        """
        for i in range(len(self.segments)-1):
            if self.segments[i].end == self.pair.end:
                self.segments = self.segments[:i+1]
                return

    def lengthen_segment(self, i):
        """
        Increases segment's length by 1 and repairs the structure
        :param i: index of segment
        :return:
        """
        segment = self.segments[i]
        segment.lengthen_segment()
        next = self.segments[i+1]
        next.move_in_direction(segment.direction())
        if i+1 == len(self.segments)-1:
            # Add
            self.add_segment(Segment(copy.deepcopy(next.end), copy.deepcopy(self.pair.end)))
        else:
            next_next = self.segments[i+2]
            if next_next.direction() == segment.direction():
                if len(next_next) > 1:
                    # Shorten
                    next_next.cut_segment_back()
                elif next_next == self.segments[-1]:
                    # Delete
                    self.segments.remove(next_next)
                else:
                    # Merge
                    if 3 - self.segments[i+3].direction() != next.direction():
                        self.segments[i+3].beg = copy.deepcopy(next.beg)
                        self.segments.remove(next)
                        self.segments.remove(next_next)
                    else:
                        # Cancel the process
                        next.move_in_direction(3 - segment.direction())
                        segment.shorten_segment()
            else:
                next_next.extend_segment_back()
        self.chek_solution_again()

    def shorten_segment(self, i):
        """
        Decreases segment's length by 1 and repairs the structure
        :param i:
        :return:
        """
        segment = self.segments[i]
        if len(segment) == 1:
            return
        segment.shorten_segment()
        next = self.segments[i+1]
        if segment.end.coords() != next.beg.coords():
            next.move_in_direction(3-segment.direction())  # move in opposite direction
        if i+1 == len(self.segments)-1:  # If the last segment has been moved
            # Add
            self.add_segment(Segment(copy.deepcopy(next.end), copy.deepcopy(self.pair.end)))
        else:
            next_next = self.segments[i+2]
            if next_next.direction() != segment.direction():
                if len(next_next) > 1:
                    # Shorten
                    next_next.cut_segment_back()
                elif next_next == self.segments[-1]:
                    # Delete
                    self.segments.remove(next_next)
                else:
                    # Merge
                    if 3 - self.segments[i+3].direction() != next.direction():
                        self.segments[i+3].beg = copy.deepcopy(next.beg)
                        self.segments.remove(next)
                        self.segments.remove(next_next)
                    else:
                        # Cancel the process
                        next.move_in_direction(segment.direction())
                        segment.lengthen_segment()

            else:
                # Same direction
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
