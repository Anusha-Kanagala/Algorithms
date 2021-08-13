#!/usr/bin/python3

# Class:     CSCI 656
# Program:   Assignment 2
# Author:    Anusha Kanagala
# Z-number:  z1901136
# Date Due:  02/26/221

# Purpose:   Below program finds the shortest path between two cities
#            using BFS,DFS with DFID and Astar with heuristic values

# Execution: python3 hw02.py 'Rennes' 'Lyon' 3


import sys
from Node import Node
from Data import Data

# object creation for Data class

data = Data()

# Print the values of open list and closed list for BFS algorithm

# Arguments: string to print and list

# Returns:   Prints the values of open and closed lists


def print_list_values(str_name, values):
    val = ""
    # loop to print each value of list
    for iter_item in values:
        val =  val + iter_item.name + ' '
    val = val[:-1]
    print(f'{str_name} ({val})')

# Print the children nodes for BFS algorithm

# Arguments: string to display and dictionary of children

# Returns:   Prints the children nodes


def print_children(str_name, values):
    val = ""
    # loop to print each children
    for key in values.keys():
        val = val + key + ' '
    val = val[:-1]
    print(f'{str_name} ({val})')

# Print the shortest path using BFS, DFS, Astar algorithms

# Arguments: string to display and node values

# Returns:   Prints the final path


def print_final_path(str_name, values):
    val = ""
    # loop to print the shortest path
    for item in values:
        val = val + item + ' '
    val = val[:-1]
    print(f'{str_name} ({val})')

# Print the open list and closed list with depth at each level for DFS algorithm

# Arguments: string to display and node values

# Returns:   Prints the open list and closed list


def print_list_values_DFID(stri, values):
    val = ""
    # loop to print open list and closed list
    for iter_item in values:
        val = val + '(' + iter_item.name + ' ' + str(iter_item.h) + ')' + ' '
    val = val[:-1]
    print(f'{stri} ({val})')

# Print children at each level of depth for DFS algorithm

# Arguments: string to display, node values and depth value

# Returns:   Prints the children at each level with depth


def print_children_DFID(stri, values, d):
    val = ""
    # loop to print children at each level
    for key in values.keys():
        val = val + '(' + key + ' ' + str(d) + ')' + ' '
    val = val[:-1]
    print(f'{stri} ({val})')

# Print open list and closed list for Astar algorithm

# Arguments: string to display, node values

# Returns:   Prints the open list and closed list with cost


def print_list_values_astar(stri, values):
    val = ""
    # loop to print open list and closed list for Astar algorithm
    for iter_item in values:
        val = val + '(' + iter_item.name + ' ' + str(iter_item.g) + ')' + ' '
    val = val[:-1]
    print(f'{stri} ({val})')


# Print open list and closed list for Astar algorithm

# Arguments: string to display, node values

# Returns:   Prints the open list and closed list with cost


def print_children_astar(stri, values):
    val = ""
    # loop to print children at each level of Astar
    for key in values.keys():
        val = val + key + ' '
    val=val[:-1]
    print(f'{stri} ({val})')


# Print open list and closed list for Astar algorithm with h value

# Arguments: string to display, openlist/ closed list

# Returns:   Prints the open list and closed list with cost


def print_list_values_astarh(stri, values):
    val = ""
    # loop to print open list and closed list of Astar with h value
    for iter_item in values:
        val = val + '(' + iter_item.name + ' ' + str(iter_item.f) + ')' + ' '
    val = val[:-1]
    print(f'{stri} ({val})')


# Print children at each node for Astar algorithm with h value

# Arguments: string to display, open list/closed list

# Returns:   Prints children nodes at each level


def print_children_astarh(stri, values):
    val = ""
    # loop to print children at each level for Astar algorithm
    for key in values.keys():
        val = val + key + ' '
    val=val[:-1]
    print(f'{stri} ({val})')


# Find the shortest path for cities using Breadth first search algorithm

# Arguments: from city and destination city

# Returns:  shortest path


def bfs_shortest_path(start_node, goal_node):
    print('BFS:\n')
    snode = Node(start_node, None)
    gnode = Node(goal_node, None)
    closedlist = []
    openlist =[]
    openlist.append(snode)

    # Loop to iterate openlist to expand nodes
    while len(openlist) > 0:
        newlist = []
        cnode = openlist.pop(0)

        print(f'\nExpanding {cnode.name}')
        if cnode.name == gnode.name:
            shortpath = []
            while cnode.name != snode.name:
                shortpath.append(cnode.name)
                cnode = cnode.parent
            shortpath.append(snode.name)
            return shortpath[::-1],len(closedlist)

        # get the children nodes of current node
        neighbours = data.get_roadmap_france().get(cnode.name)
        print_children('Children are', neighbours)
        # loop to iterate over each children node
        for key in neighbours.keys():
            neighbour = Node(key, cnode)

            if neighbour in closedlist or neighbour in openlist:
                continue
            openlist.append(neighbour)
            newlist.append(neighbour)
        closedlist.append(cnode)
        print_list_values('New children are', newlist)
        print_list_values('Open list is', openlist)
        print_list_values('Closed list is', closedlist)
    return None


