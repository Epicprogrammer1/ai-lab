"""
1.	Implement an Uninformed search algorithm : Depth First search 
"""
visited=[]
def DFS(G,v, start):
    print(start)
    visited[start]=True
    for i in range(v):
        if (G[start][i] == 1 and (not visited[i])):
            DFS(G,v,i)
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
DFS(G,v,rootNode)
"""
Output:
Enter the number of Vertices: 4
Enter number of edges: 6
Enter Edges: 
0 1
0 2
1 2
2 0 
2 3
3 3
Enter Root node: 2
2
0
1
3
"""
