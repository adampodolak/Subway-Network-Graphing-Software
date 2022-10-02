class TSalesman():
    def __init__(self) -> None:
        self.routes = []
        self.remember = []
        self.overlap = {}

    def find(self, graph, stationID, validStationsID):
        station, validStations = TSalesman.format(
            stationID, validStationsID, graph)
        isConnected = TSalesman.connected(validStationsID, validStations)

        self.remember = [station]

        for i in validStationsID:
            self.overlap[i] = []

        if isConnected:
            self.find_paths(station, validStations, [], 0)
            self.routes.sort()
            pathNums = []
            for i in self.routes[0][1]:
                pathNums.append(i.id)
            if len(self.routes) != 0:
                print("Shortest route: ")
                print(pathNums)
                print(self.routes[0][0])
            else:
                print("FAIL!")
        else:
            print("invalid set of nodes")

    def format(station, validStations, graph):
        station = graph.edges[station-1]
        Fstations = []
        for i in validStations:
            if graph.edges[i-1]:
                Fstations.append(graph.edges[i-1])
        return station, Fstations

    def connected(validStationsID, validStations):
        for i in validStations:
            foundNeighbour = False
            for j in i.neighbours:
                if j in validStationsID:
                    foundNeighbour = True
                    break
            if not foundNeighbour:
                return False
        return True

    def find_paths(self, station, validStations, path, distance):
        path.append(station)
        print(station.id)

        if len(path) > 1:
            index = station.neighbours.index(int(path[-2].id))
            distance += int(station.time[index])

        complete = True
        for i in validStations:
            if i not in path:
                complete = False

        if complete and (int(path[0].id) in station.neighbours):
            path.append(path[0])
            self.routes.append([distance, path])
            return

        deadEnd = True
        for i in validStations:
            if (i.id not in self.overlap[int(station.id)]) and (
                int(i.id) in station.neighbours) and (
                    int(i.id) != int(self.remember[-1].id)):
                self.remember.append(station)
                self.overlap[int(station.id)].append(i.id)
                self.find_paths(i, validStations, path, distance)
                deadEnd = False

        if deadEnd:
            self.find_paths(self.remember.pop(), validStations, path, distance)
