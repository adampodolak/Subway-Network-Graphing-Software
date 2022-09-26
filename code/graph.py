from GraphFactory import *

class Station:
    def __init__(self, id, line, time,lat,long) -> None:
        self.id = id
        self.neighbours = []
        self.line = line
        self.time= time
        self.marked = False
        self.lat = lat
        self.long = long


class Edge:
    def __init__(self, size) -> None:
        self.edges = []
        for i in range(size):
            self.edges.append([]) 
        
    def build_edgeGraph(self, Elist, s):
        #initialize stations in array
        for i in s:
            self.edges[int(i[0])-1] = Station(i[0],None,0,i[1],i[2])


        for i in Elist:
            s1 = Station(i[0], i[2], i[3], self.edges[int(i[0])-1].lat,self.edges[int(i[0])-1].long)
            s2 = Station(i[1], i[2], i[3], self.edges[int(i[1])-1].lat,self.edges[int(i[1])-1].long)
            self.edges[int(i[0])-1].neighbours.append(s2)
            self.edges[int(i[1])-1].neighbours.append(s1)