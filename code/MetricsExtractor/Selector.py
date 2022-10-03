from Interface import MetricsExtractor
import sys
sys.path.insert(0, './../GraphBuilder')
from GraphBuilder import EdgeGraph


# selector class to allow us to select and execute metrics extractos
class Selector():
    def set_metrics_extractor(self, metrics_extractor: MetricsExtractor):
        self.metrics_extractor = metrics_extractor

    def execute(self, graph: EdgeGraph):
        return self.metrics_extractor.get_metric(graph)
