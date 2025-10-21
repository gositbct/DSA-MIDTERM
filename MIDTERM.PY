# ...existing code...
import heapq
import matplotlib.pyplot as plt
import math

# -----------------------------
# Binary Search Tree (BST)
# -----------------------------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def find(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None

    def delete(self, key):
        def _min_node(n):
            while n.left:
                n = n.left
            return n
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = _min_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)

    def replace(self, old, new):
        if self.find(old):
            self.delete(old)
            self.insert(new)
            return True
        return False

    def inorder(self):
        result = []
        def _in(n):
            if n:
                _in(n.left)
                result.append(n.key)
                _in(n.right)
        _in(self.root)
        return result

    def preorder(self):
        result = []
        def _pre(n):
            if n:
                result.append(n.key)
                _pre(n.left)
                _pre(n.right)
        _pre(self.root)
        return result

    def postorder(self):
        result = []
        def _post(n):
            if n:
                _post(n.left)
                _post(n.right)
                result.append(n.key)
        _post(self.root)
        return result

# -----------------------------
# Heap (Min or Max)
# -----------------------------
class Heap:
    def __init__(self, mode='max'):
        self.mode = mode
        self.data = []

    def insert(self, val):
        heapq.heappush(self.data, -val if self.mode == 'max' else val)

    def pop(self):
        if not self.data:
            return None
        val = heapq.heappop(self.data)
        return -val if self.mode == 'max' else val

    def list(self):
        return [-x if self.mode == 'max' else x for x in self.data]

# -----------------------------
# Graph Algorithms
# -----------------------------
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

# -----------------------------
# Visualization helpers
# -----------------------------
def plot_bst(root):
    def _plot(node, x, y, dx):
        if not node:
            return
        plt.text(x, y, str(node.key), ha='center', va='center',
                 bbox=dict(facecolor='white', edgecolor='black'))
        if node.left:
            plt.plot([x, x - dx], [y - 1, y - 2], 'k-')
            _plot(node.left, x - dx, y - 2, dx / 2)
        if node.right:
            plt.plot([x, x + dx], [y - 1, y - 2], 'k-')
            _plot(node.right, x + dx, y - 2, dx / 2)
    plt.figure()
    _plot(root, 0, 0, 4)
    plt.axis('off')
    plt.title("Binary Search Tree")
    plt.show()

def plot_heap(heap):
    vals = heap.list()
    if not vals:
        print("Heap is empty.")
        return
    plt.figure()
    for i, val in enumerate(vals):
        level = int(math.log2(i + 1))
        index_in_level = i - (2 ** level - 1)
        x = index_in_level / (2 ** level)
        y = -level
        plt.text(x, y, str(val), ha='center', va='center',
                 bbox=dict(facecolor='white', edgecolor='black'))
        if i != 0:
            parent = (i - 1) // 2
            level_p = int(math.log2(parent + 1))
            index_p = parent - (2 ** level_p - 1)
            x_p = index_p / (2 ** level_p)
            y_p = -level_p
            plt.plot([x_p, x], [y_p, y], 'k-')
    plt.axis('off')
    plt.title(f"{heap.mode.title()} Heap")
    plt.show()

# new: simple circular layout and plot_graph helper
def _circle_positions(nodes, radius=1.0, cx=0.0, cy=0.0):
    pos = {}
    n = len(nodes)
    if n == 0:
        return pos
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / n
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        pos[node] = (x, y)
    return pos

def plot_graph(graph, highlight_edges=None, highlight_nodes=None, title="Graph"):
    nodes = list(graph.adj.keys())
    if not nodes:
        print("Graph is empty.")
        return
    pos = _circle_positions(nodes, radius=1.2)
    plt.figure()
    ax = plt.gca()
    drawn = set()
    he_set = {frozenset((a, b)) for a, b, _ in (highlight_edges or [])}
    hn_set = set(highlight_nodes or [])
    for u in graph.adj:
        for v, w in graph.adj[u]:
            edge_id = frozenset((u, v))
            if edge_id in drawn:
                continue
            drawn.add(edge_id)
            x1, y1 = pos[u]; x2, y2 = pos[v]
            color = 'red' if edge_id in he_set else 'black'
            lw = 2.5 if edge_id in he_set else 1.0
            ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, zorder=1)
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx, my, str(w), fontsize=8, color='blue', zorder=2)
    for node in nodes:
        x, y = pos[node]
        face = 'orange' if node in hn_set else 'white'
        ax.scatter([x], [y], s=400, facecolors=face, edgecolors='black', zorder=3)
        ax.text(x, y, str(node), ha='center', va='center', zorder=4)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title(title)
    plt.show()

