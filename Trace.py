from Segment import Segment


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
            route.extend(segment.middle_points()[1:])

        return route

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
