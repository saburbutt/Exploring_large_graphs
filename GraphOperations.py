import ReadGraphs as G
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G1_RoadNet = G.RoadNet_Graph
G2_Twitter = G.Twitter_Real_Graph


def Print_Graph_Info(G1,G2):
    print("Info of RoadNet", nx.info(G1))
    print("Info of Twitter Real graph", nx.info(G2))

def Get_Graph_Info(G1, G2):
    return nx.info(G1), nx.info(G2)


#Display the k-hop neighborhood of a given node u.
def K_Hop_neighbors(G1,node,K):

   neig = list(nx.neighbors(G1, node))
   #print(neig[0])
   i=1
   while i<K:
       if(len(neig)>1):
           neig = list(nx.neighbors(G1, neig[1]))
           print(neig[1])
           i += 1

       else:
           neig = list(nx.neighbors(G1, neig[0]))
           if(len(neig) == 0):
               print("OOPs no further neighbors found",'\n',i, "hops found only" )
               break
           else:
               print(neig[0])
               i+=1
   print(neig[0], "will be your kth-hop from inserted node")


#Find and display a path of length k, that has node u as one of the endpoints
def path_of_length_k(graph,s):
    pathbfs = list(nx.bfs_predecessors(graph, s,  depth_limit=None))
    #print(list(pathbfs))
    #print(len(pathbfs))
    G = nx.MultiDiGraph()
    for i in pathbfs:
        G.add_edge(i[0], i[1])
    nx.draw(G, with_labels=True ,node_color='r',
                       node_size=500,edge_color='b')
    plt.show()


#function for the subgraphs with K nodes
def Subgraph_Twitter(twitter_Real_Graph):
    SG = twitter_Real_Graph.subgraph(["12","13","14","15","16","17","18","19","20","21"])
    print("Subgraph with nodes")
    nx.draw(SG, with_labels=True ,node_color='r',
                       node_size=500,edge_color='b')
    plt.show()

def subgraph_RoadNet(roadNet_Graph):
    ## First part would be to fin the path and then use the subgraph to diplay
    SG = roadNet_Graph.subgraph(["2", "1", "6299", "6343", "4", "3","8", "812144", "811934", "812145", "813992", "811899"])
    print("Subgraph Road Net with nodes")
    nx.draw(SG, with_labels=True ,node_color='r',
                       node_size=500,edge_color='b')
    plt.show()


# Display a subgraph containing an independent set of size k that includes node u. Display the nodes in the independent set with a different color.
def subgraph_with_independentset(graph, node , k):
    # First part of the problem is to find sub graph with node u
    pathbfs = list(nx.bfs_predecessors(graph, node, depth_limit=None))
    # Second part of the problem is to find independent sets among the subgraph and mark them with a different color.
    print(pathbfs)





    G = nx.Graph()
    for i in pathbfs:
        G.add_edge(i[0], i[1])
        lastnode = i[0]

    print(lastnode)
    x = 25
    while(len(G) < k):
        x+=1
        y = x+2
        neig = list(nx.neighbors(graph, str(x)))
        neig1 = list(nx.neighbors(graph, str(y)))
        print(neig, neig1)
        G.add_edge(neig[0], neig1[0])



    #print(list(G))
    #print(G1[0])
    IS = nx.maximal_independent_set(G)
    color_map = np.empty(len(G), dtype=str)
    for i in range(len(color_map)):
        color_map[i] = 'blue'

    for count, node in enumerate(G):
        for i in IS:
            if node == i:
                color_map[count] = 'green'

    nx.draw(G, with_labels=True, node_color=color_map, node_size=500, edge_color='b')
    plt.show()


#subgraph_with_independentset(G1_RoadNet, "100")
subgraph_with_independentset(G2_Twitter, "1110", 15)



#K_Hop_neighbors(G1_RoadNet, "100", 5)
#K_Hop_neighbors(G2_Twitter, "15", 4)

#path_of_length_k(G1_RoadNet, "100")
#path_of_length_k(G2_Twitter, "15")

#print(nx.k_nearest_neighbors(G1_RoadNet, source='in+out', target='in+out', nodes=["100","101"], weight=None))
#Compute the average degree connectivity of graph.The average degree connectivity is the average nearest neighbor degree of nodes with degree k.

