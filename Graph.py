import math

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))

    def prim(self):
        import heapq
        if not self.adj:
            return []
        start = list(self.adj.keys())[0]
        visited = set([start])
        pq = [(w, start, v) for v, w in self.adj[start]]
        heapq.heapify(pq)
        mst = []
        while pq:
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            mst.append((u, v, w))
            for x, wx in self.adj[v]:
                if x not in visited:
                    heapq.heappush(pq, (wx, v, x))
        return mst

    def dijkstra(self, src):
        import heapq
        dist = {n: math.inf for n in self.adj}
        prev = {n: None for n in self.adj}
        if src not in dist:
            return {}, {}
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    def kruskal(self):
        parent = {}
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                if (v, u, w) not in edges:
                    edges.append((u, v, w))
        edges.sort(key=lambda x: x[2])
        for n in self.adj:
            parent[n] = n
        mst = []
        for u, v, w in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, w))
        return mst