# from Board import Board
# class LogicGame:
#     def __init__(self, board):
#         self.board = board

#     def move_up(self):
#         new_board = self.board.cpoy_board()
#         for square in new_board.squares:
#             if square.move and not square.rgoal:
#                 x, y = square.x, square.y
#                 while y > 0 and new_board.check_move(x, y - 1):
#                     y -= 1
#                     tsquare = new_board.get_square(x, y)
#                     if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
#                        (tsquare and tsquare.move and tsquare != square):
#                         if tsquare.is_goal and tsquare.goal_color == square.color:
#                             square.rgoal = True
#                             tsquare.color = Board.COLOR_WHITE
#                             tsquare.goal_color = Board.COLOR_WHITE
#                         break
#                 new_board.update_position(square, x, y)
#         return new_board

#     def move_down(self):
#         new_board = self.board.cpoy_board()
#         for square in new_board.squares:
#             if square.move and not square.rgoal:
#                 x, y = square.x, square.y
#                 while y < self.board.height - 1 and new_board.check_move(x, y + 1):
#                     y += 1
#                     tsquare = new_board.get_square(x, y)
#                     if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
#                        (tsquare and tsquare.move and tsquare != square):
#                         if tsquare.is_goal and tsquare.goal_color == square.color:
#                             square.rgoal = True
#                             tsquare.color = Board.COLOR_WHITE
#                             tsquare.goal_color = Board.COLOR_WHITE
#                         break
#                 new_board.update_position(square, x, y)
#         return new_board

#     def move_left(self):
#         new_board = self.board.cpoy_board()
#         for square in new_board.squares:
#             if square.move and not square.rgoal:
#                 x, y = square.x, square.y
#                 while x > 0 and new_board.check_move(x - 1, y):
#                     x -= 1
#                     tsquare = new_board.get_square(x, y)
#                     if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
#                        (tsquare and tsquare.move and tsquare != square):
#                         if tsquare.is_goal and tsquare.goal_color == square.color:
#                             square.rgoal = True
#                             tsquare.color = Board.COLOR_WHITE
#                             tsquare.goal_color = Board.COLOR_WHITE
#                         break
#                 new_board.update_position(square, x, y)
#         return new_board

#     def move_right(self):
#         new_board = self.board.cpoy_board()
#         for square in new_board.squares:
#             if square.move and not square.rgoal:
#                 x, y = square.x, square.y
#                 while x < self.board.width - 1 and new_board.check_move(x + 1, y):
#                     x += 1
#                     tsquare = new_board.get_square(x, y)
#                     if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
#                        (tsquare and tsquare.move and tsquare != square):
#                         if tsquare.is_goal and tsquare.goal_color == square.color:
#                             square.rgoal = True
#                             tsquare.color = Board.COLOR_WHITE
#                             tsquare.goal_color = Board.COLOR_WHITE
#                         break
#                 new_board.update_position(square, x, y)
#         return new_board
    
#     def next_state(self):
#             states = []
#             up_state = self.move_up()
#             down_state = self.move_down()
#             left_state = self.move_left()
#             right_state = self.move_right()

#             for state in [up_state, down_state, left_state, right_state]:
#                 if state not in states:
#                     states.append(state)

#             print("\nPossible States:")
#             counter = 1
#             for state in states:
#                 print(f"\nState {counter}:")
#                 print(state)  
#                 counter += 1  
#             print("---------------------------------------------------------")
        
#             return states
from Board import Board

