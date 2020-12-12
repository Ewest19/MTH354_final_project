class MinimalSpanningTree:
    def __init__(self, edge_list, vertex_count, initial_vertex):
        self._edge_list = edge_list                 # Creating a variable for the initial set of edges
        self._vertex_count = vertex_count           # Creating a variable for the amount of vertices
        self._initial_vertex = initial_vertex       # Creating a variable for the starting vertex
        self._MST_edge_list = list()                # Creating a list to put the edges of the minimum spanning tree
        self._list_of_vertices_in_MST = list(initial_vertex)    # Creating a variable for the vertices that are in the MST

    def get_list_of_vertices_in_MST(self):
        """
        Function to update the variable self._list_of_vertices_in_MST
        This function iterates through the edges in the edge list and check to see if Vertex1 and Vertex2
        are in the list of vertices, if not they get added.
        :return: None
        """
        """
        for edge_set in self._edge_list:
            if edge_set[0] not in self._list_of_vertices_in_MST:
                self._list_of_vertices_in_MST.append(edge_set[0])
            if edge_set[1] not in self._list_of_vertices_in_MST:
                self._list_of_vertices_in_MST.append(edge_set[1])
        """
        for edge in self._MST_edge_list:
            if edge[0] not in self._list_of_vertices_in_MST:
                self._list_of_vertices_in_MST.append(edge[0])
            if edge[1] not in self._list_of_vertices_in_MST:
                self._list_of_vertices_in_MST.append(edge[1])

    def next_edges(self):
        """
        Function that returns a list of the next possible edges.
        :return: next_edges_list
        """
        # Iterates through every vertex that is already in the MST, then finds all the edges that connect to those
        # vertices and adds them to the list of next options for edges.
        next_edges_list = list()
        self.get_list_of_vertices_in_MST()
        for vertex in self._list_of_vertices_in_MST:
            for edge in self._edge_list:
                if vertex in edge:
                    next_edges_list.append(edge)

        # Iterate through the list of next options and make sure that that edge won't be connecting two edges
        # that are already in the MST, even if it weighs the least
        self.get_list_of_vertices_in_MST()
        for edge in next_edges_list:
            if edge[0] in self._list_of_vertices_in_MST and edge[1] in self._list_of_vertices_in_MST:
                next_edges_list.remove(edge)

        return next_edges_list

    def run_algorithm(self):
        while self._vertex_count > 1:
            smallest_weight = 1000000
            next_edges_list = self.next_edges()
            next_edge = list()

            for edge in next_edges_list:
                if edge[2] < smallest_weight:
                    smallest_weight = edge[2]
                    next_edge = edge

            self._MST_edge_list.append(next_edge)
            self._edge_list.remove(next_edge)
            self._vertex_count -= 1

    def __str__(self):
        return str(self._MST_edge_list)


def main():
    print("Input the edge list of form: [['A','B',1],['B','C',2]]")
    edge_list = input('->')
    vertex_count = int(input('Number of vertices: '))
    initial_vertex = input('Choose the starting vertex: ')

    """
    edge_list = [['A', 'B', 5], ['A', 'C', 2], ['B', 'C', 1], ['C', 'E', 4], ['B', 'D', 6], ['D', 'E', 3],
                 ['E', 'F', 2], ['D', 'F', 1]]
    vertex_count = 6
    initial_vertex = 'A'
    """

    """
    edge_list = [['A', 'B', 6], ['A', 'F', 3], ['B', 'F', 5], ['B', 'G', 3], ['G', 'F', 6], ['F', 'E', 4],
                 ['G', 'E', 6], ['E', 'C', 3], ['B', 'C', 7], ['G', 'C', 5], ['C', 'D', 2], ['E', 'D', 3]]
    initial_vertex = 'A'
    vertex_count = 7
    """

    prims_algorithm = MinimalSpanningTree(edge_list, vertex_count, initial_vertex)

    prims_algorithm.run_algorithm()

    print(prims_algorithm)


if __name__ == '__main__':
    main()
