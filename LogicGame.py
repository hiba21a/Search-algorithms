from Board import Board
from Square import Square

class LogicGame:
    def __init__(self, board):
        self.board = board
    COLOR_WHITE = "white"

    def move_up(self):
        new_board = self.board.cpoy_board()  
        movable_squares = []
        for square in new_board.squares:
            if square.move and not square.rgoal:  
                x, y = square.x, square.y
                if y > 0 and new_board.check_move(x, y - 1): 
                    movable_squares.append(square)
                    
        for square in movable_squares:
            x, y = square.x, square.y
            moved = 0
            original_x, original_y = x, y

            while y > 0 and new_board.check_move(x, y - 1): 
                y -= 1 
                tsquare = new_board.get_square(x, y)  

                moved += 1

                if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                        (tsquare and tsquare.move and tsquare != square):
                    if tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        square.color = self.COLOR_WHITE
                        tsquare.color = self.COLOR_WHITE 
                        tsquare.goal_color = self.COLOR_WHITE
                    break
            if moved > 0:
                new_board.update_position(square,original_x,original_y, x, y)
        return new_board

    def move_down(self):
        new_board = self.board.cpoy_board()  

        movable_squares = []
        for square in new_board.squares:
            if square.move and not square.rgoal:  
                x, y = square.x, square.y
                if y < self.board.height - 1 and new_board.check_move(x, y + 1):
                    movable_squares.append(square)
                    
        for square in movable_squares:
            x, y = square.x, square.y
            moved = 0
            original_x, original_y = x, y

            while y < self.board.height - 1 and new_board.check_move(x, y + 1):  
                y += 1  
                tsquare = new_board.get_square(x, y) 
                moved += 1

                if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                        (tsquare and tsquare.move and tsquare != square):
                    if tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        square.color = self.COLOR_WHITE
                        tsquare.color = self.COLOR_WHITE  
                        tsquare.goal_color = self.COLOR_WHITE
                    break

            if moved > 0:
                new_board.update_position(square,original_x,original_y, x, y)
                
        return new_board

    def move_right(self):
        new_board = self.board.cpoy_board()  

        
        movable_squares = []
        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                if x < self.board.width - 1 and new_board.check_move(x + 1, y): 
                    movable_squares.append(square)
                    
        for square in movable_squares:
            x, y = square.x, square.y
            moved = 0
            original_x, original_y = x, y

            while x < self.board.width - 1 and new_board.check_move(x + 1, y): 
                x += 1  
                tsquare = new_board.get_square(x, y)  

                moved += 1

                if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                        (tsquare and tsquare.move and tsquare != square):
                    if tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        square.color = self.COLOR_WHITE
                        tsquare.color = self.COLOR_WHITE  
                        tsquare.goal_color = self.COLOR_WHITE
                       
                    break

            if moved > 0:
                new_board.update_position(square,original_x,original_y, x, y)
        return new_board


    def move_left(self):
        new_board = self.board.cpoy_board() 
        
    
        movable_squares = []
        for square in new_board.squares:
            if square.move and not square.rgoal:  
                x, y = square.x, square.y
                if x > 0 and new_board.check_move(x - 1, y):  
                    movable_squares.append(square)  
                    
        for square in movable_squares:
            x, y = square.x, square.y
            moved = 0  
            original_x, original_y = x, y  
            
            while x > 0 and new_board.check_move(x - 1, y): 
                x -= 1
                
                tsquare = new_board.get_square(x, y)  

                moved += 1 

                if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                (tsquare and tsquare.move and tsquare != square):
                    if tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        square.color = self.COLOR_WHITE
                        tsquare.color = self.COLOR_WHITE 
                        tsquare.goal_color = self.COLOR_WHITE
                    break
            if moved > 0:
                new_board.update_position(square,original_x,original_y, x, y)

        return new_board
  
    def next_state(self):
        current_board = self.board.cpoy_board()  
        
        down_state = self.move_down()
        up_state = self.move_up()
        left_state = self.move_left()
        right_state = self.move_right()

        states = []
        movements = ["Up", "Down", "Left", "Right"]  
        for i in range(4): 
            movement = movements[i] 
            state = [up_state, down_state, left_state, right_state][i]  
            if state != current_board:
                states.append((movement, state))  
        
        return states 