class LogicGame:
    def __init__(self, board):
        self.board = board

    def can_move_with_nearby_piece(self, square, next_x, next_y, dx, dy):
        """ Helper to check if movement is allowed when another piece is nearby. """
        nearby_square = self.board.get_square(next_x, next_y)
        
        # Check if there's a neighboring piece and if the cell after it is empty.
        if nearby_square and nearby_square.color in [Board.COLOR_RED, Board.COLOR_GREEN]:
            after_next_x, after_next_y = next_x + dx, next_y + dy
            return self.board.check_move(after_next_x, after_next_y)
        return True

    def move_up(self):
        new_board = self.board.cpoy_board()
        
        # Track initial positions of R and G
        r_position = None
        g_position = None
        for square in new_board.squares:
            if square.color == Board.COLOR_RED:
                r_position = (square.x, square.y)
            elif square.color == Board.COLOR_GREEN:
                g_position = (square.x, square.y)

        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while y > 0 and new_board.check_move(x, y - 1):
                    
                    # Prevent R and G from moving into each other's initial position
                    if square.color == Board.COLOR_RED and (x, y - 1) == g_position:
                        break
                    if square.color == Board.COLOR_GREEN and (x, y - 1) == r_position:
                        break
                    
                    # Move up one step
                    y -= 1
                    
                    # Check if square reached its goal
                    tsquare = new_board.get_square(x, y)
                    if tsquare and tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        # Mark the goal square as reached, but leave it as a valid moveable space
                        tsquare.color = Board.COLOR_WHITE
                        tsquare.goal_color = Board.COLOR_WHITE
                        break
                
                # Update square's position
                new_board.update_position(square, x, y)
        
        return new_board

    def move_down(self):
        new_board = self.board.cpoy_board()
        
        # Track initial positions of R and G
        r_position = None
        g_position = None
        for square in new_board.squares:
            if square.color == Board.COLOR_RED:
                r_position = (square.x, square.y)
            elif square.color == Board.COLOR_GREEN:
                g_position = (square.x, square.y)

        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while y < self.board.height - 1 and new_board.check_move(x, y + 1):
                    
                    # Prevent R and G from moving into each other's initial position
                    if square.color == Board.COLOR_RED and (x, y + 1) == g_position:
                        break
                    if square.color == Board.COLOR_GREEN and (x, y + 1) == r_position:
                        break
                    
                    # Move down one step
                    y += 1
                    
                    # Check if square reached its goal
                    tsquare = new_board.get_square(x, y)
                    if tsquare and tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        # Mark the goal square as reached, but leave it as a valid moveable space
                        tsquare.color = Board.COLOR_WHITE
                        tsquare.goal_color = Board.COLOR_WHITE
                        break
                
                # Update square's position
                new_board.update_position(square, x, y)
        
        return new_board

    def move_left(self):
        new_board = self.board.cpoy_board()
        
        # Track initial positions of R and G
        r_position = None
        g_position = None
        for square in new_board.squares:
            if square.color == Board.COLOR_RED:
                r_position = (square.x, square.y)
            elif square.color == Board.COLOR_GREEN:
                g_position = (square.x, square.y)

        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while x > 0 and new_board.check_move(x - 1, y):
                    
                    # Prevent R and G from moving into each other's initial position
                    if square.color == Board.COLOR_RED and (x - 1, y) == g_position:
                        break
                    if square.color == Board.COLOR_GREEN and (x - 1, y) == r_position:
                        break
                    
                    # Move left one step
                    x -= 1
                    
                    # Check if square reached its goal
                    tsquare = new_board.get_square(x, y)
                    if tsquare and tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        # Mark the goal square as reached, but leave it as a valid moveable space
                        tsquare.color = Board.COLOR_WHITE
                        tsquare.goal_color = Board.COLOR_WHITE
                        break
                
                # Update square's position
                new_board.update_position(square, x, y)
        
        return new_board

    def move_right(self):
        new_board = self.board.cpoy_board()
        
        # Track initial positions of R and G
        r_position = None
        g_position = None
        for square in new_board.squares:
            if square.color == Board.COLOR_RED:
                r_position = (square.x, square.y)
            elif square.color == Board.COLOR_GREEN:
                g_position = (square.x, square.y)

        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while x < self.board.width - 1 and new_board.check_move(x + 1, y):
                    
                    # Prevent R and G from moving into each other's initial position
                    if square.color == Board.COLOR_RED and (x + 1, y) == g_position:
                        break
                    if square.color == Board.COLOR_GREEN and (x + 1, y) == r_position:
                        break
                    
                    # Move right one step
                    x += 1
                    
                    # Check if square reached its goal
                    tsquare = new_board.get_square(x, y)
                    if tsquare and tsquare.is_goal and tsquare.goal_color == square.color:
                        square.rgoal = True
                        # Mark the goal square as reached, but leave it as a valid moveable space
                        tsquare.color = Board.COLOR_WHITE
                        tsquare.goal_color = Board.COLOR_WHITE
                        break
                
                # Update square's position
                new_board.update_position(square, x, y)
        
        return new_board

    def next_state(self):
        states = []
        up_state = self.move_up()
        down_state = self.move_down()
        left_state = self.move_left()
        right_state = self.move_right()

        for state in [up_state, down_state, left_state, right_state]:
            if state not in states:
                states.append(state)

        print("\nPossible States:")
        counter = 1
        for state in states:
            print(f"\nState {counter}:")
            print(state)  
            counter += 1  
        print("---------------------------------------------------------")
    
        return states
