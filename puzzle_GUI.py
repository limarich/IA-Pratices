import tkinter as tk
import numpy as np


class PuzzleGUI:
    def __init__(self, root, puzzle):
        self.root = root
        self.puzzle = puzzle
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()
        self.draw_puzzle(puzzle.start)

    def draw_puzzle(self, state):
        self.canvas.delete("all")
        matrix = state
        for row in range(3):
            for col in range(3):
                value = matrix[row][col]
                x1, y1 = col * 100, row * 100
                x2, y2 = x1 + 100, y1 + 100
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="lightblue")
                self.canvas.create_text(
                    x1 + 50, y1 + 50, text=str(value), font=("Helvetica", 24))

    def update(self, state):
        self.draw_puzzle(state)
        self.root.update()
