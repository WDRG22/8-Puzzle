# from searches import Search


# print("\nWelcome to my 8-Puzzle solver\n")

# while True:
#     try:
#         print("Select a difficulty:")
#         print(" 1: Easy")
#         print(" 2: Medium")
#         print(" 3: Hard")
#         difficulty = int(input())
#         if difficulty < 1 or difficulty > 3:
#             raise ValueError
#         break
#     except ValueError:
#         print("Invalid entry.")
# print()
    
# while True:
#     try:
#         print("Select an algorithm:")
#         print(" 1: Breadth-First Search")
#         print(" 2: Depth-First Search")
#         print(" 3: Uniform-Cost Search")
#         print(" 4: Greedy Best First Seach")
#         print(" 5: A* (h1)")
#         print(" 6: A* (h2)")
#         print(" 7: A* (h3)")
#         algorithm = int(input())
#         if algorithm < 1 or algorithm > 7:
#             raise ValueError
#         break
#     except ValueError:
#         print("Invalid entry.")        
# print()

# match difficulty:
#     case 1:
#         root = (1,3,4,8,6,2,7,0,5)
#     case 2:
#         root = (2,8,1,0,4,3,7,6,5)
#     case 3:
#         root = (5,6,7,4,0,8,3,2,1)
        
# search = Search()
# match algorithm:
#     case 1:
#         search.bfs(root)
#     case 2:
#         search.dfs(root)
#     case 3:
#         search.ucs(root)
#     case 4:
#         search.gbfs(root)
#     case 5:
#         print(5)
#     case 6:
#         print(6)
#     case 7:
#         print(7)
        
        
        
#     #### TESTING ####
from node import Node
from searches import Search
from searches import PriorityQueue

easy = (1,3,4,8,6,2,7,0,5)
med = (2,8,1,0,4,3,7,6,5)
hard = (5,6,7,4,0,8,3,2,1)
search = Search()
search.gbfs(hard)


# # n3 = Node((1,3,4,8,6,2,7,0,5), path_cost=2)
# # n2 = Node((1,3,4,8,6,2,7,0,5), path_cost=5)
# # n5 = Node((1,3,4,8,6,2,7,5,0), path_cost=5)
# # n1 = Node((1,3,4,8,6,2,7,0,5), path_cost=10)
# # n4 = Node((1,3,4,8,6,2,7,0,5), path_cost=14)
# # pq = PriorityQueue()

# # pq.push(n1, n1.path_cost)
# # pq.push(n2, n2.path_cost)
# # pq.push(n3, n3.path_cost)
# # pq.push(n4, n4.path_cost)
# # pq.push(n5, n5.path_cost)

# # print(pq.pop())
# # print(pq.pop())
# # print(pq.pop())
# # print(pq.pop())
# # print(pq.pop())
# # print(pq.pop().path_cost)
# # print(pq.pop().path_cost)
# # print(pq.pop().path_cost)
# # print(pq.pop().path_cost)