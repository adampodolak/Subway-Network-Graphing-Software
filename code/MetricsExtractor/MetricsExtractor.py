
from abc import ABC, abstractmethod
import sys
sys.path.insert(0, './../GraphBuilder')
from GraphBuilder import EdgeGraph

class MetricsExtractor(ABC):

    @abstractmethod
    def get_metric(self, graph):
        pass


class Selector():
    def set_metrics_extractor(self, metrics_extractor: MetricsExtractor):
        self.metrics_extractor = metrics_extractor

    def execute(self, graph: EdgeGraph):
        return self.metrics_extractor.get_metric(graph)


class GetNumberOfNodes(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        return len(graph.edges)


class GetNumberOfEdges(MetricsExtractor):
    def get_metric(self, graph: EdgeGraph):
        count = 0
        for i in graph.edges:
<<<<<<< HEAD:code/MetricsExtractor.py
            for j in i.neighbours:
                count += 1
=======
            if i:
                for j in i.neighbours:
                    count += 1

>>>>>>> ce62144d6605b596b42adbc3977e2dd860ce1a48:code/MetricsExtractor/MetricsExtractor.py
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
