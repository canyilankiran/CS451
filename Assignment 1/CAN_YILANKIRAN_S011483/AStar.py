import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        self.queue.put((self.root.step, self.root, int(self.root.UID)))
        self.visited[self.root.UID] = self.root
        while not self.queue.empty():
            cost,state,nodeID = self.queue.get()
            self.visited[state.UID] = state
            self.counter += 1

            if state.is_equal(target):
                return True, self.counter, state.step

            for child in self.graph.reveal_neighbors(state):
                if not self.check_value_exist(self.visited,child):
                    total_cost = child.step + self.manhattan_distance(child, target)
                    self.queue.put((total_cost, child, child.UID))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist

    def check_value_exist(self, test_dict, value):
        boolean = False
        for key, val in test_dict.items():
            if val.is_equal(value):
                boolean = True

        return boolean

