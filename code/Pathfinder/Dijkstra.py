from PathfinderInterface import PathfinderAlgorithm
import sys
sys.path.insert(0, './../GraphBuilder')
from GraphBuilder import EdgeGraph

class Dijkstras(PathfinderAlgorithm):
    def findpath(self, graph: EdgeGraph, s1, s2):
        if not graph.edges[s1-1] or not graph.edges[s2 - 1]:
            return []

        mst = [[]]
        # q holds priority list
        q = [graph.edges[s1-1]]
        distTo = []
        # qfollow and q indexes are connected. qfollow allows access to distTo[old node]
        qfollow = [graph.edges[s1-1]]

        # initialize distTo array
        for i in range(len(graph.edges)):
            distTo.append(1000)
            mst.append([])
        distTo[s1-1] = 0
        mst[s1-1].append(int(s1))

        # if start or end node not an actual station
        if s1 < 0 or s1 > len(graph.edges) or s2 < 0 or s2 > len(graph.edges):
            self.set(0, 0, 1000)
            return []

        while q:
            q = self.find_neighbours(graph, q, qfollow)
            q.pop(0)
            qfollow.pop(0)
            if not q:
                break
            index = int(q[0].id)-1
            # distTo[new node] = time to new node from old node + distTo[old node]
            findTime = q[0].neighbours.index(int(qfollow[0].id))
            if distTo[index] > int(q[0].time[findTime]) + distTo[int(qfollow[0].id)-1]:
                distTo[index] = int(q[0].time[findTime]) + \
                    distTo[int(qfollow[0].id)-1]
                # path to new node = path to old node + new node
                mst[index] = []
                for i in mst[int(qfollow[0].id)-1]:
                    mst[index].append(int(i))
                mst[index].append(int(q[0].id))

        nodes = len(mst[s2-1])
        edges = len(mst[s2-1]) - 1

        self.set(nodes, edges, distTo[s2-1])

        if s2 <= len(graph.edges):
            for i in graph.edges:
                if i:
                    i.marked = False
            return mst[s2-1]

    def find_neighbours(self, graph: EdgeGraph, q, qfollow):
        for i in q[0].neighbours:
            if not graph.edges[i-1].marked:
                q.append(graph.edges[i-1])
                graph.edges[i-1].marked = True
                qfollow.append(q[0])
        return q