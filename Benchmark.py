import sys
import random
# flake8 is returning E402 here but,
# there is no other way to format the importing of modules this way
sys.path.insert(0, './code/GraphBuilder')
from GraphBuilder import EdgeGraph
sys.path.insert(0, './code/Pathfinder')
from PathfinderFactory import PathfinderFactory
from PathfinderInterface import PathfinderAlgorithm


# building the dataset
# dataset is a random sample of 2 random nodes/stations
def build_dataset(num_of_samples):
    dataset = {}

    for i in range(0, num_of_samples):
        dataset["{0}".format(i)] = random.sample(range(1, 303), 2)

    return dataset


# method to return specified KPI
def multi_pathfind(
        pathfinder: PathfinderAlgorithm,
        graph: EdgeGraph, dataset: dict, kpi: str):
    result = {}
    for key in dataset:
        s1 = dataset[key][0]
        s2 = dataset[key][1]
        result[key] = pathfinder.call(graph, s1, s2)[kpi]

    return result


# method to create a dijkstras pathfinder
def create_dijkstras():
    pathfinder = PathfinderFactory()
    dijkstras = pathfinder.create_pathfinder("dijkstras")
    return dijkstras


# method to create an A* pathfinder
def create_astar():
    pathfinder = PathfinderFactory()
    a_star = pathfinder.create_pathfinder("a*")
    return a_star
