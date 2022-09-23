from abc import ABC, abstractmethod
from typing import TypedDict
from graph import EdgeGraph
from Itinerary import Itinerary


class PathfinderResult(TypedDict):
    num_nodes_visited: int
    num_edges_visited: int
    travel_time: int


class PathfinderAlgorithm(ABC):
    nodes_visited = 0
    edges_visited = 0
    travel_time = 0

    def call(self, graph: EdgeGraph) -> PathfinderResult:
        result: PathfinderResult = {
            "path": self.findpath(graph),
            "nodes": self.nodes_visited,
            "edges": self.edges_visited,
            "travel time": self.travel_time
        }
        return result

    @abstractmethod
    def findpath(self, graph: EdgeGraph, station1, station2):
        pass


class Dijkstras(PathfinderAlgorithm):
    # implement dijkstras here, add the number of nodes visited, edges visited, travel time, and return the path
    def findpath(self, graph: EdgeGraph, station1, station2):
        return Itinerary(graph).dijkstras(station1, station2)


class Astar(PathfinderAlgorithm):
    # implement A*
    def findpath(self, graph: EdgeGraph, station1, station2):
        return Itinerary(graph).Astar(station1, station2)


class SortingFactory():

    @staticmethod
    def createPathfinder(name):
        if name == "dijkstras":
            return Dijkstras()
        elif name == "a*":
            return Astar()
        else:
            raise ValueError(name)
