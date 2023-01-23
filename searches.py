import sys
import heapq
from node import Node
from collections import deque

# Array of tuples. Implements heapq
# Use id(node) to resolve ties in priority  
class PriorityQueue:  
    def __init__(self):
        self.items = []
        
    def __contains__(self, node):
        for item in self.items:
            if item[2].board == node.board:
                return True
        return False
    
    def push(self, priority, node):
        heapq.heappush(self.items, (priority, id(node), node))
    
    def pop(self):
        return heapq.heappop(self.items)[-1]
    
    def replace(self, priority, node):
        for item in self.items:
            if node.board == item[2].board: 
                if priority < item[0]:
                    self.items.remove(item)
                    self.push(priority, node)
                return
            
    def size(self):
        return len(self.items)

class Search:
    
    def __init__(self, time=0, space=0, solution_path=[]):
        self.time = time
        self.space = space
        self.solution_path = solution_path
        
    def display_solution(self, curr_node):  
        self.solution_path.append(curr_node)
        total_cost = curr_node.path_cost               
        while curr_node.parent is not None:
            self.solution_path.append(curr_node.parent)
            curr_node = curr_node.parent
        self.solution_path.reverse()
                     
        # for node in self.solution_path:
        #     if node.parent:
        #         print(node.action, ", Cost = ", node.move_cost, ", Path cost = ", node.path_cost)
        #     print(node.board)
            
        print("\nSOLUTION\n"
              f" Total cost = {total_cost}\n"
              f" Length = {len(self.solution_path) - 1}\n"
              f" Time = {self.time}\n"
              f" Space = {self.space}\n")         
        sys.exit("Solution found")
        
        
    def bfs(self, board):
        queue = deque()
        visited = set()     
        queue.append(Node(board))
        
        while len(queue) > 0:
            if len(queue) > self.space: self.space = len(queue) # Space measure
            curr_node = queue.popleft()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): 
                self.display_solution(curr_node)    
                                          
            children = curr_node.get_children()
            for child in children:
                if child.board not in visited:
                    if child not in queue:
                        queue.append(child)
                    else:
                        incumbent = queue.index(child)
                        if child.path_cost < queue[incumbent].path_cost:
                            queue[incumbent] = child
                            
                        
        sys.exit("No solution")        
        
    def dfs(self, board):
        stack = deque()
        visited = set()
        stack.append(Node(board))
        
        while len(stack) > 0:
            if len(stack) > self.space: self.space = len(stack) # Space measure
            curr_node = stack.pop()
            self.time += 1 # Time measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal():
                self.display_solution(curr_node)
                
            children = curr_node.get_children()
            for child in children:
                if child.board not in visited:
                    if child not in stack:
                        stack.append(child)
                    else:
                        incumbent = stack.index(child)
                        if child.path_cost < stack[incumbent].path_cost:
                            stack[incumbent] = child              
        sys.exit("No solution")            
        

    def ucs(self, board):
        pq = PriorityQueue()
        visited = set()
        root = Node(board)   
        pq.push(root.path_cost, root)
        
        while pq.size() > 0:
            if pq.size() > self.space: self.space = pq.size() # Space measure
            curr_node = pq.pop()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): # Goal check
                self.display_solution(curr_node)    
                                          
            children = curr_node.get_children()
            for child in children:
                if child.board not in visited:
                    if child not in pq:
                        pq.push(child.path_cost, child)
                    else:
                        # Replace if lower priority
                        pq.replace(child.path_cost, child)                             
        sys.exit("No solution") 

    def gbfs(self, board):
        pq = PriorityQueue()
        visited = set()
        root = Node(board)   
        pq.push(root.path_cost, root)
        
        while pq.size() > 0:
            if pq.size() > self.space: self.space = pq.size() # Space measure
            curr_node = pq.pop()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): # Goal check
                self.display_solution(curr_node)    
                                          
            children = curr_node.get_children()
            for child in children:
                child.get_h1()
                if child.board not in visited:
                    if child not in pq:
                        pq.push(child.h1, child)
                    else:
                        # Replace if lower priority
                        pq.replace(child.h1, child) 
        sys.exit("No solution") 

    def a_star_h1(self, board):
        pq = PriorityQueue()
        visited = set()
        root = Node(board)   
        root.get_h1()
        pq.push(root.h1, root)
        
        while pq.size() > 0:
            if pq.size() > self.space: self.space = pq.size() # Space measure
            curr_node = pq.pop()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): # Goal check
                self.display_solution(curr_node)    
                                          
            children = curr_node.get_children()
            for child in children:
                child.get_h1()
                if child.board not in visited:
                    if child not in pq:
                        pq.push(child.h1, child)
                    else:
                        # Replace if lower priority
                        pq.replace(child.h1, child)                             
        sys.exit("No solution") 
        
    def a_star_h2(self, board):
        pq = PriorityQueue()
        visited = set()
        root = Node(board)   
        root.get_h2()
        pq.push(root.h2, root)
        
        while pq.size() > 0:
            if pq.size() > self.space: self.space = pq.size() # Space measure
            curr_node = pq.pop()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): # Goal check
                self.display_solution(curr_node)    
                                          
            children = curr_node.get_children()
            for child in children:
                child.get_h2()
                if child.board not in visited:
                    if child not in pq:
                        pq.push(child.h2, child)
                    else:
                        # Replace if lower priority
                        pq.replace(child.h2, child)                             
        sys.exit("No solution") 
        
    def a_star_h3(self, board):
        pq = PriorityQueue()
        visited = set()
        root = Node(board)   
        root.get_h3(root.move_cost)
        pq.push(root.h3, root)
        
        while pq.size() > 0:
            if pq.size() > self.space: self.space = pq.size() # Space measure
            curr_node = pq.pop()
            self.time += 1 # Time  measure
            visited.add(curr_node.board)
            
            if curr_node.isGoal(): # Goal check
                self.display_solution(curr_node)    
                                          
            children = curr_node.get_children()
            for child in children:
                child.get_h3(child.move_cost)
                if child.board not in visited:
                    if child not in pq:
                        pq.push(child.h3, child)
                    else:
                        # Replace if lower priority
                        pq.replace(child.h3, child)                             
        sys.exit("No solution") 