import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from networkx.algorithms import community


def Sum_Weight_edge():

    weightp={('key1','key7'):10}


    return weightp


def Girvan_Newman_algorithm(G, weight):
    weighttmp={('key1','key7'):10} #예시입니다.


    g=G.copy()

    old_max_m=0 #이전 최대 modularity 기억
    max_g=g.copy()
    k = sorted(nx.connected_components(G), key=len, reverse=True)   # k 는 모두 연결되어있는 Community를 노드로 나타낸 값
    
    k_list = []

    for j in range(len(k)): #0부터 len(k)까지의 객체를 만들어줌. 
        k_list = k_list + [list(k[j])]

    max_k = k_list  # max_k 는 modularity가 최대일 때의 k 값 저장용
    m = community.modularity(G, communities=k, weight=weight)   # modularity
    max_m = m       # max_m은 modularity가 최대일 때 값 기록용


    while len(g.edges()) > 0: #edges모두 지울때까지 반복
        k = sorted(nx.connected_components(g), key=len, reverse=True)  # 커뮤니티 추출
        m = community.modularity(G, communities=k, weight=weight)   # 추출된 커뮤니티의 modularity 계산

        if m > old_max_m:   # 이전 최대 modularity보다 현재 modularity가 높을 경우 기록
            max_g = g.copy()
            max_m = m
            k_list = []
            for j in range(len(k)):
                k_list = k_list + [list(k[j])]
            max_k = k_list
            old_max_m = m


        """ remove edge """
        betweenness = nx.edge_betweenness_centrality(g, weight=weight)  # betweennes centrality 계산

        
        max_edge = max(betweenness, key=betweenness.get)    # betweeness centrality가 가장 큰 Edge 선택
        g.remove_edge(max_edge[0], max_edge[1])     # Edge 추출

    return max_g, max_m, max_k

   

G=nx.Graph()


G.add_node('key1')
G.add_node('key2')
G.add_node('key3')
G.add_node('key4')
G.add_node('key5')
G.add_node('key6')
G.add_node('key7')

G.add_edge('key1','key2')
G.add_edge('key1','key3')
G.add_edge('key1','key4')
G.add_edge('key1','key5')
G.add_edge('key6','key7')
G.add_edge('key1','key7')
G.add_edge('key2','key4')





max_g, max_m, max_k = Girvan_Newman_algorithm(G, weight=None)   # weight='weight' : weighted network

pos = nx.spring_layout(G)
fig = plt.figure(figsize=(7, 6))

# max_k, 즉 Modularity 가 가장 높은 지점의 Community k 별로 색깔 설정



im = nx.draw_networkx_nodes(G, pos, node_size=10)
nx.draw_networkx_edges(max_g, pos)
nx.draw_networkx_labels(max_g, pos, font_size=10, font_color="black")
plt.xticks([])
plt.yticks([])
plt.show(block=True)
