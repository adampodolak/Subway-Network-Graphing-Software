import math
from graph import *
from GraphFactory import *


class itinerary:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.mst = [[]]

    def dikstras(self, s1, s2):
        #
        # q holds priority list
        q = []
        distTo = []
        # qfollow and q indexes are connected. qfollow allows access to distTo[old node]
        qfollow = []

        endNode = self.graph.edges[s2-1]

        changeLat = float(self.graph.edges[s2-1].lat) - float(self.graph.edges[s1-1].lat)
        changeLong = float(self.graph.edges[s2-1].long) - float(self.graph.edges[s1-1].long)
        shortest_path = math.hypot(float(changeLat),float(changeLong))


        
        # initialize distTo array
        for i in range(len(self.graph.edges)):
            distTo.append(1000)
            self.mst.append([])
        distTo[s1-1] = 0
        self.mst[s1-1].append(s1)
        

        # initialize q and qfollow
        q.append(self.graph.edges[s1-1])
        qfollow.append(q[0])
        q,qfollow,shortest_path = self.valid(q, qfollow, q[0], shortest_path, endNode)

        # distTo[new node] = time to new node from old node + distTo[old node]
        while q:
            index = int(q[0].id)-1
            if distTo[index] > (int(q[0].time) + distTo[int(qfollow[0].id)-1]):
                distTo[index] = int(q[0].time) + distTo[int(qfollow[0].id)-1]
                #path to new node = path to old node + new node
                self.mst[index] = []
                for i in self.mst[int(qfollow[0].id)-1]:
                    self.mst[index].append(i)
                self.mst[index].append(q[0].id)


            if int(q[0].id) == s2:
                print("leaving")
                break
            q, qfollow,shortest_path= self.valid(q, qfollow,self.graph.edges[int(q[0].id)-1],shortest_path, endNode)
            qfollow.pop()

        return distTo[s2-1]

    def valid(self,q,qfollow, node,shortest_path,endnode):
        best = None
        for i in node.neighbours:
            dist = math.hypot(float(endnode.lat) - float(i.lat),float(endnode.long) - float(i.long))
        
            if dist<= shortest_path:
                shortest_path = dist
                best = i
                q[0].time = i.time
                if dist == 0:
                    break
        q.pop()
        q.append(best)
        q[0].marked = True
        qfollow.append(q[0])
        
        return q,qfollow,shortest_path


        

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

testx = 49
testy = 197
time = sample.dikstras(testx,testy)

print(sample.mst[testy-1])
print("time: " + str(time))