# Find the shortest path for cities using Astar search algorithm

# Arguments: from city, destination city and heuristic value as 0

# Returns:  shortest path


def astar_algorithm(start_node, goal_node):
    print('\nA* with h=0:\n')
    snode = Node(start_node, None)
    gnode = Node(goal_node, None)
    closedlist = []
    openlist = []
    snode.g = 0
    snode.h = 0
    snode.f = snode.g + snode.h
    openlist.append(snode)
    while len(openlist) > 0:
        cnode = openlist.pop(0)
        print(f'\nExpanding {cnode.name} f={cnode.f}, g={cnode.g}, h={cnode.h}')

        # Get the children nodes dictionary of current node
        cnodedict = data.get_roadmap_france().get(cnode.name)

        if cnode.name == gnode.name:
            final_value = cnode.g
            shortpath = []
            while cnode.name != snode.name:
                shortpath.append(cnode.name)
                cnode = cnode.parent
            shortpath.append(snode.name)
            return shortpath[::-1], final_value, len(closedlist)
        print_children_astar('Children are', cnodedict)

        # Loop to iterate dictionary to get each children node
        for k, v in cnodedict.items():
            node = Node(k, cnode.name)
            node.g = v
            if node not in closedlist:
                if node not in openlist:
                    newNode = Node(k, cnode)

                    # calculates and assigns current g value
                    newNode.g = newNode.f = int(v) + cnode.g
                    openlist.append((newNode))
                else:
                    for onode in openlist:
                        if onode == node and onode.g > (int(node.g)) + int(cnode.g):
                            # revalue g value of current node to least cost
                            revalue = int(node.g) + int(cnode.g)
                            print(f'***Revaluing open node {node.name} from {onode.g} to {revalue}')
                            onode.parent = node
                            onode.g = onode.f = revalue
        closedlist.append(cnode)
        openlist.sort()

        print_list_values_astar('Open list is', openlist)
        print_list_values_astar('Closed list is', closedlist)

    return None


# Find the shortest path for cities using Astar search algorithm

# Arguments: from city, destination city and heuristic value taken from longitudes

# Returns:  shortest path


def astarh(start_node, goal_node):
    print("\n\nA* with h=east-west distance:\n")
    snode = Node(start_node, None)
    gnode = Node(goal_node, None)
    closedlist = []
    openlist = []
    snode.g = 0

    # Calculate h value of the start node
    snode.h = data.get_h_value(snode.name,gnode.name)

    # Calculate f value of the start node
    snode.f = snode.g + snode.h
    openlist.append(snode)
    while len(openlist) > 0:
        cnode = openlist.pop(0)
        print(f'\nExpanding {cnode.name} f={cnode.f}, g={cnode.g}, h={cnode.h}')

        # get children nodes dictionary of the current node
        cnodedict = data.get_roadmap_france().get(cnode.name)

        if cnode.name == gnode.name:
            final_value = cnode.f
            shortpath = []
            while cnode.name != snode.name:
                shortpath.append(cnode.name)
                cnode = cnode.parent
            shortpath.append(snode.name)
            return shortpath[::-1], final_value, len(closedlist)
        print_children_astarh('Children are', cnodedict)

        # Iterate through dictionary to calculate g and h values of each children
        for k, v in cnodedict.items():
            node = Node(k, cnode)
            node.g = int(cnodedict.get(node.name)) + int(cnode.g)
            node.h = data.get_h_value(node.name,gnode.name)
            if node not in closedlist:
                if node not in openlist:
                    newNode = Node(k, cnode)
                    newNode.g = int(node.g)
                    newNode.h = data.get_h_value(newNode.name,gnode.name)
                    newNode.f = newNode.g + newNode.h
                    openlist.append((newNode))
                else:
                    for onode in openlist:
                        if onode == node:
                            # condition to check current node g value to get least cost path
                            if onode.g > int(node.g):
                                old_f = onode.f
                                onode.g = node.g
                                onode.parent = node.parent
                                # Calculate f value of current node with least g value
                                onode.f = onode.g + onode.h
                                print(f'***Revaluing open node {node.name} from {old_f} to {onode.f}')
        closedlist.append(cnode)
        openlist.sort(key=lambda c: c.f)

        print_list_values_astarh('Open list is', openlist)
        print_list_values_astarh('Closed list is', closedlist)

    return None


