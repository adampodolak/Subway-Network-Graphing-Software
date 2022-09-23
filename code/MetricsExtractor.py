from abc import ABC, abstractmethod
from graph import *
from GraphFactory import *

# strategy pattern to choose metric extractors


class Selector():
    def setMetricsExtractor(self, metrics_extractor):
        self.metrics_extractor = metrics_extractor

    def executeMetricsExtractor(self, graph):
        return self.metrics_extractor.get_metric(graph)


class MetricsExtractor(ABC):

    @abstractmethod
    def get_metric(self, graph):
        pass


class GetNumberOfNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        return len(graph.edges)


class GetNumberOfEdges(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        count = 0
        for i in graph.edges:
            for j in i.neighbours:
                count += 1

        return count // 2


class GetDegreeDistribution(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        degree_distributions = []

        for i in graph.edges:
            degree_distributions.append(len(i.neighbours))

        return degree_distributions


class GetAverageDegreeNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        s = 0
        for i in graph.edges:
            s += len(i.neighbours)

        return s // len(graph.edges)
