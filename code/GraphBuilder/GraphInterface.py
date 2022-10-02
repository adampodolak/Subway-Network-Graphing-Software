from abc import ABC, abstractmethod


class Graph(ABC):

    @abstractmethod
    def format_csv_file(self, csv_file):
        pass

    @abstractmethod
    def find_max(self):
        pass