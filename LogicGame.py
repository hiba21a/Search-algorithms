from Board import Board
class LogicGame:
    def __init__(self, board):
        self.board = board

    def move_up(self):
        new_board = self.board.cpoy_board()
        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while y > 0 and new_board.check_move(x, y - 1):
                    y -= 1
                    tsquare = new_board.get_square(x, y)
                    if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                       (tsquare and tsquare.move and tsquare != square):
                        if tsquare.is_goal and tsquare.goal_color == square.color:
                            square.rgoal = True
                            tsquare.color = Board.COLOR_WHITE
                            tsquare.goal_color = Board.COLOR_WHITE
                        break
                new_board.update_position(square, x, y)
        return new_board

    def move_down(self):
        new_board = self.board.cpoy_board()
        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while y < self.board.height - 1 and new_board.check_move(x, y + 1):
                    y += 1
                    tsquare = new_board.get_square(x, y)
                    if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                       (tsquare and tsquare.move and tsquare != square):
                        if tsquare.is_goal and tsquare.goal_color == square.color:
                            square.rgoal = True
                            tsquare.color = Board.COLOR_WHITE
                            tsquare.goal_color = Board.COLOR_WHITE
                        break
                new_board.update_position(square, x, y)
        return new_board

    def move_left(self):
        new_board = self.board.cpoy_board()
        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while x > 0 and new_board.check_move(x - 1, y):
                    x -= 1
                    tsquare = new_board.get_square(x, y)
                    if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                       (tsquare and tsquare.move and tsquare != square):
                        if tsquare.is_goal and tsquare.goal_color == square.color:
                            square.rgoal = True
                            tsquare.color = Board.COLOR_WHITE
                            tsquare.goal_color = Board.COLOR_WHITE
                        break
                new_board.update_position(square, x, y)
        return new_board

    def move_right(self):
        new_board = self.board.cpoy_board()
        for square in new_board.squares:
            if square.move and not square.rgoal:
                x, y = square.x, square.y
                while x < self.board.width - 1 and new_board.check_move(x + 1, y):
                    x += 1
                    tsquare = new_board.get_square(x, y)
                    if (tsquare and tsquare.is_goal and tsquare.goal_color == square.color) or \
                       (tsquare and tsquare.move and tsquare != square):
                        if tsquare.is_goal and tsquare.goal_color == square.color:
                            square.rgoal = True
                            tsquare.color = Board.COLOR_WHITE
                            tsquare.goal_color = Board.COLOR_WHITE
                        break
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