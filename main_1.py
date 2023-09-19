import numpy as np
import tkinter as tk
from puzzle_GUI import PuzzleGUI
from puzzle import Puzzle
import time


def main():
    # start = np.array([[1, 2, 5], [3, 4, 0], [6, 7, 8]])
    start = np.array([[1, 2, 5], [3, 0, 4], [6, 7, 8]])
    goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    root = tk.Tk()
    root.title("Resolvendo o 8-Puzzle")

    puzzle = Puzzle(start, goal)
    gui = PuzzleGUI(root, puzzle)

    start_time = time.time()
    puzzle.solve()
    puzzle.print_solution()
    end_time = time.time()

    if puzzle.solution:
        gui.update(start)
        root.update()
        root.after(1000)
        actions, states = puzzle.solution
        for state in states:
            gui.update(state[0])
            root.update()
            root.after(1000)

    print('Tempo decorrido:', end_time - start_time, 'segundos')

    root.mainloop()


if __name__ == "__main__":
    main()
