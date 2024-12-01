from collections import deque
from LogicGame import LogicGame
import heapq

class Algorithm:
    def __init__(self):
        pass

    @staticmethod
    def check_all_white_except_black(board):
        for square in board.squares:
            if square.color != 'black' and square.color != 'white': 
                return False
        return True

    @staticmethod
    def bfs(start_logic_game):
        queue = deque([start_logic_game])  
        visited_list = []  
        visited_list.append(str(start_logic_game.board))  
        parent_map = {str(start_logic_game.board): None}  

        while queue:
            current_logic_game = queue.popleft()  
            current_board = current_logic_game.board  

            if Algorithm.check_all_white_except_black(current_board):
                print(f"BFS visited nodes: {len(visited_list)}")
                return Algorithm._path_board(parent_map, current_logic_game)

            for move, next_board in current_logic_game.next_state():
                state_key = str(next_board)  
                if state_key in visited_list:
                    continue  

                visited_list.append(state_key)

                next_logic_game = LogicGame(next_board)  
                parent_map[state_key] = current_logic_game  
                queue.append(next_logic_game) 

        print(f"BFS visited nodes: {len(visited_list)}")
        return None

    @staticmethod
    def dfs(start_logic_game):
        stack = [start_logic_game]
        visited_list = []  
        visited_list.append(str(start_logic_game.board))  
        parent_map = {str(start_logic_game.board): None}  

        while stack:
            current_logic_game = stack.pop()  
            current_board = current_logic_game.board  

            if Algorithm.check_all_white_except_black(current_board):
                print(f"DFS visited nodes: {len(visited_list)}")
                return Algorithm._path_board(parent_map, current_logic_game)

            for move, next_board in current_logic_game.next_state():
                state_key = str(next_board)  
                if state_key in visited_list:
                    continue  

                visited_list.append(state_key) 
                next_logic_game = LogicGame(next_board)  
                parent_map[state_key] = current_logic_game  
                stack.append(next_logic_game)  

        print(f"DFS visited nodes: {len(visited_list)}")
        return None

    @staticmethod
    def recursivedfs(current_logic_game, visited=None, parent_map=None):
        if visited is None:
            visited = set()
        if parent_map is None:
            parent_map = {str(current_logic_game.board): None}

        if Algorithm.check_all_white_except_black(current_logic_game.board):
            print(f"Recursive DFS visited nodes: {len(visited)}")
            return Algorithm._path_board(parent_map, current_logic_game)

        state_key = str(current_logic_game.board)
        visited.add(state_key)

        for move, next_board in current_logic_game.next_state():
            next_state_key = str(next_board)
            if next_state_key in visited:
                continue

            next_logic_game = LogicGame(next_board)
            parent_map[next_state_key] = current_logic_game
            result = Algorithm.recursivedfs(next_logic_game, visited, parent_map)
            if result:
                return result

        return None

    @staticmethod
    def ucs(start_logic_game):
        class PriorityQueueItem:
            def __init__(self, cost, game_state):
                self.cost = cost
                self.game_state = game_state

            def __lt__(self, other):
                return self.cost < other.cost  
        priority_queue = []
        heapq.heappush(priority_queue, PriorityQueueItem(0, start_logic_game))  

        visited = set()  
        parent_map = {str(start_logic_game.board): None}  

        while priority_queue:
            current_item = heapq.heappop(priority_queue) 
            current_cost = current_item.cost
            current_logic_game = current_item.game_state
            if Algorithm.check_all_white_except_black(current_logic_game.board):
                print(f"UCS visited nodes: {len(visited)}")
                return Algorithm._path_board(parent_map, current_logic_game)

            state_key = str(current_logic_game.board)
            if state_key in visited:
                continue
            visited.add(state_key)
            for move, next_board in current_logic_game.next_state():
                next_state_key = str(next_board)
                if next_state_key in visited:
                    continue
                new_cost = current_cost + 1  
                next_logic_game = LogicGame(next_board)
                if next_state_key not in visited or new_cost < current_cost:
                    heapq.heappush(priority_queue, PriorityQueueItem(new_cost, next_logic_game))
                    parent_map[next_state_key] = current_logic_game

        print(f"UCS visited nodes: {len(visited)}")
        return None

    @staticmethod
    def _path_board(parent_map, current_logic_game):
        path = []  
        while current_logic_game is not None:
            path.append(current_logic_game.board) 
            current_logic_game = parent_map.get(str(current_logic_game.board))  
        return path[::-1]  
    
    def uniform_cost_search(start_logic_game):
        priority_queue = heapq.heappush(priority_queue,(0,start_logic_game))
        visited_list = []  
        visited_list.append(str(start_logic_game.board))  
        parent_map = {str(start_logic_game.board): None}  

        while priority_queue :
            current_cost,current_logic_game= heapq.heappop(priority_queue) 
            current_board = current_logic_game.board  

            if  Algorithm.check_all_white_except_black(current_board):
                return Algorithm._path_board(parent_map, current_logic_game)
    
    def heuristic(self):
        manhat = 0
        for square in self.board.squares:
            if square.move and not square.rgoal:  
                goal_square = self.board.get_goal_for_square(square)
                if goal_square:
                    manhat += abs(square.x - goal_square.x) + abs(square.y - goal_square.y)
        print(manhat)
        return manhat
    
    @staticmethod
    def a_star(start_logic_game):
        class PriorityQueueItem:
            def __init__(self, cost, heuristic, game_state):
                self.cost = cost
                self.heuristic = heuristic
                self.total_cost = cost + heuristic  
                self.game_state = game_state

            def __lt__(self, other):
                return self.total_cost < other.total_cost  

        priority_queue = []
        start_heuristic = Algorithm.heuristic(start_logic_game)  
        heapq.heappush(priority_queue, PriorityQueueItem(0, start_heuristic, start_logic_game))

        visited = set()
        parent_map = {str(start_logic_game.board): None}

        while priority_queue:
            current_item = heapq.heappop(priority_queue)
            current_cost = current_item.cost
            current_logic_game = current_item.game_state

            if Algorithm.check_all_white_except_black(current_logic_game.board):
                print(f"A* visited nodes: {len(visited)}")
                return Algorithm._path_board(parent_map, current_logic_game)

            state_key = str(current_logic_game.board)
            if state_key in visited:
                continue
            visited.add(state_key)

            for move, next_board in current_logic_game.next_state():
                next_logic_game = LogicGame(next_board)
                next_state_key = str(next_board)
                if next_state_key in visited:
                    continue

                move_cost = current_cost + 1  
                heuristic = Algorithm.heuristic(next_logic_game) 
                heapq.heappush(priority_queue, PriorityQueueItem(move_cost, heuristic, next_logic_game))
                parent_map[next_state_key] = current_logic_game

        print(f"A* visited nodes: {len(visited)}")
        return None
