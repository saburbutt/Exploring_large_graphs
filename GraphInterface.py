from tkinter import *
import GraphOperations as GO
import ReadGraphs as G

#Initializing the graphs
G1_RoadNet = G.RoadNet_Graph
G2_Twitter = G.Twitter_Real_Graph

#initialize
root = Tk()
root.title("Graph Operation Interface")
root.resizable(False, False)
root.wm_minsize(width=900,height=500)


# Function of the buttons

def onclick(args):
    if args == 1:
        GO.Print_Graph_Info(G1_RoadNet, G2_Twitter)
    if args == 2:
        GO.K_Hop_neighbors(G1_RoadNet, "", 5)



"""################################LAYOUT CONTROLS############################################"""
"""First section for display of Graphs"""
#all the widgets
w = LabelFrame(root, text= "Display of Graphs")
w.pack(fill="both", expand="yes")
e = Entry(w, width = 50, borderwidth = 5)
label_for_subgraph = Label(w, text= "Enter the number of nodes you want to display for Graphs")
Twitter_graph_button = Button(w, text = "Showing subgraph of Twitter")
RoadNet_graph_button = Button(w, text = "Showing subgraph of RoadNet")
Show_Graph_info = Button(w, text= "Show Info of both Graphs", command =lambda:onclick(1) )

#Positioning of widgets in the Grid
e.grid(row= 1, column= 1, padx = 1, pady = 1)
Twitter_graph_button.grid(row= 1, column= 2, padx = 1, pady = 1)
RoadNet_graph_button.grid(row= 1, column= 3, padx = 1, pady = 1)
label_for_subgraph.grid(row= 2, column= 1, padx = 1, pady = 1)
Show_Graph_info.grid(row = 1, column = 4, padx = 1, pady = 1)

"""############################################################################"""




"""############################################################################"""
"""Second section for K hop neigborhood of node given a vertex"""
w1 = LabelFrame(root, text= "K Hop neigborhood")
w1.pack(fill="both", expand="yes")
submit_Khop_twitter = Button(w1, text = "K-Hop of twitter")
submit_Khop_realg = Button(w1, text = "K-Hop of realgraph")
e_k = Entry(w1, width = 20, borderwidth = 5)
e_startingnode = Entry(w1, width = 20, borderwidth = 5)
label_for_Khops = Label(w1, text= "Enter the K number of hops")
label_for_startingnode = Label(w1, text= "Enter the starting node U for k-hops")

#Positioning of widgets in the Grid
e_k.grid(row= 4, column= 0, padx = 15, pady = 2)
label_for_Khops.grid(row= 5, column= 0, padx = 15, pady = 2)
e_startingnode.grid(row= 4, column= 1, padx = 2, pady = 2)
label_for_startingnode.grid(row= 5, column= 1, padx = 15, pady = 2)
submit_Khop_twitter.grid(row= 4, column= 2, padx = 2, pady = 2)
submit_Khop_realg.grid(row= 4, column= 3, padx = 2, pady = 2)

"""############################################################################"""


root.mainloop()