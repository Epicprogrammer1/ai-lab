"""
2.	Implement an Uninformed search algorithm: IDFS.
"""
visited=[]
def IDFS(G,v, start,goalNode,curr_depth,limit):
    print(start,end=" ")
    if(curr_depth<=limit):
        visited[start]=True
        for i in range(v):
            if (G[start][i] == 1 and (not visited[i])):
                IDFS(G,v,i,goalNode,curr_depth+1,limit)
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
goalNode=int(input("Enter the Goal Node:"))
for i in range(0,int(input("Enter Max depth: "))):
    print("\nDepth Limit:",i , end="  ")
IDFS(G,v,rootNode,goalNode,0,i)
"""
Output:
Enter the number of Vertices: 7
Enter number of edges: 6
Enter Edges: 
0 1
0 2
1 3
1 4
2 5
2 6
Enter Root node: 0
Enter the Goal Node:6
Enter Max depth: 2
Depth Limit: 0  0 1 2 
Depth Limit: 1  0 1 3 4 2 5 6 
"""
