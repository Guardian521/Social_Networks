from pyecharts import options as opts
from pyecharts.charts import Graph

# 读取节点数据文件
with open("/Users/gushuai/Desktop/bnodes.csv", "r") as f:
    node_lines = f.readlines()

# 读取边数据文件
with open("/Users/gushuai/Desktop/bedges.csv", "r") as f:
    edge_lines = f.readlines()

# 提取节点和边的数据
nodes = []
links = []

for line in node_lines[1:]:  # 跳过标题行
    node_info = line.strip().split(",")  # 按逗号分割节点信息
    if node_info[1] != 'NULL':  # 如果节点大小不是 'NULL'
        nodes.append(opts.GraphNode(name=node_info[0], symbol_size=int(node_info[1])))  # 添加节点，并指定节点大小
    else:
        nodes.append(opts.GraphNode(name=node_info[0], symbol_size=30))  # 使用默认节点大小

for line in edge_lines[1:]:  # 跳过标题行
    edge_info = line.strip().split(",")  # 按逗号分割边信息
    # 添加边
    links.append({"source": edge_info[0], "target": edge_info[1]})

# 创建一个Graph实例
graph = Graph()

# 设置图表的全局配置项
graph.set_global_opts(
    title_opts=opts.TitleOpts(title="学生食堂消费网络"), # 设置标题
    legend_opts=opts.LegendOpts(is_show=False), # 不显示图例
)

# 设置图表的系列配置项
graph.add(
    "",
    nodes,
    links,
    layout="force", # 设置布局为环形
    is_rotate_label=True, # 设置标签旋转
    linestyle_opts=opts.LineStyleOpts(color="red", width=2, curve=0.3), # 设置线条样式，颜色根据源节点，曲度为0.3
    label_opts=opts.LabelOpts(position="right"), # 设置标签位置为右侧

)

# 渲染图表
graph.render("network_graph_real_data.html")
