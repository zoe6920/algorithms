# -*- coding: utf-8 -*-


    
def isSafe(v, graph, path, pos):
   
    # If the vertex is adjacent to
    # the vertex of the previously
    # added vertex
    if graph[path[pos - 1]][v] == 0:
        return False
 
    # If the vertex has already
    # been included in the path
    for i in range(pos):
        if path[i] == v:
            return False
 
    # Both the above conditions are
    # not true, return true
    return True
 
# To check if there exists
# at least 1 hamiltonian cycle
hasCycle = False
 
# Function to find all possible
# hamiltonian cycles
def hamCycle(graph):
    global hasCycle
     
    # Initially value of boolean
    # flag is false
    hasCycle = False
 
    # Store the resultant path
    path = []
    path.append(0)
 
    # Keeps the track of the
    # visited vertices
    visited = [False]*(len(graph))
 
    for i in range(len(visited)):
        visited[i] = False
 
    visited[0] = True
 
    # Function call to find all
    # hamiltonian cycles
    FindHamCycle(graph, 1, path, visited)
 
    if hasCycle:
        # If no Hamiltonian Cycle
        # is possible for the
        # given graph
        print("No Hamiltonian Cycle" + "possible ")
        return
 
# Recursive function to find all
# hamiltonian cycles
def FindHamCycle(graph, pos, path, visited):
   
    # If all vertices are included
    # in Hamiltonian Cycle
    if pos == len(graph):
       
        # If there is an edge
        # from the last vertex to
        # the source vertex
        if graph[path[-1]][path[0]] != 0:
           
            # Include source vertex
            # into the path and
            # print the path
            path.append(0)
            for i in range(len(path)):
                print(path[i]+1, end = " ")
            print()
 
            # Remove the source
            # vertex added
            path.pop()
 
            # Update the hasCycle
            # as true
            hasCycle = True
        return
 
    # Try different vertices
    # as the next vertex
    for v in range(len(graph)):
       
        # Check if this vertex can
        # be added to Cycle
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
 
            # Recur to construct
            # rest of the path
            FindHamCycle(graph, pos + 1, path, visited)
            # Remove current vertex
            # from path and process
            # other vertices
            visited[v] = False
            path.pop()

n,e = map(int,input().split())
graph= []
for i in range(n):
    graph.append([])
    for j in range(n):
        graph[i].append(0)
    
i, j =map(int,input().split())
while i != 0 and j != 0:
    i = i - 1
    j = j - 1
    graph[i][j] = 1
    graph[j][i] = 1
    i, j =map(int,input().split())
hamCycle(graph)
