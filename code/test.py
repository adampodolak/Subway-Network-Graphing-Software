from PathfinderFactory import *


class testPaths():
    def __init__(self, graph, alg) -> None:
        self.graph = graph
        self.alg = alg

    def testPath1(self):
        # check path from station 11 to station 45
        self.alg.call(self.graph, 11, 45)
        assert self.alg.result["path"] == [11, 94, 282, 144, 207, 45]
        assert self.alg.result["nodes"] == 6
        assert self.alg.result["edges"] == 5
        assert self.alg.result["travel time"] == 21

    def testPath2(self):
        # check path from station 291 to station 222
        self.alg.call(self.graph, 291, 222)
        assert self.alg.result["path"] == [291, 210, 75, 222]
        assert self.alg.result["nodes"] == 4
        assert self.alg.result["edges"] == 3
        assert self.alg.result["travel time"] == 7

    def testPath3(self):
        # check path from station 1 to station 103
        self.alg.call(self.graph, 1, 303)
        assert self.alg.result["path"] == [1, 265, 110, 17, 74, 99, 236, 229, 273, 107, 192, 277, 89, 145, 123, 95, 160, 266, 303]
        assert self.alg.result["nodes"] == 19
        assert self.alg.result["edges"] == 18
        assert self.alg.result["travel time"] == 39

    def testPath4(self):
        # check path from station1 to station 1
        self.alg.call(self.graph, 1, 1)
        assert self.alg.result["path"] == [1]
        assert self.alg.result["nodes"] == 1
        assert self.alg.result["edges"] == 0
        assert self.alg.result["travel time"] == 0

    def testPath5(self):
        # check path from station -1(does not exist) to station 1
        self.alg.call(self.graph, -1, 1)
        assert self.alg.result["path"] == []
        assert self.alg.result["nodes"] == 0
        assert self.alg.result["edges"] == 0
        assert self.alg.result["travel time"] == 1000

    def testPath6(self):
        # check path from station 1 to station 400(does not exist)
        self.alg.call(self.graph, 1, 400)
        assert self.alg.result["path"] == []
        assert self.alg.result["nodes"] == 0
        assert self.alg.result["edges"] == 0
        assert self.alg.result["travel time"] == 1000

    def test_find_next_node(self):
        # check the closest node to station 71 from the neighbours of station 20
        path, end = self.alg.find_next_node(self.graph, self.graph.edges[20], [self.graph.edges[71]], False)
        hold = []
        for i in path:
            hold.append(i.id)
        assert hold == ['72', '286']

    def test_find_next_node_edge(self):
        # check the closest node to station 71 from the neighbours of station 20
        path, end = self.alg.find_next_node(self.graph, self.graph.edges[20], [self.graph.edges[71]], False)
        hold = []
        for i in path:
            hold.append(i.id)
        assert hold == ['72', '286']

    def test_find_neighbours(self):
        # find all neighbours of station 10
        q = self.alg.find_neighbours(graph, [self.graph.edges[10]], [])
        hold = []
        for i in q:
            hold.append(int(i.id))
        for i in graph.edges:
            if i:
                i.marked = False
        assert hold == [11, 163, 212, 83, 104, 28, 249, 94]


graph = main()

alg = PathfinderFactory()

d1 = alg.createPathfinder("dijkstras")
tester1 = testPaths(graph, d1)
tester1.testPath1()
tester1.testPath2()
tester1.testPath3()
tester1.testPath4()
tester1.testPath5()
tester1.testPath6()
tester1.test_find_neighbours()

a = alg.createPathfinder("a*")
testA = testPaths(graph, a)
testA.testPath1()
testA.testPath2()
# testA.testPath3()
testA.testPath4()
testA.testPath5()
testA.testPath6()
testA.test_find_next_node()
