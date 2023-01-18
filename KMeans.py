import matplotlib.pyplot as plot
from math import sqrt

x = [1, 4, 8, 10, 0, 7, 2, 5, 6, 3, 9, 4, 7, 8, 2, 5, 6, 1, 0, 3, 9, 10, 4, 5, 7, 8, 2, 6, 1, 0, 3, 9, 10, 4, 5, 7, 8,
     2, 6, 1, 0, 3, 9, 10, 4, 5, 7, 8, 2, 6]
y = [2, 8, 9, 5, 1, 7, 0, 6, 3, 4, 9, 8, 6, 3, 0, 1, 4, 7, 2, 5, 10, 8, 3, 5, 1, 9, 7, 6, 2, 0, 4, 10, 9, 6, 7, 5, 2, 0,
     8, 1, 3, 4, 10, 5, 3, 8, 9, 6, 2, 0, 7, 1, 4]
data = list(zip(x, y))
a, b = 4, 5


# for a in range(3,10):
#     pyplot.scatter(x,y)
#     pyplot.show()

def distance(aa, bb):
    return sqrt((aa[0] - bb[0]) ** 2 + (aa[1] - bb[1]) ** 2)


def find_centroid(points):
    if len(points) > 0:
        m1 = sum([e[0] for e in points]) / len(points)
        m2 = sum([e[1] for e in points]) / len(points)
        return m1, m2


def k_means():
    mean_1 = (8, 0)
    mean_2 = (x[9], y[9])
    m1tmp, m2tmp = (-1, -1), (-1, -1)

    while mean_1 != m1tmp or mean_2 != m2tmp:
        cluster_1 = []
        cluster_2 = []

        for p in range(len(data)):
            if distance(mean_1, data[p]) < distance(mean_2, data[p]):
                cluster_1.append(data[p])
            else:
                cluster_2.append(data[p])

        print(mean_1)
        print(mean_2)

        mean_1 = find_centroid(cluster_1)
        mean_2 = find_centroid(cluster_2)

        cluster_1_x, cluster_1_y = zip(*cluster_1)
        cluster_2_x, cluster_2_y = zip(*cluster_2)

        plot.scatter(cluster_1_x, cluster_1_y, color="r")
        plot.plot(mean_1[0], mean_1[1], marker="x", color="r")
        plot.scatter(cluster_2_x, cluster_2_y, color="b")
        plot.plot(mean_2[0], mean_2[1], marker="x", color="b")
        plot.grid()
        plot.show()


if __name__ == "__main__":
    k_means()
