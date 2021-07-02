"""
1. Implement an Uninformed search algorithm: Breadth first search
"""
visited=[]
def BFS(G,v, start,goalNode):
    visited = [False] * v
    q = [start]
    visited[start] = True
    while q:
        current_node = q[0]
        print(current_node, end = ' ')
        q.pop(0)
        for i in range(v):
            if (G[current_node][i] == 1 and (not visited[i])):
                if(goalNode==i):
                    print(goalNode)
                    return
                q.append(i)
                visited[i] = True
def addEdge(G, start, end):
    G[start][end] = 1
    G[end][start] = 1
v=int(input('Enter the number of Vertices: '))
G = [[0 for i in range(v)] for j in range(v)]
visited=[False]*v
noOfEdges=int(input("Enter number of edges: "))
print("Enter Edges: ")
for i in range(noOfEdges):
    addEdge(G,*list(map(int,input().split())))
rootNode=int(input("Enter Root node: "))
goalNode=int(input("Enter Destination node: "))
BFS(G,v,rootNode,goalNode)

"""
OUTPUT:
Enter the number of Vertices: 6

Enter number of edges: 10

Enter Edges: 
0 1
1 2
2 3
4 5
5 1
5 3
2 5
2 4
1 3
1 4
Enter Root node: 1
Enter Destination node: 6
1 0 2 3 4 5 
"""
