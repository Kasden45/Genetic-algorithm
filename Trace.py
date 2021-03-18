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

    def lengthen_segment(self, i):
        print("Lengthen")
        segment = self.segments[i]
        segment.lengthen_segment()
        next = self.segments[i+1]
        if segment.end.coords() != next.beg.coords():
            next.move_in_direction(segment.direction())
        if i+1 == len(self.segments)-1:
            self.add_segment(Segment(next.end, self.pair.end))
        else:
            next_next = self.segments[i+2]
            if next_next.direction() == segment.direction():
                if len(next_next) > 1:
                    # Skracanie
                    next_next.cut_segment_back()
                elif next_next == self.segments[-1]:
                    # Usuwanie
                    self.segments.remove(next_next)
                else:
                    # Laczenie
                    self.segments[i+3].beg = next.beg
                    self.segments.remove(next)
                    self.segments.remove(next_next)
            else:
                next_next.extend_segment_back()

    def shorten_segment(self, i):
        print("Shorten")
        segment = self.segments[i]
        if len(segment) == 1:
            return
        segment.shorten_segment()
        next = self.segments[i+1]
        if segment.end.coords() != next.beg.coords():
            next.move_in_direction(3-segment.direction())  # przesuń w odwrotną stronę
        if i+1 == len(self.segments)-1:  # Jeżeli przesunięto ostatni fragment
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
                    self.segments[i+3].beg = next.beg
                    self.segments.remove(next)
                    self.segments.remove(next_next)
            else:
                next_next.extend_segment_back()

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
