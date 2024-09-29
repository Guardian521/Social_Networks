import networkx as nx
import numpy as np
import random
from sklearn.cluster import DBSCAN
import time
import matplotlib.pyplot as plt

def modularity(G, clusters):
    m = G.size(weight='weight')
    Q = 0
    for cluster in clusters:
        cluster_edges = G.subgraph(cluster).size(weight='weight')
        cluster_degrees = sum(dict(G.degree(cluster)).values())
        Q += cluster_edges / m - (cluster_degrees / (2 * m)) ** 2
    return Q


def kmeans_dbscan(data, k, max_iterations=50, epsilon=0.5, min_samples=5):
    center_indices = random.sample(range(len(data)), k)
    center_points = [data[i] for i in center_indices]

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        # kmeans
        for point in data:
            distances = [np.abs(point - centroid) for centroid in center_points]
            cluster_index = np.argmin(distances)

            # 检查索引是否越界
            if cluster_index < len(clusters):
                clusters[cluster_index].append(point)
            else:
                print(f"Warning: Index out of range for cluster {cluster_index}")
                continue

        new_center_points = [np.mean(cluster, axis=0) for cluster in clusters]

        # 计算模块度增量
        prev_modularity = modularity(G, clusters)
        new_modularity = modularity(G, clusters)
        delta_modularity = new_modularity - prev_modularity

        if delta_modularity > 0:
            center_points = new_center_points
        else:
            clustering = DBSCAN(eps=epsilon, min_samples=min_samples).fit(data.reshape(-1, 1))
            labels = clustering.labels_
            unique_labels = set(labels)
            clusters = [[] for _ in range(len(unique_labels))]
            for i, label in enumerate(labels):
                clusters[label].append(data[i])
            center_points = [np.mean(cluster, axis=0) for cluster in clusters if cluster]

    return clusters, center_points


G = nx.les_miserables_graph()
# 提取节点度作为特征向量
node_degrees = np.array([val for (node, val) in G.degree()])

# 基于模块度优化的K均值与DBSCAN混合聚类算法
k = 6
begin_time=time.time()
clusters, centroids = kmeans_dbscan(node_degrees, k)
end_time=time.time()

print('time:',end_time-begin_time)

#画图
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color=[i for i, c in enumerate(clusters) for _ in c], cmap=plt.cm.tab10, node_size=3000, edge_color='gray', linewidths=1, font_size=10)
plt.title("Les Miserables Co-Appearance Network with Louvain Community Detection")
plt.show()