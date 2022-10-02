from PathfinderInterface import PathfinderAlgorithm
import math


class AstarDFS(PathfinderAlgorithm):
    def findpath(self, graph, s1, s2):
        # if start or end node not an actual station
        if s1 < 0 or s1 > len(graph.edges) or s2 < 0 or s2 > len(graph.edges):
            self.set(0, 0, 1000)
            return []

        if not graph.edges[s1-1] or not graph.edges[s2 - 1]:
            return []

        path = [graph.edges[s1-1]]
        end = False

        # if start and end node are the same
        if s1 == s2:
            end = True

        while not end:
            path, end = self.find_next_node(
                graph, graph.edges[s2-1], path, end)
            if end:
                break

        dist = self.find_distance(path)

        nodes = len(path)
        edges = nodes-1
        self.set(nodes, edges, dist)

        for i in graph.edges:
            if i:
                i.marked = False
        answer = []
        for i in path:
            answer.append(int(i.id))
        return answer

    def find_next_node(self, graph, s2, path, end):
        closestN = None
        relativeShort = 1000
        for i in path[len(path)-1].neighbours:
            if not graph.edges[i-1].marked:
                edge1 = float(s2.lat) - float(graph.edges[i-1].lat)
                edge2 = float(s2.long) - float(graph.edges[i-1].long)
                dist = math.hypot(edge1, edge2)

                if dist <= relativeShort:
                    relativeShort = dist
                    closestN = graph.edges[i-1]
                    if dist == 0:
                        end = True
                        break
        if closestN:
            closestN.marked = True
            path.append(closestN)
        else:
            path.pop()
        return path, end

    def find_distance(self, path):
        dist = 0
        for i in range(len(path)-1):
            t_index = path[i].neighbours.index(int(path[i+1].id))
            dist += int(path[i].time[t_index])
        return dist
