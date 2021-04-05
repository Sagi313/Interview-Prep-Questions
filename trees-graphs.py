def DFS(graph:dict[str:list[str]], start:str, end:str)->bool: # O(V + E)
    if start == end:    # We found a path
        return True
    visited.append(start)
    for adj in graph[start]:
        if adj not in visited:  # Checks to see if we already saw this node before
            if DFS(graph,adj,end):  # In case we found a path
                return True 
    return False

def BFS(graph:dict[str:list[str]], start:str, end:str)->bool:   # O(V + E)
    toVisit=[start] # queue
    visited=[]
    while len(toVisit):
        curr=toVisit.pop(0) # The node we are currently on
        visited.append(curr)    # To make sure we won't get stuck in a loop
        if curr == end: # If we found a path
            return True

        for adj in graph[curr]:   # Add all adjacencies to the queue
            if adj not in visited and adj not in toVisit:
                toVisit.append(adj)
            
    return False

def bidirectionalSearch(graph:dict[str:list[str]], start:str, end:str)->bool:   # Uses 2 BFS. One from start and one from end. When both collaide->True
    toVisit1=[start] # queue
    visited1=[]
    toVisit2=[end]  #queue
    visited2=[]

    while len(toVisit1) and len(toVisit2):
        curr1=toVisit1.pop(0) # The node we are currently on
        visited1.append(curr1)    # To make sure we won't get stuck in a loop

        curr2=toVisit2.pop(0)
        visited2.append(curr2)

        for node in visited1:  # Checks to see if both BFS got to the same node
            if node in visited2:
                return True

        for adj in graph[curr1]:   # Add all adjacencies to the queue
            if adj not in visited1 and adj not in toVisit1:
                toVisit1.append(adj)
        
        endAdj=[]
        for i in graph: # Reverse the path from end to start
            for node in graph[i]:
                if curr2 == node:
                    endAdj.append(i) 

        for adj in endAdj:   # Add all adjacencies to the queue (from the end)
            if adj not in visited2 and adj not in toVisit2:
                toVisit2.append(adj)

    return False

def matBFS(graph:list[list[int]], start:int, end:int)->bool:    # Less optimal than the dict version because of the search inside the matrix, instead of using the hash table
    visited=[]
    toVisit=[start]

    while len(toVisit):
        curr=toVisit.pop(0) # The node we are currently on
        visited.append(curr)    # To make sure we won't get stuck in a loop
        if curr == end: # If we found a path
            return True

        for i in range(len(graph[curr])):   # Add all adjacencies to the queue
            if graph[curr][i] == 1:
                if i not in visited and i not in toVisit:
                    toVisit.append(i)
            
    return False

class node:
    def __init__(self,val:int,left=None,right=None):
        self.val=val 
        self.right= right
        self.left= left


def createBinaryTree(arr:list[int],start:int,end:int):
    if start==end:
        return node(arr[start]) # Returns a leaf
    return node(arr[int((start+end)/2)],createBinaryTree(arr,start,int((start+end)/2)-1),createBinaryTree(arr,int((start+end)/2)+1,end))

def inOrderTra(root:node):  # L-node-R
    if root == None:
        return
    inOrderTra(root.left)
    inOrderTra(root.right)
    print(root.val)


aGraph={'a':['c','d'],'b':['c','a'],'c':['d'],'d':['e'],'e':['c','f'],'f':['e']}
matGraph=[[0,1,1,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,0]]
visited=[]
toBST=[1,2,3,4,5,6,7]
newRoot=createBinaryTree(toBST,0,6)
inOrderTra(newRoot)
