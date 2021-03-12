import math
import random

from Individual import Individual
from Point import Point
from Segment import Segment
from Trace import Trace


def point_out_of_bounds(point, board):
    """
    Checks if point is out of the board and
    :param Point point: point to be checked
    :param PCB_Board board: board of given size
    :return: (bool, list) (True if point is out of bounds and False otherwise,
    list of directions in which point exceeded the board)
    """
    banned = []
    if point.x > board.x - 1:
        banned.append(1)
    if point.x < 0:
        banned.append(2)
    if point.y > board.y - 1:
        banned.append(3)
    if point.y < 0:
        banned.append(0)
    if len(banned) == 0:
        return False, banned
    else:
        return True, banned


def length_out_of_bound(trace, board):
    """
    Counts length of the trace laying out of the board
    :param Trace trace:
    :param PCB_Board board:
    :return: length
    """
    _sum = 0
    for segment in trace.segments:
        points = segment.middle_points()
        for i in range(0, len(points) - 1):
            if point_out_of_bounds(points[i], board)[0] or point_out_of_bounds(points[i + 1], board)[0]:
                print("Out: ", points[i], points[i + 1])
                _sum += 1

    return _sum


def point_from_direction(direction, length, point):
    """
    Calculates coordinates and creates a point after moving 'length' units from point in 'direction'
    :param str direction: (0 - UP, 1 - LEFT, 2 - RIGHT, 3 - DOWN)
    :param int length: move length
    :param Point point: starting point
    :return: destination point
    """
    if direction == "UP":
        return Point(point.x, point.y - length)
    elif direction == "RIGHT":
        return Point(point.x + length, point.y)
    elif direction == "LEFT":
        return Point(point.x - length, point.y)
    elif direction == "DOWN":
        return Point(point.x, point.y + length)


def dist_from_target(point, trace):
    """
    Calculates the distance from the point to the trace's end point
    :param point:
    :param trace:
    :return: distance
    """
    return math.dist([point.x, point.y], [trace.pair.end.x, trace.pair.end.y])


class RandomIndividualGenerator:
    def __init__(self, board=None):
        self.board = board
        self.dir = {0: "UP", 1: "RIGHT", 3: "DOWN", 2: "LEFT"}
        self.individual = Individual(board)
        self.dict_tr = {}
        self.population = []

    def set_board(self, board):
        self.board = board
        self.individual.board = board

    def next_step(self, last_direction, trace):
        """
        Calculates the next point of the trace
        :param last_direction: last direction of the segment from the trace
        :param trace: trace which will be continued with created or extended segment
        :return: None
        """
        choices = [0, 1, 2, 3]
        okay = False
        if last_direction is not None:
            choices.remove(3 - last_direction)

        if len(trace.segments) == 0:
            end = trace.pair.beg
        else:
            end = trace.last_segment().end

        while not okay:

            okay = True
            rand_int = random.choice(choices)
            random_direction = self.dir[rand_int]

            new_point = point_from_direction(random_direction, 1, end)

            # if point_out_of_bounds(new_point, self.board)[0]:
            #     okay = False  # generate new point if the actual one is out of bounds

            dist = dist_from_target(new_point, trace)
            if dist > self.dict_tr[trace][0] and dist > self.dict_tr[trace][1] \
                    and end.x != trace.pair.end.x and end.y != trace.pair.end.y:
                # If distance from new point to the end of trace is bigger than from two previous points,
                # change direction
                okay = False

            if okay and last_direction is not None and random_direction == self.dir[last_direction]:
                # if new point can extend last segment, then do it
                extended_segment = Segment(trace.last_segment().beg, new_point)
                if self.individual.will_collide(extended_segment, trace) and (random.random() > 0.7):
                    # try to forbid the newly extended segment to collide with any trace
                    okay = False
                else:
                    # Extend the last segment
                    trace.extend_last_segment(new_point)
            elif okay:
                seg = Segment(end, new_point)
                if self.individual.will_collide(seg, trace) and (random.random() > 0.7):
                    # try to forbid the new segment to collide with any trace
                    okay = False
                else:
                    # Extend new segment
                    trace.add_segment(seg)
            if okay:
                # set two previous distances from the end of the trace
                self.dict_tr[trace][0] = self.dict_tr[trace][1]
                self.dict_tr[trace][1] = dist

    def generate(self):
        """
        Pseudo randomly generates new individual to solve the board
        :return: newly generated solution/individual
        """
        self.individual = Individual(self.board)
        for pair in self.board.pairs.values():
            # Initiate, crate traces for the individual
            tr = Trace(pair)
            self.dict_tr[tr] = [1000000, 100000]
            self.individual.add_trace(tr)
        counter = 0
        while not self.individual.all_traces_connected:
            # If not all traces are connected, then continue in turns
            for trace in list(trace for trace in self.individual.traces):
                if not trace.connected_pair:
                    last_direction = trace.last_direction()
                    # Calculate the next step
                    self.next_step(last_direction, trace)
                    # Set flag if all individual's traces are connected
                    self.individual.check_connected()
            counter += 1
        print("Counter:", counter)

        return self.individual
