from abc import ABC, abstractmethod


class MetricsExtractor(ABC):

    # abstract method that takes in a graph
    # can be implemented to compute any metric relating to the graph
    @abstractmethod
    def get_metric(self, graph):
        pass
