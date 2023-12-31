from GraphFactory import GraphFactory


class Station:

    # initialize a station class
    # holds information relating to each stations
    # our graph will be formed of Station objects
    def __init__(self, id, line, lat, long, zone) -> None:
        self.neighbours = []
        self.id = id
        self.zone = zone
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

    def build_edge_graph(self, Elist, s):
        # initialize stations in array
        for i in s:
            self.edges[int(i[0])-1] = Station(i[0], None, i[1], i[2], i[5])

        # add the neighbours to the neighbours array
        for i in Elist:
            self.edges[int(
                i[0])-1].neighbours.append(int(self.edges[int(i[1])-1].id))
            self.edges[int(i[0])-1].time.append(i[3])
            self.edges[int(
                i[1])-1].neighbours.append(int(self.edges[int(i[0])-1].id))
            self.edges[int(i[1])-1].time.append(i[3])


class BuildEdgeGraph:

    # method to build the final graph
    def build():
        connections = '_dataset/london.connections.csv'
        stations = '_dataset/london.stations.csv'

        g = GraphFactory()
        connections_graph = g.build_graph("connections")
        stations_graph = g.build_graph("stations")
        edges = connections_graph.format_csv_file(connections)
        s = stations_graph.format_csv_file(stations)
        size = stations_graph.find_max(stations)

        graph = EdgeGraph(size)
        graph.build_edge_graph(edges, s)

        return graph
