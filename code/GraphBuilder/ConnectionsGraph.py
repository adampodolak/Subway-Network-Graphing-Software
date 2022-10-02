from GraphInterface import Graph
import csv

class ConnectionsGraph(Graph):

    def __init__(self):
        self.type = "connections"

    def format_csv_file(self, csv_file):
        self.edges = []
        with open(csv_file) as connections:
            csv_reader = csv.reader(connections, delimiter=',')
            for row in csv_reader:
                self.edges.append(row)

            self.edges.pop(0)
        return self.edges

    def find_max(self, csv):
        l = self.format_csv_file(csv)
        max = int(l[0][0])
        for i in l:
            if int(i[0]) > max:
                max = int(i[0])

        return max