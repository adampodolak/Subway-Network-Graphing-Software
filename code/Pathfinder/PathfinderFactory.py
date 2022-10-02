from Dijkstra import Dijkstras
from Astar import AstarDFS

class PathfinderFactory():

    @staticmethod
    def create_pathfinder(name):
        if name == "dijkstras":
            return Dijkstras()
        elif name == "a*":
            return AstarDFS()
        else:
            raise ValueError(name)
