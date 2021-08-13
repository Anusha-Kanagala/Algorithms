# Create a class Node
class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0
        self.d = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.g < other.g

    def __str__(self):
        return self.name + ' ' + str(self.g)

    def __cmp__(self, other):
        return cmp(self.h, other.h)
