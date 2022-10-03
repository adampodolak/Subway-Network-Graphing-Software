class ConnectedComponents():
    def setup(self):
        first = str(self.z-0.5)
        second = str(self.z+0.5)
        third = str(self.z)

        l_zones = {
            first: [],
            second: [],
            third: []
        }

        for i in self.graph.edges:
            if i:
                if i.zone == first:
                    l_zones[first].append(int(i.id))
                elif i.zone == second:
                    l_zones[second].append(int(i.id))
                elif i.zone == third:
                    l_zones[third].append(int(i.id))

        together = l_zones[first] + l_zones[second] + l_zones[third]

        return together

    def run(self, graph, z):
        self.graph = graph
        self.z = z
        self.together = self.setup()
        self.connecteds = []

        leave = True
        while leave:
            leave = False
            for i in self.together:
                if not self.graph.edges[i-1].marked:
                    leave = True
                    self.connecteds.append(
                        self.traverse(self.graph.edges[i-1], []))
                    break

        for i in graph.edges:
            if i:
                i.marked = False

        return self.connecteds

    def traverse(self, station, path):
        station.marked = True
        path.append(station.id)
        for i in station.neighbours:
            if i in self.together and (not self.graph.edges[i-1].marked):
                self.traverse(self.graph.edges[i-1], path)
        return path
