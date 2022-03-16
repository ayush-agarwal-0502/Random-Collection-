# Code by Ayush Agarwal 
# Electronics engineering , IIT BHU Varanasi , 2nd year 

# This is a code for dijkstra algorithm given the adjacency matrix of the graph 
# this code uses oops , and unlike other codes availaible online , this code uses arrays 
# since I found it more intutive to implement 
# This code has been written from scratch by me :) enjoy 

# I have made a class called graph and made its method as dijkstra algorithm  

# importing the required libraries 
import math 

# initiating the class
class graph():

    # defining the constructor 
    def __init__(self,adj_matrix):
        # making the given adjacency matrix as an attribute of the object ,
        # so that I can easily use it 
        self.adj_matrix = adj_matrix
        # neighbours1 array is an array of the nodes which are already discovered 
        # and can be the possible ways of extending the search 
        self.neighbours1 = [] 
        # storing the parent node info for each node in an array 
        self.parent = [-1 for x in range(len(adj_matrix[0]))]
        # storing the path in another array 
        self.path = []
        # visited = 1 means that we have already looked at its neighbours 
        self.visited = [0 for x in range(len(adj_matrix[0]))]
        # discovered = 1 means that it was a neighbour to a visited node 
        self.discovered = [0 for x in range(len(adj_matrix[0]))]
        # cost is the dist from start considering the weights 
        self.cost = [999 for x in range(len(adj_matrix[0]))]

    # the method for dijkstra , start and end are the names of the start and end nodes 
    def dijkstra(self,start,end):
        # alpha is a variable showing which node is being run ,
        # i.e. the node whose neighbours we are adding 
        # obviously gotta start from the start node and mark it visited 
        alpha = start
        self.visited[alpha] = 1
        # the infinite loop which breaks only when it returns the path 
        while(True):
            # helps see the way in which the nodes were traversed
            print(alpha)
            # print(self.adj_matrix[alpha])
            # making the active node alpha as visited 
            self.visited[alpha] = 1
            # acting on all the neighbours of alpha 
            for i in range(0,len(self.adj_matrix[alpha])):
                # if undiscovered neighbour add it to neighbours array and set its parents and cost 
                if(self.discovered[i]==0 and self.adj_matrix[alpha][i]!=0 and self.visited[i]==0):
                    self.parent[i]=alpha
                    self.discovered[i] = 1
                    self.cost[i] = self.cost[alpha] + self.adj_matrix[alpha][i]
                    self.neighbours1.append(i)
                # if already discovered neighbour , update only if lower cost found 
                if(self.discovered[i]==1 and self.adj_matrix[alpha][i]!=0 and self.visited[i]==0):
                    if(self.cost[i] > self.cost[alpha] + self.adj_matrix[alpha][i]):
                        self.cost[i] = self.cost[alpha] + self.adj_matrix[alpha][i]
                        self.parent[i]=alpha
            # the terminating condition is when alpha becomes end 
            # (and not when the end becomes discovered which I used to think before manually 
            # implementing this algorithm )
            if(alpha == end):
                # now using this beta variable , find all the chain of parents and store them in path
                beta = end
                # print(beta)
                self.path.append(beta)
                while(beta!=start):
                    beta = self.parent[beta]
                    # print(beta)
                    self.path.append(beta)
                # need to reverse due to the way we added it 
                # end was in the front of the array and start at the last of path array 
                self.path.reverse()
                print(self.path)
                return self.path
            # if we havent reached the end yet , gotta continue 
            else:
                # we need to find the lowest cost discovered not visited node and 
                # assign alpha to it 
                bazinga = [99 for x in range(len(self.neighbours1))]
                # bazinga is an array of the costs of the nodes in neighbours , to get the least cost neighbour 
                for z in range(0,len(self.neighbours1)):
                    bazinga[z] = self.cost[self.neighbours1[z]]
                # temp is the minimum cost possible for the nodes in the neighbour array 
                temp = min(bazinga)
                # res is an array which holds the minimum cost options in the neighbours array 
                res = []
                for idx in range(0, len(bazinga)):
                    if temp == bazinga[idx]:
                        res.append(self.neighbours1[idx])
                # print(res)
            # is res is empty , it means all nodes have been visited 
            # this might be a case when there is no entry to a certain node 
            if(res):
                # selecting one of the possible options among all least cost neighbour nodes
                alpha = res[0]
                # print("value of alpha now is " + str(alpha))
            else:
                #the worst case when no path exists , and the neighbours array becomes empty 
                print("no path possible ")
                break
            # very very essential step , otherwise throws infinite loop 
            self.neighbours1.remove(alpha)
            # print("value of alpha now is " + str(alpha))
                


# Now testing my graph class 
# The diagram for this specific adjacency matrix can be referred from 
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
# the diagram shows that the answer given by my code is correct 

adj_matrix_1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]  ]

# making the graph 
graph1 = graph(adj_matrix_1)
# getting the path using dijkstra 
path1 = graph1.dijkstra(0,8)
print("Final output path : ")
print(path1)
    