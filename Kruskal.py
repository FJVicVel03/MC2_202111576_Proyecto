import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph  = []
        self.nodes = []
        self.parent = {}
        self.rank = {}
        self.MST = []
        
        
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])
    
    def addNode(self,value):
        self.nodes.append(value)
        
    def printSolution(self,s,d,w):
        for s,d,w in self.MST:
            print("%s - %s: %s" % (s,d,w))
            
    def makeSet(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0
        
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        
    def kruskalAlgo(self):
        i, e = 0,0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        for vertex in self.nodes:
            self.makeSet(vertex)
        while e < self.V -1:
            s,d,w = self.graph[i]
            i+=1
            x = self.find(s)
            y = self.find(d)
            if x != y:
                e+=1
                self.MST.append([s,d,w])
                self.union(x,y)
        self.printSolution(s,d,w)
        

# Pedimos la cantidad de nodos y aristas
n = int(input("Ingresa la cantidad de nodos: "))
g = Graph(n)

# Pedimos los nombres de los nodos
for i in range(n):
    node = input("Ingresa el nombre del nodo " + str(i+1) + ": ")
    g.addNode(node)

# Pedimos las aristas
e = int(input("Ingresa la cantidad de aristas: "))
for i in range(e):
    print("Arista " + str(i+1))
    s = input("Ingresa el nombre del nodo de origen: ")
    d = input("Ingresa el nombre del nodo de destino: ")
    w = int(input("Ingresa el peso de la arista: "))
    g.addEdge(s,d,w)

g.kruskalAlgo()

#Creamos un grafo vacío
G = nx.Graph()

#Agregamos los nodos
for node in g.nodes:
    G.add_node(node)

#Agregamos las aristas del grafo ingresado
for edge in g.graph:
    G.add_edge(edge[0], edge[1], weight=edge[2])

#Agregamos las aristas del árbol de expansión mínima
for edge in g.MST:
    G.add_edge(edge[0], edge[1], weight=edge[2], color='r')

#Obtenemos las posiciones de los nodos
pos = nx.spring_layout(G)

#Dibujamos el grafo
nx.draw(G, pos, with_labels=True, font_weight='bold')

#Dibujamos las etiquetas de las aristas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#Dibujamos las aristas del árbol de expansión mínima en color rojo
edges = G.edges()
colors = [G[u][v]['color'] if ('color' in G[u][v]) else 'k' for u,v in edges]
nx.draw_networkx_edges(G, pos, edgelist=g.MST, edge_color='r', width=2)

#Mostramos el grafo
plt.show()
