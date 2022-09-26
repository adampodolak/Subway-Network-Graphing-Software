from graph import *
from BFS import * 


class itinerary:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.mst = [[]]

    def dikstras(self, s1, s2):
        # q holds priority list
        q = [self.graph.edges[s1-1]]
        distTo = []
        # qfollow and q indexes are connected. qfollow allows access to distTo[old node]
        qfollow = [self.graph.edges[s1-1]]


        # initialize distTo array
        for i in range(len(self.graph.edges)):
            distTo.append(1000)
            self.mst.append([])
        distTo[s1-1] = 0
        self.mst[s1-1].append(s1)
       

        q = self.find_neighbours(q, qfollow)

        while q:
            index = int(q[0].id)-1
            # distTo[new node] = time to new node from old node + distTo[old node]
            if distTo[index] > (int(q[0].time) + distTo[int(qfollow[0].id)-1]):
                distTo[index] = int(q[0].time) + distTo[int(qfollow[0].id)-1]
                #path to new node = path to old node + new node
                self.mst[index] = []
                for i in self.mst[int(qfollow[0].id)-1]:
                    self.mst[index].append(i)
                self.mst[index].append(q[0].id)

            #update priority queue
            q = self.find_neighbours(q, qfollow)
            q.pop(0)
            qfollow.pop(0)

        if s2<=len(self.graph.edges):
            return distTo[s2-1]

    def find_neighbours(self, q, qfollow):
        for i in self.graph.edges[int(q[0].id)-1].neighbours:
            if i.marked == False:
                q.append(i)
                i.marked = True
                qfollow.append(q[0])
        return q

connections = '../_dataset/london.connections.csv'
stations = '../_dataset/london.stations.csv'

g = GraphFactory()
connections_graph = g.build_graph("connections")
stations_graph = g.build_graph("stations")
edges = connections_graph.format_csv_file(connections)
s = stations_graph.format_csv_file(stations)
size = stations_graph.find_max(stations)


graph = Edge(size)
graph.build_edgeGraph(edges, s)
sample = itinerary(graph)

testx = 256
testy = 92
time = sample.dikstras(testx,testy)


print(sample.mst[testy-1])
print("time: " + str(time))