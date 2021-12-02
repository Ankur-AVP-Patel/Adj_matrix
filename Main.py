class Graph(object):

    # Initialise adjacency matrix
    def __init__(self, size):
        self.adjmatrix = []
        for i in range(size):
            self.adjmatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, u, v):
        if u == v:
            print("%d and %d are the same vertex!" % (u, v))
        self.adjmatrix[u][v] = 1
        self.adjmatrix[v][u] = 1

    # Remove Edges
    def remove_edge(self, u, v):
        if self.adjmatrix[u][v] == 0:
            print("There is no edge between %d and %d" % (u, v))
        self.adjmatrix[u][v] = 0
        self.adjmatrix[v][u] = 0
    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjmatrix:
            print(row)

    def dfs(self, temp, start_vert, visited):
        # print(start_vert, end=' ')

        # set start vert tas visited
        visited[start_vert] = True
        temp.append(start_vert)

        for i in range(self.size):
            if (self.adjmatrix[start_vert][i] == 1 and (not visited[i])):
                self.dfs(temp, i, visited)
        return (temp)



    def get_connected_components(self):
        visited = [False] * self.size
        connected_comp = []

        # set all verts to not visited
        for i in range(self.size):
            visited.append(False)

        for v in range(self.size):
            if visited[v] == False:
                temp = []
                connected_comp.append(self.dfs(temp, v, visited))
        return connected_comp

def main():
    g = Graph(5)

    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 4)


    g.print_matrix()


    output =  g.get_connected_components()
    

if __name__ == '__main__':
    main()