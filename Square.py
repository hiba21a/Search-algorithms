class Square:
    def __init__(self, x, y, color, move=False, is_goal=False, goal_color=None ,moveable_on_it=False):
        self.x = x
        self.y = y
        self.color = color
        self.move = move
        self.moveable_on_it = moveable_on_it
        self.is_goal = is_goal
        self.goal_color = goal_color
        self.rgoal = False  

    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        
        return (self.x == other.x and
                self.y == other.y and
                self.color == other.color and
                self.moveable_on_it == other.moveable_on_it and
                self.is_goal == other.is_goal and
                self.goal_color == other.goal_color)

   