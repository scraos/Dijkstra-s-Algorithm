class Dgraph():
    def __init__(self):
        self.nodes = []
        self.arrows = []
        self.dists = {}

    def addnode(self,n):
        self.nodes.append(n)

    def addarrow(self,arrow,dist):
        self.arrows.append(arrow)
        self.dists[arrow] = dist

    def neighbors_of(self,node):
        set1 = []
        for i in self.arrows:
            if i[1] == node:
                set1.append(i[0])
            elif i[0] == node:
                set1.append(i[1])
        return set1

    def getLength(self, node1, node2):
        if (node1, node2) in self.arrows:
            return self.dists[(node1, node2)]
        elif (node2, node1) in self.arrows:
            return self.dists[(node2, node1)]