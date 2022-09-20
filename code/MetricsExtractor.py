from abc import ABC, abstractmethod
# strategy pattern to choose metric extractors


class Selector():
    def setMetricsExtractor(self, metrics_extractor):
        self.metrics_extractor = metrics_extractor

    def executeMetricsExtractor(self):
        return self.metrics_extractor.get_metric()


class MetricsExtractor(ABC):

    @abstractmethod
    def get_metric(self, graph):
        pass


class GetNumberOfNodes(MetricsExtractor):
    def get_metric(self, graph):
        return "the number of nodes in the graph"


class GetNumberOfEdges(MetricsExtractor):
    def get_metric(self, graph):
        return "the number of edges in the graph"


class GetAverageDegree(MetricsExtractor):
    def get_metric(self, graph):
        return "the average degree of each node"
