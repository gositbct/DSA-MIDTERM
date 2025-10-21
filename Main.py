from BSTree import *
from Graph import *
from Heap import *
from Matplot import *
import heapq
import matplotlib.pyplot as plt
import math

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
            t = input("Add to (B)ST or (H)eap?: ").strip().lower()
            if t == 'b':
                while True:
                    try:
                        v = int(input("Enter value: ").strip())
                    except ValueError:
                        print("Please enter an integer."); continue
                    bst.insert(v)
                    if input("Again (y/n)?: ").strip().lower() != 'y': break
                print("Done adding to BST.")
            else:
                while True:
                    h = input("Use (M)ax or (m)in heap?: ").strip()
                    if h == 'M' or h.lower() == 'max':
                        heap = heap_max; break
                    if h == 'm' or h.lower() == 'min':
                        heap = heap_min; break
                    print("Enter 'M' or 'm'.")
                while True:
                    try:
                        v = int(input("Enter value: ").strip())
                    except ValueError:
                        print("Please enter an integer."); continue
                    heap.insert(v)
                    if input("Again (y/n)?: ").strip().lower() != 'y': break
                print("Done adding to heap.")


        elif choice == '2':
            target = input("Edit (B)ST or (H)eap?: ").lower()
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