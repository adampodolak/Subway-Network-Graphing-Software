import csv
import numpy as np


def format_data(file):
    edges = []
    temp = []
    with open(file) as connections:
        csv_reader = csv.reader(connections, delimiter=',')
        for row in csv_reader:
            edges.append(row)

        edges.pop(0)
    return edges


def count(csv):
    return (len(format_data(csv)))


def find_max(csv):
    l = format_data(csv)
    max = int(l[0][0])
    for i in l:
        if int(i[0]) > max:
            max = int(i[0])

    return max
