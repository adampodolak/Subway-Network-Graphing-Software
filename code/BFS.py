#not needed
class DFS:
    def __init__(self, maxTime,desiredNode) -> None:
        self.visited = [] # List to keep track of visited nodes.
        self.path = []
        self.maxTime = maxTime
        self.desiredNode = desiredNode
        self.check = True
        

    def dfs(self, graph, node, curTime):  #function for dfs 
        #check if we visited the node, or time with the node exceeds original time found
        # print("next")
        # print("current node: " + str(node.id))
        if node not in self.visited and self.maxTime >= int(node.time) + curTime:
            self.visited.append(node)
            curTime += int(node.time)
            #print(*self.path, sep='-->')

            #check for duplicates
            if node.id not in self.path:
                self.path.append(node.id)
            else:
                #print("looped")
                return

            #check if we found the desired node
            if node.id == self.desiredNode.id:
                self.check = False
                print("found the end")
                return 

            #recurse down for neighbours
            for neighbour in graph.edges[int(node.id)-1].neighbours:
                if self.check:
                    self.dfs(graph, neighbour,curTime)
                else:
                    return
            
            #if we reach down here, the node will not lead to the desired node
            if self.check:
                self.path.pop()
                curTime -= int(node.time)

    