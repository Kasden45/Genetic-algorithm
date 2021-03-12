class Individual:
    def __init__(self, board, traces=None):
        """

        :param board: board on which individual will operate
        :param traces: traces which should connect all pairs on the board
        """
        if traces is None:
            traces = []
        self.board = board
        self.traces = traces
        self.all_traces_connected = False

    def will_collide(self, segment, trace):
        """
        Checks if segment will collide with any of the already connected points
        :param segment:
        :param trace:
        :return: True if segment will collide, False otherwise
        """
        warning = [tr for tr in self.traces if tr != trace]
        war2 = [x for x in self.all_points() if x in segment.middle_points()[1:]]
        return any(war2)

    # or any([trace for trace in warning if
    #         trace.pair.beg in segment.middle_points()[1:] or trace.pair.end in segment.middle_points()[1:]])
    def add_trace(self, trace):
        """
        Adds trace to the collection
        :param trace: trace that should be connected by the individual
        :return: None
        """
        if any(pair for pair in self.board.pairs.values() if pair == trace.pair):
            self.traces.append(trace)

    def check_connected(self):
        """
        If all traces are connected, set flag as True
        :return: None
        """
        if all(trace.connected_pair for trace in self.traces):
            self.all_traces_connected = True

    def all_points(self):
        """

        :return: array of all points connected via traces
        """
        points = []
        for trace in self.traces:
            for segment in trace.segments:
                points.extend(segment.middle_points())

        return points

    def __str__(self):
        """

        :return: readable string with information about all traces and its segments
        """
        temp = ""
        counter = 1
        for trace in self.traces:
            temp += "{}. \n".format(counter) + str(trace) + "\n"
            counter += 1
        return temp
