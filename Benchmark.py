from GraphBuilder import *
from GraphFactory import *
from PathfinderFactory import *
import random


def build_dataset(num_of_samples):
    dataset = {}

    for i in range(0, num_of_samples):
        dataset["{0}".format(i)] = random.sample(range(1, 303), 2)

    return dataset


def multi_pathfind(pathfinder: PathfinderAlgorithm, graph: EdgeGraph, dataset: dict, kpi: str):
    result = {}
    for key in dataset:
        s1 = dataset[key][0]
        s2 = dataset[key][1]
        result[key] = pathfinder.call(graph, s1, s2)[kpi]

    return result


def create_dijkstras():
    pathfinder = PathfinderFactory()
    dijkstras = pathfinder.create_pathfinder("dijkstras")
    return dijkstras


def create_astar():
    pathfinder = PathfinderFactory()
    a_star = pathfinder.create_pathfinder("a*")
    return a_star
