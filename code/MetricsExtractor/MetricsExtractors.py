
import sys
# flake8 is returning E402 here but,
# there is no other way to format the importing of modules this way
sys.path.insert(0, './../GraphBuilder')
from GraphBuilder import EdgeGraph
from Interface import MetricsExtractor


# find the number of nodes in the graph
class GetNumberOfNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        return len(graph.edges)


# find the number of edges in the graph
class GetNumberOfEdges(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        count = 0
        for i in graph.edges:
            if i:
                for j in i.neighbours:
                    count += 1

        return count // 2


# finds the degree distribution, returns an array of degrees
# where the station number is the index
# and the value at index is the degree of that station
class GetDegreeDistribution(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        degree_distributions = []

        for i in graph.edges:
            if i:
                degree_distributions.append(len(i.neighbours))

        return degree_distributions


# returns the average degree of all the nodes in the graph
class GetAverageDegreeNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        s = 0
        for i in graph.edges:
            if i:
                s += len(i.neighbours)

        return s // len(graph.edges)
