class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.size = [1] * size  

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]  
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]  
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
            self.size[rootX] += self.size[rootY]  
        return True

def find_connected_components(graph):
    height = len(graph)
    width = len(graph[0])
    ds = DisjointSet(height * width)

    for i in range(height):
        for j in range(width):
            if graph[i][j] == 1:
                index = i * width + j
                if i > 0 and graph[i-1][j] == 1:  # 檢查上方元素
                    ds.union(index, index - width)
                if j > 0 and graph[i][j-1] == 1:  # 檢查左方元素
                    ds.union(index, index - 1)

    components = {}
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 1:
                index = i * width + j
                root = ds.find(index)
                if root in components:
                    components[root].append(index)
                else:
                    components[root] = [index]

    return components.values()

def calculate_areas(components, graph_size):
    areas = []
    for component in components:
        area = sum(graph_size[index] for index in component)
        areas.append(area)
    return areas

h,w = map(int,input().split())
graph = []
for _ in range(h):
    line = input().strip()
    row = [int(char) for char in line]
    graph.append(row)

# Get connected components
connected_components = find_connected_components(graph)
# Calculate the area of each connected component
graph_size = [1] * (len(graph) * len(graph[0]))
areas = calculate_areas(connected_components, graph_size)

print("Number of Connected Components:", len(connected_components))
print("Areas of Connected Components:", areas)

