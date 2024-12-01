import copy
from Square import Square

class Board:
    COLOR_BLACK = "black"
    COLOR_WHITE = "white"
    COLOR_RED = "red"
    COLOR_GREEN = "green"
    COLOR_BLUE = "blue"

    def __init__(self, width, height, squares):
        self.width = width
        self.height = height
        
        self.net = []  
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Square(x, y, self.COLOR_WHITE, moveable_on_it=True))
            self.net.append(row)
        
        self.squares = squares
        for square in squares:
            self.net[square.y][square.x] = square
   
    def __eq__(self, other):
            if not isinstance(other, Board):
                return False
            
            if self.width != other.width or self.height != other.height:
                return False
            
            for i in range(len(self.squares)):  
                if self.squares[i] != other.squares[i]: 
                    return False

            return True
    
    def get_square(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.net[y][x]
        return None
    def get_goal_for_square(self, square):
        for sq in self.squares:
            if sq.is_goal and sq.goal_color == square.color:
                return sq
        return None
    def cpoy_board(self):
        new_squares = [copy.deepcopy(square) for square in self.squares]
        new_board = Board(self.width, self.height, new_squares)
        return new_board

    def check_move(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            tsquare = self.net[y][x]
            return tsquare.color == self.COLOR_WHITE or tsquare.moveable_on_it == True
        return False
        
    def update_position(self, square, original_x, original_y, new_x, new_y):
        original_square = self.net[original_y][original_x]
        if original_square.is_goal:  
            self.net[original_y][original_x] = Square(
                original_x, original_y, self.COLOR_WHITE, 
                is_goal=True, 
                goal_color=original_square.goal_color, 
                moveable_on_it=True
            )
        else:
            self.net[original_y][original_x] = Square(
                original_x, original_y, self.COLOR_WHITE, moveable_on_it=True
            )

        target_square = self.net[new_y][new_x]
        if target_square.is_goal:
            square.is_goal = True
            square.goal_color = target_square.goal_color
        else:
            square.is_goal = False
            square.goal_color = None

        square.x, square.y = new_x, new_y
        self.net[new_y][new_x] = square


    def calculate_cost(self, other_board):
        cost = 0
        for square in self.squares:
            other_square = next((s for s in other_board.squares if s.x == square.x and s.y == square.y), None)
            if other_square:
                cost += abs(square.x - other_square.x) + abs(square.y - other_square.y)
        return cost
    
    def __str__(self):
        result = ""
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                square = self.net[y][x]
                if square:
                    if square.color == self.COLOR_BLACK:
                        row += "# "  
                    elif square.color == self.COLOR_WHITE and not square.is_goal:
                        row += "- " 
                    elif square.move:
                        if square.color == self.COLOR_GREEN:
                            row += "G "
                        elif square.color == self.COLOR_BLUE:
                            row += "B "
                        elif square.color == self.COLOR_RED:
                            row += "R "
                        else:
                            row += "- " 
                    elif square.is_goal:
                        if square.goal_color == self.COLOR_GREEN:
                            row += "g "
                        elif square.goal_color == self.COLOR_BLUE:
                            row += "b "
                        elif square.goal_color == self.COLOR_RED:
                            row += "r "
                        elif square.goal_color == self.COLOR_WHITE:
                            row += "- "
            result += row.strip() + "\n"
        return result.strip()
