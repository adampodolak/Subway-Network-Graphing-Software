from abc import ABC, abstractmethod
from typing import TypedDict
from graph import *
import math
from PathCoverage import *


class PathfinderResult(TypedDict):
    path: list[int]
    num_nodes_visited: int
    num_edges_visited: int
    travel_time: int


class PathfinderAlgorithm(ABC):
    nodes_visited = 0
    edges_visited = 0
    travel_time = 0

    def call(self, graph: EdgeGraph, s1, s2) -> PathfinderResult:
        self.result: PathfinderResult = {
            "path": self.findpath(graph, s1, s2),
            "nodes": self.nodes_visited,
            "edges": self.edges_visited,
            "travel time": self.travel_time
        }
        return self.result

    def set(self, num_nodes, num_edges, travel_time):
        self.nodes_visited = num_nodes
        self.edges_visited = num_edges
        self.travel_time = travel_time

    @abstractmethod
    def findpath(self, graph: EdgeGraph, s1, s2):
        pass


class Dijkstras(PathfinderAlgorithm):
    def findpath(self, graph: EdgeGraph, s1, s2):
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
                distTo[index] = int(q[0].time[findTime]) + distTo[int(qfollow[0].id)-1]
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


class AstarDFS(PathfinderAlgorithm):
    def findpath(self, graph: EdgeGraph, s1, s2):
        path = [graph.edges[s1-1]]
        end = False

        # if start and end node are the same
        if s1 == s2:
            end = True

        # if start or end node not an actual station
        if s1 < 0 or s1 > len(graph.edges) or s2 < 0 or s2 > len(graph.edges):
            self.set(0, 0, 1000)
            return []

        while not end:
            path, end = self.find_next_node(graph, graph.edges[s2-1], path, end)
            if end:
                break

        dist = self.find_distance(path)

        nodes = len(path)
        edges = nodes-1
        self.set(nodes, edges, dist)

        for i in graph.edges:
            if i:
                i.marked = False
        answer = []
        for i in path:
            answer.append(int(i.id))
        return answer

    def find_next_node(self, graph, s2, path, end):
        closestN = None
        relativeShort = 1000
        for i in path[len(path)-1].neighbours:
            if not graph.edges[i-1].marked:
                edge1 = float(s2.lat) - float(graph.edges[i-1].lat)
                edge2 = float(s2.long) - float(graph.edges[i-1].long)
                dist = math.hypot(edge1, edge2)

                if dist <= relativeShort:
                    relativeShort = dist
                    closestN = graph.edges[i-1]
                    if dist == 0:
                        end = True
                        break
        if closestN:
            closestN.marked = True
            path.append(closestN)
        else:
            path.pop()
        return path, end

    def find_distance(self, path):
        dist = 0
        for i in range(len(path)-1):
            t_index = path[i].neighbours.index(int(path[i+1].id))
            dist += int(path[i].time[t_index])
        return dist


class PathfinderFactory():

    @staticmethod
    def createPathfinder(name):
        if name == "dijkstras":
            return Dijkstras()
        elif name == "a*":
            return AstarDFS()
        else:
            raise ValueError(name)


graph = main()

alg = PathfinderFactory()
dijkstras = alg.createPathfinder("dijkstras")
a = alg.createPathfinder("a*")
# dijkstras.call(graph, 42, 300)
# a.call(graph,42,300)

# result1 = dijkstras.result
# print(result1)

# aresult = a.result
# print(aresult)

traverser = TravellingSalesman(graph,dijkstras)
traverser.find(27,[27,103,56,74])