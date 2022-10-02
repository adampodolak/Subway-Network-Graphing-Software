from GraphFactory import *


class Station:
    def __init__(self, id, line, lat, long) -> None:
        self.id = id
        self.neighbours = []
        self.line = line
        self.time = []
        self.marked = False
        self.lat = lat
        self.long = long


class EdgeGraph:

    def __init__(self, size) -> None:
        self.edges = []
        for i in range(size):
            self.edges.append([])

    def build_edgeGraph(self, Elist, s):
        # initialize stations in array
        for i in s:
            self.edges[int(i[0])-1] = Station(i[0], None, i[1], i[2])

        for i in Elist:
            self.edges[int(i[0])-1].neighbours.append(
                    int(self.edges[int(i[1])-1].id))
            self.edges[int(i[0])-1].time.append(i[3])
            self.edges[int(i[1])-1].neighbours.append(
                int(self.edges[int(i[0])-1].id))
            self.edges[int(i[1])-1].time.append(i[3])


def getWeight(graph, s1, s2):
    return (graph.get(s1, s2))


def main():
    connections = '../_dataset/london.connections.csv'
    stations = '../_dataset/london.stations.csv'

    g = GraphFactory()
    connections_graph = g.build_graph("connections")
    stations_graph = g.build_graph("stations")
    edges = connections_graph.format_csv_file(connections)
    s = stations_graph.format_csv_file(stations)
    size = stations_graph.find_max(stations)

    graph = EdgeGraph(size)
    graph.build_edgeGraph(edges, s)

    return graph


main()
