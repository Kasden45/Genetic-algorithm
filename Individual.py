import numpy as np
import pylab as pl
from matplotlib import collections  as mc, ticker
import random


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
        collisions = [x for x in self.all_points() if x in segment.middle_points()[1:]]
        return any(collisions)

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

    def all_collisions(self):
        """
        Counts number of collisions in the solution
        :return:
        """
        collisions = set()
        no_collisions = 0
        for trace in self.traces:
            for point in trace.trace_route():
                if point not in collisions:
                    collisions.add(point)
                else:
                    no_collisions += 1
        return no_collisions

    def all_collision_points(self):
        """

        :return: points that cause collisions
        """
        collisions = set()
        colliding_points = set()
        for trace in self.traces:
            for point in trace.trace_route():
                if point not in collisions:
                    collisions.add(point)
                else:
                    colliding_points.add(point)
        return colliding_points

    def plot_segments(self, title="Title", fitness=None):
        """
        Shows plot with the solution
        :param title: title of the plot
        :param fitness: fitness object with fitness function
        :return:
        """
        segments = fitness.total_segments(self)
        length = fitness.total_length(self)
        collisions = fitness.collisions(self)
        score = fitness.count_fitness(self)


        fig, ax = pl.subplots()
        circles = []
        pl.grid()
        pl.title("{}\nScore: {}".format(title, score))
        for trace in self.traces:
            lines = []
            color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            c = np.array([color])
            for segment in trace.segments:
                lines.append([segment.beg.coords(), segment.end.coords()])
            lc = mc.LineCollection(lines, colors=c, linewidths=2)
            circles.append(pl.Circle(trace.pair.beg.coords(), 0.15, color=color, fill=True))
            circles.append(pl.Circle(trace.pair.end.coords(), 0.15, color=color, fill=True))
            ax.add_collection(lc)

        for circle in circles:
            ax.add_patch(circle)
        ax.invert_yaxis()
        c = np.array(["black"])
        lines = [[(0, 0), (0, self.board.y)],
                 [(0, self.board.y), (self.board.x, self.board.y)],
                 [(self.board.x, self.board.y), (self.board.x, 0)],
                 [(0, 0), (self.board.x, 0)]]
        lc = mc.LineCollection(lines, colors=c, linewidths=1)
        ax.add_collection(lc)
        ax.margins(0.1)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        pl.figtext(0.5, 0.01, "Segments:{} Length:{} Collisions:{}".format(segments, length, collisions), ha="center", fontsize=14,
                    bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})
        print("Collide")
        for point in self.all_collision_points():
            print((point.x, point.y))
            ax.plot(point.x, point.y, marker="x", color="black")

        # pl.ylim([0, self.board.y])
        # pl.xlim([0, self.board.x])
        pl.draw()
        pl.waitforbuttonpress(0)
        #pl.show()


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

    def __eq__(self, other):
        return

