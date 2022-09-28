from graph import *
from GraphFactory import *
from PathfinderFactory import *
import random


def build_dataset(num_of_samples):
    dataset = {}

    for i in range(1, num_of_samples):
        dataset["{0}".format(i)] = random.sample(range(1, 303), 2)

    return dataset


def multi_pathfind(pathfinder: PathfinderAlgorithm, graph: EdgeGraph, dataset: dict, kpi: str):
    result = {}
    for key in dataset.keys():
        s1 = key[0]
        s2 = key[1]
        result[key] = pathfinder.call(graph, s1, s2)[kpi]

    return result


def create_dijkstras():
    # create a dijkstras PathfinderAlgorithm
    pass


def create_astart():
    # create a_start PathfinderAlgorithm that you will pass into multi_pathfind
    pass


def measure_nodes():
    # implement something that measures the number of nodes for both dijkstras and a*
    pass


def measure_edges():
    pass


def measure_travel_time():
    pass
