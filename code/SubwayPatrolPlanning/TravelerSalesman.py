class TravellingSalesman():

    def __init__(self, graph, alg) -> None:
        self.graph = graph
        self.alg = alg

    def data(self, validStations):
        self.stationList = {}
        self.Paths = {}
        self.distances = {}

        for i in validStations:
            self.stationList[int(i.id)] = []
            self.Paths[int(i.id)] = []
            self.distances[int(i.id)] = []
            for j in validStations:
                if i != j:
                    self.stationList[int(i.id)].append(j.id)
                    self.alg.call(self.graph, int(i.id), int(j.id))
                    self.Paths[int(i.id)].append(self.alg.result["path"])
                    self.distances[int(i.id)].append(
                        self.alg.result["travel time"])

    def format(self, station, validStations):
        station = self.graph.edges[station-1]
        Fstations = []
        for i in validStations:
            if self.graph.edges[i-1]:
                Fstations.append(self.graph.edges[i-1])
        return station, Fstations

    def find(self, startID, validStationsID):
        self.length = len(validStationsID)
        self.startID = startID
        start, validStations = self.format(startID, validStationsID)
        self.data(validStations)

        path, time = self.perform(start, [startID], [], 0)
        print(path, time)

    def perform(self, start, history, path, time):
        neighbourIDs = self.stationList[int(start.id)]
        paths_to_neighbour = self.Paths[int(start.id)]
        travelTimes = self.distances[int(start.id)]

        if len(history) == self.length:
            index = neighbourIDs.index(str(self.startID))
            path += paths_to_neighbour[index]
            time += travelTimes[index]
            return path, time

        while True:
            index = travelTimes.index(min(travelTimes))
            if int(neighbourIDs[index]) in history:
                paths_to_neighbour.pop(index)
                neighbourIDs.pop(index)
                travelTimes.pop(index)
            else:
                break

        path += paths_to_neighbour[index]
        path.pop()
        time += travelTimes[index]
        history.append(int(neighbourIDs[index]))

        path, time = self.perform(
            self.graph.edges[int(neighbourIDs[index])-1], history, path, time)
        return path, time
