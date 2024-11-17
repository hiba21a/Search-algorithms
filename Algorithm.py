from collections import deque
from LogicGame import LogicGame

class Algorithm:
    @staticmethod
    def check_all_white_except_black(board):
        for square in board.squares:
            if square.color != 'black' and square.color != 'white': 
                return False
        return True
    @staticmethod
    def bfs(start_logic_game, game_instance):
        queue = deque([start_logic_game])  
        visited_list = []  
        visited_list.append(str(start_logic_game.board))  
        parent_map = {str(start_logic_game.board): None}  

        while queue:
            current_logic_game = queue.popleft()  
            current_board = current_logic_game.board  

            if  Algorithm.check_all_white_except_black(current_board):
                return Algorithm._path_board(parent_map, current_logic_game)

            for move, next_board in current_logic_game.next_state():
                state_key = str(next_board)  
                if state_key in visited_list:
                    continue  

                visited_list.append(state_key)

                next_logic_game = LogicGame(next_board)  
                parent_map[state_key] = current_logic_game  
                queue.append(next_logic_game)  
        return None 
     
    @staticmethod
    def dfs(start_logic_game, game_instance):
        stack = [start_logic_game]
        visited_list = []  
        visited_list.append(str(start_logic_game.board))  
        print(start_logic_game.board)
        parent_map = {str(start_logic_game.board): None}  
        while stack:
            current_logic_game = stack.pop()  
            current_board = current_logic_game.board  
            if  Algorithm.check_all_white_except_black(current_board):
                return Algorithm._path_board(parent_map, current_logic_game)

            for move, next_board in current_logic_game.next_state():
                state_key = str(next_board)  
                if state_key in visited_list:
                    continue  

                visited_list.append(state_key) 
                next_logic_game = LogicGame(next_board)  
                parent_map[state_key] = current_logic_game  
                stack.append(next_logic_game)  

        return None  
    
    @staticmethod
    def _path_board(parent_map, current_logic_game):
        path = []  
        while current_logic_game is not None:
            path.append(current_logic_game.board) 
            current_logic_game = parent_map.get(str(current_logic_game.board))  
        return path[::-1]  
