from ConnectionsGraph import ConnectionsGraph
from StationsGraph import StationsGraph


class GraphFactory():

    # static method that returns a concrete graph
    @staticmethod
    def build_graph(csv_file_type):
        try:
            if csv_file_type == "connections":
                return ConnectionsGraph()
            if csv_file_type == "stations":
                return StationsGraph()
        except AssertionError as e:
            print(e)
