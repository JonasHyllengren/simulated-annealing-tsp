from anneal import SimAnneal
import matplotlib.pyplot as plt
import random

def read_edges(path):

    edges = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = [float(x.replace("\n", "")) for x in line.split(" ")]
            edges.append(line)
        N = len(edges)
        # squarify
        for i in range(0,N):
            edges[i] = edges[i] + (N-i-1)*[0.0]
            print(edges[i])
    return edges

def generate_random_coords(num_nodes):
    return [[random.uniform(-1000, 1000), random.uniform(-1000, 1000)] for i in range(num_nodes)]


if __name__ == "__main__":
    edges = read_edges("edges.txt")  # generate_random_coords(100)
    sa = SimAnneal(edges, stopping_iter=5000)
    sa.anneal()
    sa.visualize_routes()
    sa.plot_learning()
