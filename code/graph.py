from main import format_data, count, find_max


class Station:
    def __init__(self, id, latitude, longitude, name, display_name, zone, total_lines, rail) -> None:
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.dislpay_name = display_name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail


class Edge:
    def __init__(self, size) -> None:
        self.edges = [[0]*size] * size

    def print_edges(self):
        print(self.edges)

    def build_edgeGraph(self, Elist):
        print(Elist[0][3])
        print(Elist[1][3])
        print(Elist[2][3])
        print(Elist[3][3])
        print(Elist[4][3])
        for i in Elist:
            station1 = int(i[0]) - 1
            station2 = int(i[1]) - 1
            time = int(i[3])
            self.edges[station1][station2] = time

    def get(self, s1, s2):
        s1 -= 1
        s2 -= 1
        return self.edges[s1][s2]


graph = Edge(find_max('../_dataset/london.stations.csv'))
graph.build_edgeGraph(format_data('../_dataset/london.connections.csv'))
print("results")
print(graph.get(163, 11))
print(graph.get(11, 212))
print(graph.get(49, 87))
print(graph.get(49, 197))
print(graph.get(82, 163))
