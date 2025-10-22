import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time

class graph_structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        """เพิ่ม edge แบบสองทิศทาง (undirected)"""
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        # ป้องกันการเพิ่มซ้ำ
        if neighbor not in self.graph[node]:
            self.graph[node].append(neighbor)
        if node not in self.graph[neighbor]:
            self.graph[neighbor].append(node)

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} -> {neighbors}")
        # วาดกราฟปกติ
        self.plot_graph(title="Graph Structure (full)")

    def plot_graph(self, highlight_nodes=None, title="Graph Structure", pause_time=0.6, final_show=True):

        if highlight_nodes is None:
            highlight_nodes = []

        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(6, 4))
        node_colors = []
        for n in G.nodes():
            if n in highlight_nodes:
                node_colors.append('lightcoral')   # โหนดที่ถูกไฮไลท์
            else:
                node_colors.append('skyblue')      # โหนดปกติ

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=12,
            font_weight='bold',
            edge_color="gray"
        )
        plt.title(title)
        if final_show:
            plt.show()
        else:
            plt.show(block=False)
            plt.pause(pause_time)
            plt.clf()

#bfs
    def bfs(self, start, animate=False, pause_time=0.6):
        print("=== Breadth-First Search ===")
        if start not in self.graph:
            print(f"Start node '{start}' not in graph.")
            return

        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                if animate:
                    self.plot_graph(highlight_nodes=[node], title=f"BFS visiting: {node}",
                                    pause_time=pause_time, final_show=False)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        print()
        if animate:
            self.plot_graph(title="BFS finished", final_show=True)

#dfs
    def dfs(self, start, animate=False, pause_time=0.6):
        print("=== Depth-First Search ===")
        if start not in self.graph:
            print(f"Start node '{start}' not in graph.")
            return

        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                if animate:
                    self.plot_graph(highlight_nodes=[node], title=f"DFS visiting: {node}",
                                    pause_time=pause_time, final_show=False)
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        print()
        if animate:
            self.plot_graph(title="DFS finished", final_show=True)


if __name__ == "__main__":
    g = graph_structure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    print("Graph Structure")
    g.show_graph()

    g.bfs('A', animate=False)

    g.dfs('A', animate=False)