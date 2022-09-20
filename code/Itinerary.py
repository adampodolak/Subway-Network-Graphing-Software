from graph import *
from main import *

class itinerary:
    def __init__(self,graph) -> None:
        self.graph=graph
    
    def dikstras(self, s1,s2):
        q = []
        distTo = []
        qfollow = []

        for i in range(len(self.graph.edges)):
            distTo.append(1000)
            
        distTo[s1-1] = 0


        #distTo[new node] = distTo[old node] + time to new node 
        #implement this later
        q.append(self.graph.edges[s1-1])
        qfollow.append(int(q[0].id))
        q = self.find_neighbours(q,qfollow)

        while q:
            index = int(q[0].id)-1
            if distTo[index]>int(q[0].time) + distTo[qfollow[0]]:
                distTo[index] = int(q[0].time) + distTo[qfollow[0]]
            q = self.find_neighbours(q,qfollow)
            q.pop(0)
            qfollow.pop(0)
            print(distTo[s2-1])

        return distTo[s2-1]
            
    def find_neighbours(self, q,qfollow):
        for i in self.graph.edges[int(q[0].id)-1].neighbours:
            if i.marked == False:
                q.append(i)
                qfollow.append(int(q[0].id))
                i.marked = True
        return q

size = find_max('../_dataset/london.stations.csv')
graph = Edge(size)
graph.build_edgeGraph(format_data('../_dataset/london.connections.csv'),size)
sample = itinerary(graph)
print (sample.dikstras(13,279))

