class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.weights = [0 for _ in range(vertices)]
        self.E = 0
        self.edges = dict()

    def add_edge(self, u, v):
        self.graph[u][v] = self.graph[v][u] = 1
        self.edges[frozenset((u, v))] = len(self.edges)
        self.E += 1

    def get_edge(self, u, v):
        return self.edges[frozenset([u, v])]


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 1)
g.add_edge(2, 3)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(0, 4)
g.add_edge(3, 5)
g.add_edge(3, 6)
g.weights = [4, 5, 6, 2, 1, 7, 3]

# primal dual method
# 1. initial values of x and y
X = [0 for _ in range(g.V)]
Y = [0 for _ in range(g.E)]

for u, v in g.edges:
    # 2. pick e = uv such that X_u + X_v < 1
    e = g.get_edge(u, v)

    # 3. increase Y_e such that Sigma Y_f = W_u or Sigma Y_f = W_v
    ΔW_u = g.weights[u] - sum([Y[g.get_edge(u, i)] for i in range(g.V) if g.graph[i][u] == 1])
    ΔW_v = g.weights[v] - sum([Y[g.get_edge(v, i)] for i in range(g.V) if g.graph[i][v] == 1])
    if ΔW_u > ΔW_v:
        Y[g.get_edge(u, v)] += ΔW_v
        X[v] = 1
    else:
        Y[g.get_edge(u, v)] += ΔW_u
        X[u] = 1

print('value of x : ', X)
print('value of y : ', Y)
print('weight : ', sum([X[i] * g.weights[i] for i in range(g.V)]))