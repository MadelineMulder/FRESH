#!/usr/bin/env python
# coding: utf-8

# <h1> FLOOD ROUTING FOR EMERGENCY SERVICES FOR HURRICANES (FRESH)</h1> 
# 
# <h2> Introduction </h2>
# 
# The OSMnx python package is used for the routing where street networks from OpenStreetMap are utilized. The modes include: <b> walk </b>, <b> drive </b> and <b> bike </b>. In this section, we focus on calculating the shortest distance between points in Grand Bahama Island. We will focus on the period during Hurricane Dorian to understand the impact of the storm on travel distances. 

# <h2> Importing Libraries </h2>
# 
# The routing.yml file contains all the required libraries for this section. All the necessary libraries are imported before starting the project.  

# In[1]:


import osmnx as ox
import networkx as nx
import folium


# <h2> Street Network </h2>
# 
# The OSMnx retrieves the street network data for Grand Bahama Island. We specified two poins of interest using geographic coordinates.
# 
# <b> <i> Shortest route </i> </b> calculation in our case was found using tha 'Dijkstra algorithm'

# In[2]:


ox.settings.log_console=True
ox.settings.use_cache=True

start_latlng = (26.508882, -78.714336)
end_latlng = (26.533496, -78.680912)

start_latlng = (start_latlng [0],start_latlng[1])
end_latlng = (end_latlng [0],end_latlng[1])

start_marker = folium.Marker(location = start_latlng, popup = start_latlng, icon = folium.Icon(color='blue'))
end_marker = folium.Marker(location = end_latlng, popup = end_latlng, icon = folium.Icon(color='orange'))

place = 'Grand Bahama Island, The Bahamas'

mode = 'drive'

optimizer = 'time'

graph = ox.graph_from_place(place, network_type = mode)

orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)


# <h2> Visualization </h2>
# 
# Here, we used the <b> folium </b> library to visualize the calculated distance

# In[3]:


shortest_route_map = ox.plot_route_folium(graph, shortest_route, color = '#AA1111', tiles = 'openstreetmap')

start_marker.add_to(shortest_route_map)
end_marker.add_to(shortest_route_map)

folium.TileLayer ('openstreetmap').add_to(shortest_route_map)
folium.TileLayer ('Stamen Terrain').add_to(shortest_route_map)
folium.TileLayer ('cartodbdark_matter').add_to(shortest_route_map)

folium.LayerControl().add_to(shortest_route_map)

shortest_route_map

