from LogicGame import LogicGame
from Game import Game
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    
    print("Current State:")
    print(game.board)
    print("---------------------------------------------------------")
    
    game_logic = LogicGame(game.board)
    
    next_states = game_logic.next_state()


    root.mainloop()
