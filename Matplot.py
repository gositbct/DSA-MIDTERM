import math
import matplotlib.pyplot as plt

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