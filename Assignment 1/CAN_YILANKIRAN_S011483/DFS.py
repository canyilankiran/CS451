


class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        root = self.stack[0]
        self.visited[root.UID] = root
        while self.stack:
            state = self.stack.pop()
            self.counter += 1
            self.visited[state.UID] = state

            if state.is_equal(target):
                return True, self.counter, state.step

            for child in self.graph.reveal_neighbors(state):
                if not self.check_value_exist(self.visited, child):
                    self.stack.append(child)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def check_value_exist(self, test_dict, value):
        boolean = False
        if test_dict:
            for key, val in test_dict.items():
                if val.is_equal(value):
                    boolean = True

        return boolean

