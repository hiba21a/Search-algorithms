from Board import Board
from Square import Square

COLOR_BLACK = "black"
COLOR_WHITE = "white"
COLOR_RED = "red"
COLOR_GREEN = "green"
COLOR_BLUE ="blue"


def get_levels():
    levels = []
    level1_squares = [ 
        Square(0, 0, COLOR_BLACK),           
        Square(0, 1, COLOR_BLACK),            
        Square(0, 2, COLOR_BLACK),            
        Square(0, 3, COLOR_BLACK),            
        Square(0, 4, COLOR_WHITE),            

        Square(1, 0, COLOR_BLACK),            
        Square(2, 0, COLOR_BLACK),            
        Square(3, 0, COLOR_BLACK),            
        Square(4, 0, COLOR_BLACK),            

        Square(4, 1, COLOR_BLACK),            
        Square(4, 2, COLOR_BLACK),            
        Square(4, 3, COLOR_BLACK),            
        Square(4, 4, COLOR_BLACK),           

        Square(3, 4, COLOR_BLACK),            
        Square(2, 4, COLOR_BLACK),            
        Square(1, 3, COLOR_WHITE),            

        Square(1, 1, COLOR_WHITE),            
        Square(1, 2, COLOR_WHITE),            
        Square(1, 4, COLOR_BLACK),            

        Square(2, 2, COLOR_WHITE),            
        Square(2, 3, COLOR_WHITE),           
        Square(3, 1, COLOR_WHITE),            
        Square(3, 2, COLOR_WHITE),            
        Square(3, 3, COLOR_WHITE),            

        Square(3, 3, COLOR_WHITE),          
        Square(2, 1, COLOR_WHITE),  

        Square(2, 3, COLOR_GREEN, move=True),          
        Square(1, 2, COLOR_WHITE, is_goal=True, goal_color=COLOR_GREEN),  
    ]
    levels.append(Board(width=5, height=5, squares=level1_squares))

    level2_squares = [ 
        Square(0, 0, COLOR_BLACK),           
        Square(0, 1, COLOR_BLACK),            
        Square(0, 2, COLOR_BLACK),            
        Square(0, 3, COLOR_BLACK),            
        Square(0, 4, COLOR_WHITE),            

        Square(1, 0, COLOR_BLACK),            
        Square(2, 0, COLOR_BLACK),            
        Square(3, 0, COLOR_BLACK),            
        Square(4, 0, COLOR_BLACK),            

        Square(4, 1, COLOR_BLACK),            
        Square(4, 2, COLOR_BLACK),            
        Square(4, 3, COLOR_BLACK),            
        Square(4, 4, COLOR_BLACK),           

        Square(3, 4, COLOR_BLACK),            
        Square(2, 4, COLOR_BLACK),            
        Square(1, 3, COLOR_WHITE),            

        Square(1, 1, COLOR_WHITE),            
        Square(1, 2, COLOR_WHITE),            
        Square(1, 4, COLOR_BLACK),            

        Square(2, 2, COLOR_WHITE),            
        Square(2, 3, COLOR_WHITE),           
        Square(3, 1, COLOR_WHITE),            
        Square(3, 2, COLOR_WHITE),            
        Square(3, 3, COLOR_WHITE),            

        Square(3, 3, COLOR_RED, move=True),          
        Square(2, 1, COLOR_WHITE, is_goal=True, goal_color=COLOR_RED),  

        Square(2, 3, COLOR_GREEN, move=True),          
        Square(1, 2, COLOR_WHITE, is_goal=True, goal_color=COLOR_GREEN),  
    ]
    levels.append(Board(width=5, height=5, squares=level2_squares))
    
    return levels