# Find the shortest path for cities using Depth First Search algorithm with depth value

# Arguments: from city, destination city, depth

# Returns:  shortest path


def dfs_withDFID(start_node, goal_node, depth):
    print("\n\nDFID:\n")
    found_path = False
    is_dfid = True
    snode = start_node
    gnode = goal_node
    total_nodes_expanded = 0
    # loop to iterate through each depth level untill max reached
    for dlimit in range(0, (int(depth)+1)):
        print("\n\nDFID LEVEL ", dlimit, ":", sep='')
        found_path,nodes_expanded,cnode = dfs_inner(snode, gnode, dlimit, is_dfid)
        # Calculates total nodes expanded at all levels
        total_nodes_expanded = total_nodes_expanded + nodes_expanded
        if found_path:
            break
    val = ""
    # Loop to iterate and print the shortest path
    while cnode.name != snode:
        val = cnode.name + " " + val
        cnode = cnode.parent
    val = snode + " " + val
    val = val[:-1]
    print(f'\n\nDFID solution: ({val})' )
    if not found_path:
        print(total_nodes_expanded,"total nodes expanded\n")


# Find the shortest path for cities using Depth First Search algorithm

# Arguments: from city, destination city

# Returns:  shortest path


def dfs_withOutDFID(start_node, goal_node):
    print("\n\nDFS:\n")
    is_dfid = False
    snode = start_node
    gnode = goal_node
    found_path, nodes_expanded, cnode = dfs_inner(snode, gnode, 0, is_dfid)
    val = ""
    # Loop to iterate and print the shortest path
    while cnode.name != snode:
        val = cnode.name + " " + val
        cnode = cnode.parent
    val = snode +" " + val
    val = val[:-1]

    print(f'\n\nDepth-first search solution: ({val})')
    print(nodes_expanded,"nodes expanded\n")


# Find the shortest path for cities using Depth First Search algorithm with or without depth value

# Arguments: from city, destination city, depth, is_dfid

# Returns:  shortest path


def dfs_inner(start_node, goal_node, depth_limit,is_dfid):
    snode = Node(start_node, None)
    gnode = Node(goal_node, None)
    openlist = []
    closedlist = []
    snode.h = 0
    openlist.append(snode)

    # assign depth to max value if is_dfid is false
    if is_dfid:
        depth = depth_limit
    else:
        depth = 99999999

    # condition to check if there are any nodes to expand in open list
    while(len(openlist)>0):
        cnode = openlist.pop(0)
        print(f'\nExpanding {cnode.name[:]}')

        if cnode.name == gnode.name:
            return False, len(closedlist),cnode

        # Condition to check if depth is reached
        if cnode.h == depth:
            print("Depth has been reached")

        elif cnode.h < depth:
            # Get children nodes of current node
            neighbours = data.get_roadmap_france().get(cnode.name)
            if not is_dfid:
                print_children('Children are', neighbours)
            else:
                print_children_DFID('Children are', neighbours, cnode.h + 1)
            newchildren = []

            # Iterate through dictionary to get each children node and calculate h value
            for k in neighbours:
                node = Node(k, cnode)
                # increment depth at each level
                node.h = int(cnode.h) + 1
                if node not in closedlist:
                    if node not in openlist and node.h <= depth:
                        newchildren.append(node)
                        openlist.append(node)
            if not is_dfid:
                print_list_values('New children are', newchildren)
            else:
                print_list_values_DFID('New or revalued children are', newchildren)
        closedlist.append(cnode)
        openlist.sort(key=lambda c: c.h, reverse=True)
        if not is_dfid:
            print_list_values('Open list is', openlist)
            print_list_values('Closed list is', closedlist)
        else:
            print_list_values_DFID('Open list is', openlist)
            print_list_values_DFID('Closed list is', closedlist)

    return False,len(closedlist),cnode


final_path,expanded_nodes = bfs_shortest_path(sys.argv[1], sys.argv[2])
print ('\n')
print_final_path('Breadth-first search solution:',final_path)
print(f'{expanded_nodes} nodes expanded')

final_path = dfs_withOutDFID('Rennes', 'Lyon')

final_path, path_length, size = astar_algorithm(sys.argv[1], sys.argv[2])
print ('\n')
print_final_path('A* solution with h=0:', final_path)
print(f'Path length: {path_length}')
print(f'{size} nodes expanded')

final_path, path_length, size = astarh(sys.argv[1], sys.argv[2])
print('\n')
print_final_path('A* solution with h=east-west distance:', final_path)
print(f'Path length: {path_length}')
print(f'{size} nodes expanded')

final_path = dfs_withDFID('Rennes','Lyon',sys.argv[3])
