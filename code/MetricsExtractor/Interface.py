from abc import ABC, abstractmethod


class MetricsExtractor(ABC):

    @abstractmethod
    def get_metric(self, graph):
        pass
