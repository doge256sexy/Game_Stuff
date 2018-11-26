__author__ = 'Gregorio Manabat III'
import sys
import math

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

class KMeansController:
    def __init__(self, balls, clusters, cluster_func, threshold):
        self.balls = balls
        self.k_means_clusters = []
        self.cluster_cap = clusters
        self.cluster_func = cluster_func
        self.threshold = threshold

    def update_points(self):

        for point in self.balls:
            closest = sys.maxsize
            closest_cluster = None
            for cluster in self.k_means_clusters:
                distance = dist((point.x, point.y), cluster.average)
                if distance < closest:
                    closest = distance
                    closest_cluster = cluster
            point.category = closest_cluster.category
            closest_cluster.weights.append(point)

    def update_clusters(self):
        for cluster in self.k_means_clusters:
            cluster.update()
            cluster.weights.clear()

    def create(self):
        for i in range(self.cluster_cap):
            self.k_means_clusters.append(KMeansCluster(*self.cluster_func(), parent=self))

class KMeansCluster:

    def __init__(self, tag, x, y, parent):
        self.category = tag
        self.weights = []
        self.average = (x, y)
        self.parent = parent

    def update(self):
        if len(self.weights) < self.parent.threshold:
            self.parent.k_means_clusters.remove(self)
            return
        ave = 0 + 0j
        heavy = 0
        for weight in self.weights:
            ave += complex(weight.x, weight.y) * weight.radius ** 2
            heavy += weight.radius ** 2
        ave /= heavy
        new_average = (ave.real, ave.imag)
        self.average = new_average