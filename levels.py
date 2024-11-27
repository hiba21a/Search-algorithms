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

        Square(2, 3, COLOR_GREEN, move=True ,moveable_on_it=False ),          
        Square(1, 2, COLOR_WHITE, is_goal=True, goal_color=COLOR_GREEN,moveable_on_it=True),  
    ]
    levels.append(Board(width=5, height=5, squares=level1_squares))

    level2_squares = [ 
        Square(0, 0, COLOR_BLACK),           
        Square(0, 1, COLOR_BLACK),            
        Square(0, 2, COLOR_BLACK),            
        Square(0, 3, COLOR_BLACK),            
        Square(0, 4, COLOR_WHITE,moveable_on_it=True),            

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
        Square(1, 3, COLOR_WHITE,moveable_on_it=True),            

        Square(1, 1, COLOR_WHITE,moveable_on_it=True),            
        Square(1, 2, COLOR_WHITE,moveable_on_it=True),            
        Square(1, 4, COLOR_BLACK),            

        Square(2, 2, COLOR_WHITE,moveable_on_it=True),            
        Square(2, 3, COLOR_WHITE,moveable_on_it=True),           
        Square(3, 1, COLOR_WHITE,moveable_on_it=True),            
        Square(3, 2, COLOR_WHITE,moveable_on_it=True),            
        Square(3, 3, COLOR_WHITE,moveable_on_it=True),            

        Square(3, 3, COLOR_RED, move=True),          
        Square(2, 1, COLOR_WHITE, is_goal=True, goal_color=COLOR_RED,moveable_on_it=True),  

        Square(2, 3, COLOR_GREEN, move=True),          
        Square(1, 2, COLOR_WHITE, is_goal=True, goal_color=COLOR_GREEN,moveable_on_it=True),  
    ]
    levels.append(Board(width=5, height=5, squares=level2_squares))

    level3_squares =[
        Square(0, 0, COLOR_BLACK),           
        Square(0, 1, COLOR_BLACK),           
        Square(0, 2, COLOR_BLACK),            
        Square(0, 3, COLOR_BLACK),            
        Square(0, 4, COLOR_BLACK),            


        Square(1, 0, COLOR_BLACK),            
        Square(2, 0, COLOR_BLACK),           
        Square(3, 0, COLOR_BLACK),            
        Square(4, 0, COLOR_BLACK),           
        Square(5, 0, COLOR_WHITE,moveable_on_it=True),            
        Square(6, 0, COLOR_WHITE,moveable_on_it=True),            
        Square(7, 0, COLOR_WHITE,moveable_on_it=True),            
        Square(8, 0, COLOR_WHITE,moveable_on_it=True),           

        Square(1, 1, COLOR_WHITE, is_goal=True, goal_color=COLOR_GREEN,moveable_on_it=True),  
        Square(2, 1, COLOR_WHITE,moveable_on_it=True),            
        Square(3, 1, COLOR_WHITE,moveable_on_it=True),            
        Square(4, 1, COLOR_WHITE,moveable_on_it=True),           
        Square(5, 1, COLOR_BLACK),            
        Square(6, 1, COLOR_WHITE,moveable_on_it=True),            
        Square(7, 1, COLOR_WHITE,moveable_on_it=True),            
        Square(8, 1, COLOR_WHITE,moveable_on_it=True),            

        Square(1, 2, COLOR_WHITE,moveable_on_it=True),  
        Square(2, 2, COLOR_WHITE,moveable_on_it=True),  
        Square(3, 2, COLOR_WHITE, is_goal=True, goal_color=COLOR_RED,moveable_on_it=True),  
        Square(4, 2, COLOR_WHITE,moveable_on_it=True),  
        Square(5, 2, COLOR_WHITE,moveable_on_it=True),  
        Square(6, 2, COLOR_BLACK),
        Square(7, 2, COLOR_BLACK),
        Square(8, 2, COLOR_BLACK),

        Square(1, 3, COLOR_WHITE,moveable_on_it=True),  
        Square(2, 3, COLOR_WHITE,moveable_on_it=True),  
        Square(3, 3, COLOR_WHITE,moveable_on_it=True),  
        Square(4, 3, COLOR_WHITE,moveable_on_it=True),  
        Square(5, 3, COLOR_WHITE,moveable_on_it=True),  
        Square(6, 3, COLOR_RED, move=True,moveable_on_it=False),           
        Square(7, 3, COLOR_GREEN, move=True,moveable_on_it=False),          
        Square(8, 3, COLOR_BLACK),

        Square(1, 4, COLOR_BLACK),            
        Square(2, 4, COLOR_BLACK),           
        Square(3, 4, COLOR_BLACK),            
        Square(4, 4, COLOR_BLACK),           
        Square(5, 4, COLOR_BLACK),            
        Square(6, 4, COLOR_BLACK),           
        Square(7, 4, COLOR_BLACK),           
        Square(8, 4, COLOR_BLACK),            

    ]

    levels.append(Board(width=9, height=5, squares=level3_squares))


    
    return levels


