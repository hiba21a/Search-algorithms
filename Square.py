class Square:
    def __init__(self, x, y, color, move=False, is_goal=False, goal_color=None):
        self.x = x
        self.y = y
        self.color = color
        self.move = move
        self.is_goal = is_goal
        self.goal_color = goal_color
        self.rgoal = False  

    