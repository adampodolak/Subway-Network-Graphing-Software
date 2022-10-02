class TSalesman():
    def __init__(self) -> None:
        self.routes = []
        self.remember = []
        self.overlap = {}

    def find(self, graph, stationID, validStationsID):
        station,validStations = TSalesman.format(stationID,validStationsID,graph)
        isConnected = TSalesman.connected(validStationsID,validStations)

        self.remember = [station]

        for i in validStationsID:
            self.overlap[i] = [i]

        if isConnected:
            self.find_paths(station, validStations, [], 0)
            self.routes.sort()
            pathNums = []
            for i in self.routes[0][1]:
                pathNums.append(i.id)
            if len(self.routes) != 0:
                print ("Shortest route: ")
                print (pathNums)
                print (self.routes[0][0])
            else:
                print ("FAIL!")
        else:
            print("invalid set of nodes")

    def format(station,validStations,graph):
        station = graph.edges[station-1]
        Fstations = []
        for i in validStations:
            if graph.edges[i-1]:
                Fstations.append(graph.edges[i-1])
        return station, Fstations
  
    def connected(validStationsID,validStations):
        for i in validStations:
            foundNeighbour = False
            for j in i.neighbours:
                if j in validStationsID:
                    foundNeighbour = True
                    break
            if foundNeighbour == False:
                return False
        return True

     m 
                    

    def find_paths(self, station, validStations, path, distance):

        path.append(station)
        print(station.id)

        look = []
        for i in path:
            look.append(i.id)
        print (look)

        if len(path)>1:
            index = station.neighbours.index(int(path[-2].id))
            distance += int(station.time[index])

        complete = True
        for i in validStations:
            if i not in path:
                complete = False
        
        if complete and (int(path[0].id) in station.neighbours) :
            print ('here')
            path.append(path[0])
            self.routes.append([distance,path])
            return 

        deadEnd = True
        for i in validStations:
            if (int(i.id) not in self.overlap[int(station.id)]) and (int(i.id) in station.neighbours) and (int(i.id) != int(self.remember[-1].id)):
                self.remember.append(station)
                self.overlap[int(station.id)].append(int(i.id))
                self.find_paths(i, validStations, path, distance)
                deadEnd = False
              
        if deadEnd:
            self.find_paths(self.remember.pop(), validStations, path, distance)






        # # Add way point
        # print(count)
        # path.append(station)
        # pathNums = []
        # for i in path:
        #     pathNums.append(i.id)
        # print (pathNums)
        

        # # Calculate path length from current to last station
        # if len(path) > 1:
        #     index = station.neighbours.index(int(path[-2].id))
        #     distance += int(station.time[index])

        # # If path contains all validStations and is not a dead end,
        # # add path from last to first city and return.
        #     check = True
        #     for i in validStations:
        #         if i not in path:
        #             check = False
            
        #     if (int(station.id) in path[-2].neighbours) and check:
        #         path.append(path[0])
        #         pathNums.append(path[-1].id)
        #         index = station.neighbours.index(int(path[-1].id))
        #         distance += int(station.time[index])
        #         print(pathNums, distance)
        #         self.routes.append([distance, path])
        #         path.pop()
        #         path.pop()
                
        #         return path

        # # Fork paths for all possible validStations not yet used
        # count+=1
        # for s in validStations:
        #     noWay = True
        #     if (s not in path) and (int(station.id) in s.neighbours): 
        #         path = self.find_paths(s, validStations, path, distance,count)
        #         noWay = False
        
        # if noWay:
        #      path = self.find_paths(path[-2],validStations, path, distance, count)
        
        
        # return path








# """
#     Author: Simon Westphahl <westphahl@gmail.com>
#     Description: Brute-force implementation for solving the TSP.
#     http://en.wikipedia.org/wiki/Travelling_salesman_problem
# """

# routes = []


# def find_paths(station, validStations, path, distance):
#     # Add way point
#     path.append(station)

#     # Calculate path length from current to last station
#     if len(path) > 1:
#         distance += validStations[path[-2]][station]

#     # If path contains all validStations and is not a dead end,
#     # add path from last to first city and return.
#     if (len(validStations) == len(path)) and (validStations[path[-1]].has_key(path[0])):
#         global routes
#         path.append(path[0])
#         distance += validStations[path[-2]][path[0]]
#         print path, distance
#         routes.append([distance, path])
#         return

#     # Fork paths for all possible validStations not yet used
#     for city in validStations:
#         if (city not in path) and (validStations[city].has_key(station)):
#             find_paths(city, dict(validStations), list(path), distance)


# if __name__ == '__main__':
#     validStations = {
#         'RV': {'S': 195, 'UL': 86, 'M': 178, 'BA': 180, 'Z': 91},
#         'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
#         'M': {'RV': 178, 'UL': 123, 'N': 170},
#         'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210, 'MA': 135, 'KA': 64},
#         'N': {'S': 210, 'UL': 171, 'M': 170, 'MA': 230, 'F': 230},
#         'F': {'N': 230, 'S': 210, 'MA': 85},
#         'MA': {'F': 85, 'N': 230, 'S': 135, 'KA': 67},
#         'KA': {'MA': 67, 'S': 64, 'BA': 191},
#         'BA': {'KA': 191, 'RV': 180, 'Z': 85, 'BE': 91},
#         'BE': {'BA': 91, 'Z': 120},
#         'Z': {'BA': 120, 'BE': 85, 'RV': 91}
#     }

#     print "Start: RAVENSBURG"
#     find_paths('RV', validStations, [], 0)
#     print "\n"
#     routes.sort()
#     if len(routes) != 0:
#         print "Shortest route: %s" % routes[0]
#     else:
#         print "FAIL!"