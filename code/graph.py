from GraphFactory import *


class Station:
    def __init__(self, id, line, time) -> None:
        self.id = id
        self.neighbours = []
        self.line = line
        self.time = time


class Edge:
    def __init__(self, size):
        self.edges = []
        for i in range(size):
            self.edges.append([])

    def build_edgeGraph(self, Elist, size):
        # initialize stations in array
        for i in range(size):
            self.edges[i] = Station(i+1, 0, 0)

        for i in Elist:
            s1 = Station(i[0], i[2], i[3])
            s2 = Station(i[1], i[2], i[3])
            self.edges[int(i[0])-1].neighbours.append(s2)
            self.edges[int(i[1])-1].neighbours.append(s1)

    def get(self, s1, s2):
        a = s1-1
        b = s2
        for i in self.edges[a].neighbours:
            if (int(i.id) == int(b)):
                return i.time


connections = '../_dataset/london.connections.csv'
stations = '../_dataset/london.stations.csv'

g = GraphFactory()
connections_graph = g.build_graph("connections")
edges = connections_graph.format_csv_file(connections)
size = connections_graph.find_max(stations)

graph = Edge(size)
graph.build_edgeGraph(edges, size)

# graph.build_edgeGraph(format_data('../_dataset/london.connections.csv'), size)


print("results")

print(graph.get(11, 163))
# for i in graph.edges[10].neighbours:
#    print(i.id)
print(graph.edges[10].neighbours[0].id)
print(graph.get(11, 212))
print(graph.get(49, 87))
print(graph.get(49, 197))
print(graph.get(82, 163))
