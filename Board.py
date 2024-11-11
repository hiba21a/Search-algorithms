import copy
from Square import Square

class Board:

    COLOR_BLACK = "black"
    COLOR_WHITE = "white"
    COLOR_RED = "red"
    COLOR_GREEN = "green"
    COLOR_BLUE ="blue"

    def __init__(self, width, height, squares):
        self.width = width
        self.height = height
       
        self.net = [] 
        for i in range(height):  
            row = []
            for j in range(width):
                row.append(None)
            self.net.append(row)   
        self.squares = squares

        for square in squares:
            self.net[square.y][square.x] = square

    def get_square(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.net[y][x]
        return None

    def cpoy_board(self):
        new_squares = [copy.deepcopy(square) for square in self.squares]
        new_board = Board(self.width, self.height, new_squares)
        print(new_board)
        return new_board

    def check_move(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            tsquare = self.net[y][x]
            return tsquare is None or tsquare.color == "white"
        return False

    def update_position(self, square, new_x, new_y):
        """Update the position of a square on the board."""
        self.net[square.y][square.x] = None  
        square.x, square.y = new_x, new_y  
        self.net[new_y][new_x] = square 

    def __str__(self):
        result = ""
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                square = self.net[y][x]
                if square:
                    if square.color == "black":
                        row += "# "  
                    elif square.color == "white" and not square.is_goal:
                        row += "__"  
                    elif square.move:
                        if square.color == "green":
                            row += "G "  
                        elif square.color == "blue":
                            row += "B "  
                        else:
                            row += "R "  
                    elif square.is_goal:
                        if square.goal_color == "green":
                            row += "g "
                        elif square.goal_color == "blue":
                            row += "b " 
                        else:
                            row += "r "  
            result += row.strip() + "\n"
        return result.strip()

   