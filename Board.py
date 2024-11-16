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
        new_square = Square(original_x, original_y, self.COLOR_WHITE, moveable_on_it=True)
        self.net[original_y][original_x] = new_square

        square.x, square.y = new_x, new_y
        self.net[new_y][new_x] = square


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
                        else:
                            row += "R "
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
