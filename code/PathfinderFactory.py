from abc import ABC, abstractmethod
from typing import TypedDict
from graph import *
import math


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
    # implement dijkstras here, add the number of nodes visited, edges visited, travel time, and return the path
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
        mst[s1-1].append(s1)

        q = self.find_neighbours(graph, q, qfollow)

        while q:
            index = int(q[0].id)-1
            # distTo[new node] = time to new node from old node + distTo[old node]
            if distTo[index] > (int(q[0].time) + distTo[int(qfollow[0].id)-1]):
                distTo[index] = int(q[0].time) + distTo[int(qfollow[0].id)-1]
                # path to new node = path to old node + new node
                mst[index] = []
                for i in mst[int(qfollow[0].id)-1]:
                    mst[index].append(i)
                mst[index].append(q[0].id)

            # update priority queue
            q = self.find_neighbours(graph, q, qfollow)
            q.pop(0)
            qfollow.pop(0)

        nodes = len(mst[s2-1])
        edges = len(mst[s2-1]) - 1

        self.set(nodes, edges, distTo[s2-1])

        if s2 <= len(graph.edges):
            return mst[s2-1]

    def find_neighbours(self, graph: EdgeGraph, q, qfollow):
        for i in graph.edges[int(q[0].id)-1].neighbours:
            if i.marked == False:
                q.append(i)
                i.marked = True
                qfollow.append(q[0])
        return q


class Astar(PathfinderAlgorithm):

    # implement A*
    def findpath(self, graph: EdgeGraph, s1, s2):
        mst = [[]]
        # q holds priority list
        q = []
        distTo = []
        # qfollow and q indexes are connected. qfollow allows access to distTo[old node]
        qfollow = []

        endNode = graph.edges[s2-1]

        changeLat = float(
            graph.edges[s2-1].lat) - float(graph.edges[s1-1].lat)
        changeLong = float(
            graph.edges[s2-1].long) - float(graph.edges[s1-1].long)
        shortest_path = math.hypot(float(changeLat), float(changeLong))

        # initialize distTo array
        for i in range(len(graph.edges)):
            distTo.append(1000)
            mst.append([])
        distTo[s1-1] = 0
        mst[s1-1].append(s1)

        # initialize q and qfollow
        q.append(graph.edges[s1-1])
        qfollow.append(q[0])
        q, qfollow, shortest_path = self.valid(
            q, qfollow, q[0], shortest_path, endNode)

        # distTo[new node] = time to new node from old node + distTo[old node]
        while q:
            index = int(q[0].id)-1
            if distTo[index] > (int(q[0].time) + distTo[int(qfollow[0].id)-1]):
                distTo[index] = int(q[0].time) + distTo[int(qfollow[0].id)-1]
                # path to new node = path to old node + new node
                mst[index] = []
                for i in mst[int(qfollow[0].id)-1]:
                    mst[index].append(i)
                mst[index].append(q[0].id)

            if int(q[0].id) == s2:
                print("leaving")
                break
            q, qfollow, shortest_path = self.valid(
                q, qfollow, graph.edges[int(q[0].id)-1], shortest_path, endNode)
            qfollow.pop()

        return distTo[s2-1]

    def valid(self, q, qfollow, node, shortest_path, endnode):
        best = None
        for i in node.neighbours:
            dist = math.hypot(float(endnode.lat) - float(i.lat),
                              float(endnode.long) - float(i.long))

            if dist <= shortest_path:
                shortest_path = dist
                best = i
                q[0].time = i.time
                if dist == 0:
                    break
        q.pop()
        q.append(best)
        q[0].marked = True
        qfollow.append(q[0])

        return q, qfollow, shortest_path


class PathfinderFactory():

    @staticmethod
    def createPathfinder(name):
        if name == "dijkstras":
            return Dijkstras()
        elif name == "a*":
            return Astar()
        else:
            raise ValueError(name)


graph = main()

alg = PathfinderFactory()
dijkstras = alg.createPathfinder("dijkstras")
dijkstras.call(graph, 11, 45)
result = dijkstras.result
nodes = dijkstras.result["nodes"]
edges = dijkstras.result["edges"]
print(result)
print(nodes, edges)
