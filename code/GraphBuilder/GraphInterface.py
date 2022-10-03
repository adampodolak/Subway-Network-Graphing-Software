from abc import ABC, abstractmethod


# graph interface
class Graph(ABC):

    # will be implemented by a concrete graph
    # formats the csv into a list of edges
    # can be implemented for any csv file format
    @abstractmethod
    def format_csv_file(self, csv_file):
        pass

    # finding the max number of stations
    # important for initializing the size of our graph array
    @abstractmethod
    def find_max(self):
        pass
