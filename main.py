from puzzle import Node, searches

print("Welcome to my 8-Puzzle solver")

while True:
    try:
        print("Select a difficulty:")
        print(" 1: Easy")
        print(" 2: Medium")
        print(" 3: Hard")
        difficulty = int(input())
        if difficulty < 1 or difficulty > 3:
            raise ValueError
        break
    except ValueError:
        print("Invalid entry.")
    
while True:
    try:
        print("Select an algorithm:")
        print(" 1: Breadth-First Search")
        print(" 2: Depth-First Search")
        print(" 3: Uniform-Cost Search")
        print(" 4: Greedy Best First Seach")
        print(" 5: A* (h1)")
        print(" 6: A* (h2)")
        print(" 7: A* (h3)")
        algorithm = int(input())
        if algorithm < 1 or algorithm > 7:
            raise ValueError
        break
    except ValueError:
        print("Invalid entry.")        

match difficulty:
    case 1:
        root = (1,3,4,8,6,2,7,0,5)
    case 2:
        root = (2,8,1,0,4,3,7,6,5)
    case 3:
        root = (5,6,7,4,0,8,3,2,1)
        
search = searches()
match algorithm:
    case 1:
        search.bfs(root)
    case 2:
        search.dfs(root)
    case 3:
        search.ucs(root)
    case 4:
        search.gbfs(root)
    case 5:
        print(5)
    case 6:
        print(6)
    case 7:
        print(7)