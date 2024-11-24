import tkinter as tk
from tkinter import messagebox
from LogicGame import LogicGame
from levels import get_levels
from Algorithm import Algorithm

SQUARE_SIZE = 50

class Game:

    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=10 * SQUARE_SIZE, height=10 * SQUARE_SIZE)
        self.canvas.pack()
        
        self.levels = get_levels()
        self.current_level_index = 1
        self.board = self.levels[self.current_level_index]
        self.draw_board()

        self.root.bind("<Up>", self.handle_key_up)
        self.root.bind("<Down>", self.handle_key_down)
        self.root.bind("<Left>", self.handle_key_left)
        self.root.bind("<Right>", self.handle_key_right)
        self.root.bind("<n>", self.show_next_states)
        self.root.bind("<s>", self.solve_with_bfs)
        self.root.bind("<d>", self.solve_with_dfs)

    def handle_key_up(self, event):
        self.move_and_check('up')

    def handle_key_down(self, event):
        self.move_and_check('down')

    def handle_key_left(self, event):
        self.move_and_check('left')

    def handle_key_right(self, event):
        self.move_and_check('right')

    def load_level(self, level_index):
        if level_index < len(self.levels):
            self.board = self.levels[level_index]  
            self.draw_board()
        else:
            messagebox.showinfo("Congratulations", "You've completed all levels!")
            self.root.quit()

    def draw_board(self):
        self.canvas.delete("all")
        for square in self.board.squares:
            x1, y1 = square.x * SQUARE_SIZE, square.y * SQUARE_SIZE
            x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=square.color, outline="black")
            if square.is_goal:
                self.canvas.create_rectangle(x1 + 3, y1 + 3, x2 - 3, y2 - 3, outline=square.goal_color, width=2)

    def move_and_check(self, direction):
        logic = LogicGame(self.board) 

        if direction == 'up':
            new_board = logic.move_up()  
        elif direction == 'down':
            new_board = logic.move_down()  
        elif direction == 'left':
            new_board = logic.move_left()  
        elif direction == 'right':
            new_board = logic.move_right() 

        self.board = new_board  
        self.draw_board()  

        if self.check_success():
            self.show_success_message()

    def check_success(self):
        return all(square.rgoal for square in self.board.squares if square.move)

    def show_success_message(self):
        messagebox.showinfo("Success", "Level Completed!")
        self.current_level_index += 1
        self.load_level(self.current_level_index)

    def show_next_states(self, event):
        logic = LogicGame(self.board)
        
        next_states = logic.next_state()
        for movement, state in next_states:
            print(f"Movement: {movement}")
            print(state)

    def solve_with_bfs(self, event):
        logic = LogicGame(self.board)
        algorithm = Algorithm()

        solution_path = algorithm.bfs(logic, self) 

        if solution_path:
            for step, state in enumerate(solution_path):
                print(f"\nStep {step + 1}:")
                print(state)
                print("-----------------------")
            messagebox.showinfo("Solution Found")
        else:
            messagebox.showinfo("No Solution")

    def solve_with_dfs(self, event):
            logic = LogicGame(self.board)
            algorithm = Algorithm()

            solution_path = algorithm.dfs(logic, self) 

            if solution_path:
                for step, state in enumerate(solution_path):
                    print(f"\nStep {step + 1}:")
                    print(state)
                    print("-----------------------")

                messagebox.showinfo("Solution Found")
            else:
                messagebox.showinfo("No Solution")
