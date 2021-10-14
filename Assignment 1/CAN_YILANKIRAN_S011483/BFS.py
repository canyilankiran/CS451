from math import log
from math import ceil


class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):
        """ YOUR CODE HERE """
        while self.queue:
            state = self.queue.pop()
            self.visited[state.UID] = state
            self.counter +=1

            if state.is_equal(target):
                return True,self.counter, state.step

            for child in self.graph.reveal_neighbors(state):
                if not self.check_value_exist(self.visited, child):
                    self.queue.insert(0,child)



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
