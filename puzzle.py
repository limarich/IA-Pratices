import numpy as np
from collections import deque


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class Queue:
    def __init__(self):
        self.queue = deque()

    def add(self, node):
        self.queue.append(node)

    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.queue)

    def empty(self):
        return len(self.queue) == 0

    def remove(self):
        if self.empty():
            raise Exception("Fila vazia")
        else:
            node = self.queue.popleft()
            return node


class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.solution = None
        self.start_blank_piece_index = self.find_piece_index(start)
        self.goal_blank_piece_index = self.find_piece_index(goal)
        self.num_explored = 0
        self.explored = []

    def find_piece_index(self, puzzle):
        for row in range(3):
            for column in range(3):
                if puzzle[row][column] == 0:
                    return (row, column)

    def neighbors(self, state):
        mat, (row, column) = state
        results = []

        combinations = [(-1, 0, 'peça para cima'), (1, 0, 'peça para baixo'),
                        (0, -1, 'peça para esquerda'), (0, 1, 'peça para direita')]

        for direction_row, direction_column, action in combinations:
            new_row = direction_row + row
            new_column = direction_column + column

            if 0 <= new_row < 3 and 0 <= new_column < 3:
                mat1 = np.copy(mat)
                mat1[row, column] = mat1[new_row, new_column]
                mat1[new_row, new_column] = 0

                results.append((action, [mat1, (new_row, new_column)]))

        return results

    def print_solution(self):
        if self.solution is not None:
            actions, cells = self.solution
            print("Estado inicial:\n", self.start, "\n")
            print("Estado final:\n", self.goal, "\n")
            print("\nCombinações exploradas: ", self.num_explored, "\n")
            print("Solução:\n ")
            for action, cell in zip(actions, cells):
                print("Ação: ", action, "\n", cell[0], "\n")
            print("Objetivo atingido com sucesso!")
        else:
            print("Nenhuma solução encontrada.")

    def does_not_contain_state(self, state):
        for st in self.explored:
            if (st[0] == state[0]).all():
                return False
        return True

    def solve(self):
        start = Node(
            state=[self.start, self.start_blank_piece_index], parent=None, action=None)
        queue = Queue()
        queue.add(start)

        self.explored = []

        while True:
            if queue.empty():
                raise Exception('Fila vazia: Sem Solução!')

            node = queue.remove()
            self.num_explored += 1

            if (node.state[0] == self.goal).all():
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()
                self.solution = (actions,  cells)
                return

            self.explored.append(node.state)

            for action, state in self.neighbors(node.state):
                if not queue.contains_state(state) and self.does_not_contain_state(state):
                    child = Node(state=state, parent=node, action=action)
                    queue.add(child)


if __name__ == "__main__":
    # start = np.array([[1, 2, 5], [3, 4, 0], [6, 7, 8]])
    start = np.array([[1, 2, 5], [3, 0, 4], [6, 7, 8]])
    goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    p = Puzzle(start, goal)
    p.solve()
    p.print_solution()
