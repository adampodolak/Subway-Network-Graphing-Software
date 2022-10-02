
from abc import ABC, abstractmethod
from typing import TypedDict


class PathfinderResult(TypedDict):
    path: list[int]
    num_nodes_visited: int
    num_edges_visited: int
    travel_time: int


class PathfinderAlgorithm(ABC):
    nodes_visited = 0
    edges_visited = 0
    travel_time = 0

    def call(self, graph, s1, s2) -> PathfinderResult:
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
    def findpath(self, graph, s1, s2):
        pass
