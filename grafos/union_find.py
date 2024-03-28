class UnionFind:
    def __init__(self, elems):
        #self.groups = {e: e for e in elems}
        self.groups = {}
        for e in elems:
            self.groups[e] = e

    def find(self, v):
        if self.groups[v] == v:
            return v

        real_group = self.find(self.groups[v])
        # plancho la estructura
        self.groups[v] = real_group
        return real_group

    def union(self, u, v):
        new_group = self.find(u)
        other = self.find(v)
        self.groups[other] = new_group
