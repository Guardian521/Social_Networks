import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
list_nodes = list(range(1, 21))
G.add_nodes_from(list_nodes)
# 每个节点和其后两个节点相连
for i in range(len(list_nodes)):
    G.add_edge(list_nodes[i], list_nodes[(i + 1) % len(list_nodes)])
    G.add_edge(list_nodes[i], list_nodes[(i + 2) % len(list_nodes)])
#邻接矩阵
import pandas as pd
ad_matrix=nx.adjacency_matrix(G).todense()#邻接矩阵
print(ad_matrix)
ad_matrix=pd.DataFrame(ad_matrix) #转为dataframe格式
ad_matrix.to_csv('adjacency_matrix.csv')#存储为csv
#绘图
pos = nx.spring_layout(G, iterations=1000)
plt.figure(figsize=(20, 16))
nx.draw_networkx(G, pos, node_color=range(20), node_size=1700, cmap=plt.cm.Greens)#渐变蓝
plt.show()