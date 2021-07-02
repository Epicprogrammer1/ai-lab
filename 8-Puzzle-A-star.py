"""
1)	To solve 8-puzzle problem using A* algorithm
"""
from copy import copy,deepcopy
import heapq

class Node:     
    def __init__(self,state,parent,level):
        self.state=state
        self.parent=parent
        self.level=level
        self.cost=0
            
    def __lt__(self,other):
        return self.cost<other.cost
    
    def blankposition(self):
        mat=self.state
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j]=="_"):
                    return (i,j)
                
def misplaced_tiles(current_state,goal_state):
    cnt=0  
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if(current_state[i][j]!=goal_state[i][j] and current_state[i][j]!="_"):
                cnt+=1
    return cnt

def generatechildren(current_state,priorityqueue):
    action_dict={
        'up': [0,-1],
        'down': [0,1],
        'left': [-1,0],
        'right': [1,0],
    }
    
    m=len(current_state.state)
    n=len(current_state.state[0])
    
    current_state_blank=current_state.blankposition()
    for i in action_dict.values():
        x,y=current_state_blank[0]+i[0],current_state_blank[1]+i[1]
        
        if(x >= 0 and x < m and y >= 0 and y < n):
            new_state=Node(deepcopy(current_state.state),current_state,current_state.level+1)
            new_state.state[x][y],new_state.state[current_state_blank[0]][current_state_blank[1]]=new_state.state[current_state_blank[0]][current_state_blank[1]],new_state.state[x][y]
            new_state.cost=misplaced_tiles(new_state.state,goal_state)

            if(new_state.state not in closed_list): 
                heapq.heappush(priorityqueue,new_state)
                
closed_list=[]

def solve(intial,depthlimit=10000):
    priorityqueue=[]
    curr_depth=0
    root=Node(intial,None,0)
    root.cost=misplaced_tiles(root.state,goal_state)
    heapq.heappush(priorityqueue,root)
    
    while(len(priorityqueue)!=0 and curr_depth<depthlimit):
        minimum_ele=heapq.heappop(priorityqueue)
        heapq.heappush(closed_list,minimum_ele.state)
        
        if(minimum_ele.cost==0):
            printPath(minimum_ele)
            return
        
        generatechildren(minimum_ele,priorityqueue)
        curr_depth+=1
    print()
    
    if(curr_depth==depthlimit):
        print("Depth Limit Reached",depthlimit)

def printMatrix(mat):
    n=3
    for i in range(n):
        for j in range(n):
            print((mat[i][j]), end = " ")
             
        print()
        
def printPath(root):     
    if root == None:
        return
    
    printPath(root.parent)
    print("g=" ,root.level," h=",root.cost," f=",root.cost+root.level)
    printMatrix(root.state)
    print()
    
print("Enter Initial State (_ for representing blank space): ")

start_state=[]
goal_state=[]
for i in range(3):
    start_state.append(input().split())
print("Enter Goal State (_ for representing blank space): ")
for i in range(3):
    goal_state.append(input().split())
print("\nSolution: \n")
solve(start_state)


"""
Output:

Test Case 1:
Enter Initial State (_ for representing blank space): 
1 2 3
5 6 _
7 8 4
Enter Goal State (_ for representing blank space): 
1 2 3
5 8 6
_ 7 4

Solution: 

g= 0  h= 3  f= 3
1 2 3 
5 6 _ 
7 8 4 

g= 1  h= 2  f= 3
1 2 3 
5 _ 6 
7 8 4 

g= 2  h= 1  f= 3
1 2 3 
5 8 6 
7 _ 4 

g= 3  h= 0  f= 3
1 2 3 
5 8 6 
_ 7 4

Test Case 2:
Enter Initial State (_ for representing blank space): 
8 1 2
_ 4 3
7 6 5
Enter Goal State (_ for representing blank space): 
1 2 3
4 5 6
7 8 _

Solution: 
Depth Limit Reached 10000
"""

