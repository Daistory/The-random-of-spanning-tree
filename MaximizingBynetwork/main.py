# !usr/bin/python
# -*- coding:utf-8 -*-

import method
import invking

# file_name = "17-URVemail-edges.net"
# file_name = "69-USAirport2010-directed.edges"
# file_name = "35-caHepPh-maxcomponent.edges"
# file_name = "54-p2pGnutella31-directed.edges"
# file_name = "34-caGrQc-maxcomponent.edges"
file_name = "facebook_combined.txt"
# file_name = "Brightkite_edges.txt"
# file_name = "Email-Enron.txt"
# file_name = "hehe.txt"
# file_name = "Gowalla_edges.txt"
# file_name = "com-dblp.ungraph.txt"
# file_name1 = "similarAntPoint.txt"
path = "data/facebook"
graph, total = method.getGraph(method.getPath(file_name))
amt_vaccination = graph.number_of_nodes() / 10
invking.getResultByAllWay(graph, amt_vaccination, path, total)
