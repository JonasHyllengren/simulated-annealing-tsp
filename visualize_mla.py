import matplotlib.pyplot as plt

def plot_hanging_line(point1, point2):
    import numpy as np

    a = point1[0]
    b = point2[0]

    x = np.linspace(a, b, 100)
    y = np.sin( np.pi*(x-a)/(a-b) ) / (a-b)

    plt.plot(x,y)

def plotTSP(nodes, edges, num_iters=1):

    """
    nodes: List with the ordering of the nodes
    edges: edges between the different nodes
    num_iters: number of paths that are in the path list
    """
    nodes = nodes[0]
    N = len(nodes)

    print(nodes)

    plt.plot(range(N),[0.0]*N,'co')
    for i in range(1,N):
        # Draw edges to earlier nodes
        for j in range(0,i):
            if edges[max(nodes[i],nodes[j])][min(nodes[i],nodes[j])] != 0:
                #plt.arrow(i, 0, j, 0, head_width = a_scale, color = 'g', length_includes_head = True)
                plot_hanging_line([i,0],[j,0])


    """
    # Unpack the primary TSP path and transform it into a list of ordered
    # coordinates

    x = []; y = []
    for i in paths[0]:
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x, y, 'co')

    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x))/float(100)

    # Draw the older paths, if provided
    if num_iters > 1:

        for i in range(1, num_iters):

            # Transform the old paths into a list of coordinates
            xi = []; yi = [];
            for j in paths[i]:
                xi.append(points[j][0])
                yi.append(points[j][1])

            plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]),
                    head_width = a_scale, color = 'r',
                    length_includes_head = True, ls = 'dashed',
                    width = 0.001/float(num_iters))
            for i in range(0, len(x) - 1):
                plt.arrow(xi[i], yi[i], (xi[i+1] - xi[i]), (yi[i+1] - yi[i]),
                        head_width = a_scale, color = 'r', length_includes_head = True,
                        ls = 'dashed', width = 0.001/float(num_iters))

    # Draw the primary path for the TSP problem
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale,
            color ='g', length_includes_head=True)
    for i in range(0,len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                color = 'g', length_includes_head = True)

    """

    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(0-1.1, N+1.1)
    plt.ylim(0-1.1, 0+1.1)
    plt.show()