def main():
    bst = BST()
    heap_max = Heap('max')
    heap_min = Heap('min')
    graph = Graph()

    while True:
        print("\n******** MENU FOR NON-LINER DATA STRUCTURE ********")
        print("[0] QUIT")
        print("[1] ADD ITEMS – BSTREE / HEAP TREE")
        print("[2] EDIT ITEMS – BSTREE / HEAP TREE")
        print("[3] DELETE ITEMS FROM BSTREE")
        print("[4] DELETE ITEMS FROM HEAP TREE")
        print("[5] PRINT ITEMS FROM BSTREE (INORDER, PREORDER, POSTORDER)")
        print("[6] PRINT ITEMS FROM HEAP TREE (MAX & MIN)")
        print("[7] GRAPH PROBLEM USING PRIM’S ALGORITHM")
        print("[8] GRAPH PROBLEM USING DIJKSTRA’S ALGORITHM")
        print("[9] GRAPH PROBLEM USING KRUSKAL’S ALGORITHM")
        choice = input("Your choice (0–9): ")

        if choice == '0':
            print("Exiting program...")
            break

        elif choice == '1':
            again = 'y'
            while again == 'y':
                while True:
                    htype = input("Use (max) heap or (min) heap?: ").strip()
                    if htype.lower() == 'max' or htype == 'M':
                        heap = heap_max
                        last_heap_type = 'Max'
                        break
                    if htype.lower() == 'min' or htype == 'm':
                        heap = heap_min
                        last_heap_type = 'Min'
                        break
                    print("Please enter exactly 'M' (Max) or 'm' (Min), or type 'max' / 'min'.")
                val = int(input("Enter value to add: "))
                heap.insert(val)
                last_heap = heap
                again = input("Again (y/n)? ").lower()

        elif choice == '2':
            target = input("Edit (B)ST or (H)eap? ").lower()
            if target == 'b':
                old = int(input("Enter old value: "))
                new = int(input("Enter new value: "))
                if bst.replace(old, new):
                    print("BST updated:", bst.inorder())
                    plot_bst(bst.root)
                else:
                    print("Value not found.")
            else:
                print("Heap editing not directly supported. Use delete/insert instead.")

        elif choice == '3':
            again = 'y'
            while again == 'y':
                val = int(input("Enter value to delete from BST: "))
                bst.delete(val)
                print("BST updated:", bst.inorder())
                plot_bst(bst.root)
                again = input("Again (y/n)? ").lower()

        elif choice == '4':
            htype = input("Delete from (M)ax or (m)in heap? ").lower()
            heap = heap_max if htype == 'm' else heap_min
            again = 'y'
            while again == 'y':
                val = heap.pop()
                if val is None:
                    print("Heap empty.")
                    break
                print("Popped:", val)
                print("Heap now:", heap.list())
                plot_heap(heap)
                again = input("Again (y/n)? ").lower()

        elif choice == '5':
            mode = input("Traversal type (in/pre/post): ").lower()
            if mode == 'in':
                print("Inorder:", bst.inorder())
            elif mode == 'pre':
                print("Preorder:", bst.preorder())
            elif mode == 'post':
                print("Postorder:", bst.postorder())
            plot_bst(bst.root)

        elif choice == '6':
            print("Max Heap:", heap_max.list())
            print("Min Heap:", heap_min.list())
            plot_heap(heap_max)
            plot_heap(heap_min)

        elif choice == '7':
            n = int(input("Number of edges: "))
            graph = Graph()
            for _ in range(n):
                u, v, w = input("Enter edge (u v w): ").split()
                graph.add_edge(u, v, float(w))
            mst = graph.prim()
            print("Prim's MST edges:", mst)
            total = sum(w for _, _, w in mst)
            print("Total weight:", total)
            plot_graph(graph, highlight_edges=mst, title="Prim's MST")

        elif choice == '8':
            n = int(input("Number of edges: "))
            graph = Graph()
            for _ in range(n):
                u, v, w = input("Enter edge (u v w): ").split()
                graph.add_edge(u, v, float(w))
            src = input("Enter source node: ")
            dist, prev = graph.dijkstra(src)
            print("Dijkstra distances from", src, ":", dist)
            target = input("Enter target node to highlight path (or leave blank): ").strip()
            if target:
                if target not in prev:
                    print("Target not in graph.")
                else:
                    path = []
                    cur = target
                    while cur is not None:
                        path.append(cur)
                        cur = prev[cur]
                    path = path[::-1]
                    path_edges = [(path[i], path[i+1], 0) for i in range(len(path)-1)]
                    plot_graph(graph, highlight_edges=path_edges, highlight_nodes=path, title=f"Shortest path {src} -> {target}")
            else:
                plot_graph(graph, title="Graph (Dijkstra)")

        elif choice == '9':
            n = int(input("Number of edges: "))
            graph = Graph()
            for _ in range(n):
                u, v, w = input("Enter edge (u v w): ").split()
                graph.add_edge(u, v, float(w))
            mst = graph.kruskal()
            print("Kruskal's MST edges:", mst)
            total = sum(w for _, _, w in mst)
            print("Total weight:", total)
            plot_graph(graph, highlight_edges=mst, title="Kruskal's MST")

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()