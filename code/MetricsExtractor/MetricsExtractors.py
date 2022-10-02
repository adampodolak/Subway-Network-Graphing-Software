
import sys
sys.path.insert(0, './../GraphBuilder')
from GraphBuilder import EdgeGraph
from Interface import MetricsExtractor


class GetNumberOfNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        return len(graph.edges)


class GetNumberOfEdges(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        count = 0
        for i in graph.edges:
<<<<<<< HEAD:code/MetricsExtractor/MetricsExtractor.py
            for j in i.neighbours:
                count += 1
=======
            if i:
                for j in i.neighbours:
                    count += 1

>>>>>>> 55d0a3898ce99cb34eaff67ec3f0f0df3707be5a:code/MetricsExtractor/MetricsExtractors.py
        return count // 2


class GetDegreeDistribution(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        degree_distributions = []

        for i in graph.edges:
            if i:
                degree_distributions.append(len(i.neighbours))

        return degree_distributions


class GetAverageDegreeNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        s = 0
        for i in graph.edges:
            if i:
                s += len(i.neighbours)

        return s // len(graph.edges)
