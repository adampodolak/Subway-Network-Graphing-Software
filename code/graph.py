from GraphFactory import *


class Station:
    def __init__(self, id, line, time, lat, long) -> None:
        self.id = id
        self.neighbours = []
        self.line = line
        self.time = time
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
            self.edges[int(i[0])-1] = Station(i[0], None, 0, i[1], i[2])

        for i in Elist:
            s1 = Station(i[0], i[2], i[3], self.edges[int(
                i[0])-1].lat, self.edges[int(i[0])-1].long)
            s2 = Station(i[1], i[2], i[3], self.edges[int(
                i[1])-1].lat, self.edges[int(i[1])-1].long)
            self.edges[int(i[0])-1].neighbours.append(s2)
            self.edges[int(i[1])-1].neighbours.append(s1)


def getWeight(graph, s1, s2):
    return(graph.get(s1, s2))


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
