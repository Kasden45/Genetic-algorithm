from Generator import point_out_of_bounds, length_out_of_bound


class Fitness:
    def __init__(self, col_weight, tot_len_weight, tot_seg_weight, out_of_bounds_weight=1, len_out_of_bounds_weight=1):
        """

        :param col_weight:
        :param tot_len_weight:
        :param tot_seg_weight:
        :param out_of_bounds_weight:
        :param len_out_of_bounds_weight:
        """
        self.collisions_weight = col_weight
        self.total_length_weight = tot_len_weight
        self.total_segments_weight = tot_seg_weight
        self.out_of_bounds_weight = out_of_bounds_weight
        self.len_out_of_bounds_weight = len_out_of_bounds_weight

        pass

    def collisions(self, individual):
        """
        Counts collisions made by individual 's traces
        :param individual:
        :return: onumber of collisions
        """
        all_points = []
        for trace in individual.traces:
            all_points.extend(trace.trace_route())
        return len(set(individual.all_collisions()))

    def out_of_bounds(self, individual):
        """
        Counts how many traces went out of bounds of the board
        :param individual:
        :return: number of 'out of bounds' traces
        """
        traces_out_of_bounds = 0
        for trace in individual.traces:
            if any(point for point in trace.trace_route() if point_out_of_bounds(point, individual.board)[0]):
                traces_out_of_bounds += 1

        return traces_out_of_bounds

    def length_out_of_bounds(self, individual):
        """
        Counts the length of 'out of bounds' traces
        :param individual:
        :return: the length of 'out of bounds' traces
        """
        total_out_of_bounds = 0
        for trace in individual.traces:
            total_out_of_bounds += length_out_of_bound(trace, individual.board)

        return total_out_of_bounds

    def total_length(self, individual):
        """
        Counts the length of all segments present on the individual's board
        :param individual:
        :return: total length of segments
        """
        _sum = 0
        for trace in individual.traces:
            _sum += sum(len(segment) for segment in trace.segments)
        return _sum

    def total_segments(self, individual):
        """
        Counts how many segments are present on the individual's board
        :param individual:
        :return: number of segments
        """
        _sum = 0
        for trace in individual.traces:
            _sum += len(trace.segments)
        return sum(len(trace.segments) for trace in individual.traces)

    def count_fitness(self, individual):
        """
        Calculates individual's score
        :param individual:
        :return: score
        """
        return self.collisions(individual) * self.collisions_weight + \
               self.total_length(individual) * self.total_length_weight + \
               self.total_segments(individual) * self.total_segments_weight + \
               self.out_of_bounds(individual) * self.out_of_bounds_weight +\
               self.length_out_of_bounds(individual) * self.len_out_of_bounds_weight
