from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.datasets import make_blobs
import networkx as nx
import community  # 需要安装 python-louvain 库，可以使用 pip install python-louvain 进行安装

# 导入 Les Miserables Co-Appearance Network 数据集
G = nx.les_miserables_graph()
print(G.nodes)
# 使用 Louvain 算法检测社团结构
partition = community.best_partition(G)

# 打印每个节点所属的社团
for node, comm in partition.items():
    print(f"Node {node} belongs to community {comm}")

# 绘制网络图，并根据社团进行着色
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # 使用 Spring layout 布局绘制图形
nx.draw(G, pos, with_labels=True, node_color=list(partition.values()), cmap=plt.cm.tab10, node_size=3000, edge_color='gray', linewidths=1, font_size=10)
plt.title("Les Miserables Co-Appearance Network with Louvain Community Detection")
plt.show()
