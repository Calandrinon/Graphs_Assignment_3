from graph import DoubleDictGraph


class Tests:

    def __init__(self):
        self.test_get_vertices()
        self.test_is_edge()
        self.test_add_edge()
        self.test_get_outbound_neighbours()
        self.test_get_inbound_neighbours()
        self.test_get_number_of_vertices()
        self.test_get_in_and_out_degree()
        self.test_parse_outbound_edges()
        self.test_parse_inbound_edges()
        self.test_retrieve_edge_cost()
        self.test_modify_edge_cost()
        self.test_remove_edge()
        self.test_add_vertex()
        self.test_remove_vertex()
        self.test_copy_graph()
        self.test_read_graph_from_file()
        self.test_write_graph_to_file()
        self.test_create_random_graph()


    def test_get_vertices(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)

        dict = {}
        for i in range(30):
            dict[i] = []
        dict[0] = [0, 1]
        dict[1] = [2, 3]
        dict[2] = [1, 3]

        assert(dict.keys() == graph.get_vertices())
        print("Vertex set getter test passed!")


    def test_is_edge(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(1, 2, 7)
        assert(graph.is_edge(1, 2) == True)
        assert(graph.is_edge(2, 3) == False)
        print("Edge existence check test passed!")


    def test_add_edge(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(4, 3, 15)
        assert(graph.is_edge(4, 3) == True)
        print("Edge addition test passed!")


    def test_get_outbound_neighbours(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 2, 5)
        assert(graph.get_outbound_neighbours_of_vertex_X(0) == [2])
        print("Outbound neighbours of a node test passed!")


    def test_get_inbound_neighbours(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 2, 5)
        assert(graph.get_inbound_neighbours_of_vertex_X(2) == [0])
        print("Inbound neighbours of a node test passed!")


    def test_get_number_of_vertices(self):
        graph = DoubleDictGraph(30)
        graph.remove_vertex(5)
        graph.remove_vertex(2)
        graph.remove_vertex(3)
        assert(graph.get_number_of_vertices() == 27)
        print("Number of vertices getter test passed!")


    def test_get_in_and_out_degree(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)
        assert(graph.get_in_and_out_degree(1) == (2, 2))
        print("In and out degree of a node test passed!")


    def test_parse_outbound_edges(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)
        assert(graph.parse_outbound_edges_of_vertex_x(0) == [0, 1])
        print("Outbound edges of a node parsing test passed!")


    def test_parse_inbound_edges(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)
        assert(graph.parse_inbound_edges_of_vertex_x(1) == [0, 2])
        print("Inbound edges of a node parsing test passed!")


    def test_retrieve_edge_cost(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)
        assert(graph.retrieve_edge_cost(1, 3) == 8)
        print("Edge cost retrieval test passed!")


    def test_modify_edge_cost(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)
        graph.modify_edge_cost(1, 3, 18)
        assert(graph.retrieve_edge_cost(1, 3) == 18)
        print("Edge cost modification test passed!")


    def test_remove_edge(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)
        assert(graph.is_edge(0, 1) == True)

        graph.remove_edge(0, 1)

        assert(graph.is_edge(0, 1) == False)
        print("Edge removal test passed!")


    def test_add_vertex(self):
        graph = DoubleDictGraph(1)
        graph.add_vertex(156)

        assert(graph.get_number_of_vertices() == 2)
        print("Vertex addition test passed!")


    def test_remove_vertex(self):
        graph = DoubleDictGraph(30)
        graph.add_edge(0, 0, 1)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, -1)
        graph.add_edge(1, 3, 8)
        graph.add_edge(2, 3, 5)

        graph.remove_vertex(1)

        assert(graph.is_edge(0, 1) == False)
        assert(graph.is_edge(2, 1) == False)
        assert(graph.is_edge(1, 2) == False)
        assert(graph.is_edge(1, 3) == False)

        print("Vertex removal test passed!")


    def test_copy_graph(self):
        graph = DoubleDictGraph(2)
        graph.add_edge(0, 1, 0)
        copy_of_the_graph = graph.copy()
        
        assert(copy_of_the_graph.get_number_of_vertices() == 2)
        dictout = copy_of_the_graph.get_dict_out()
        assert(len(dictout[0]) == 1)
        assert(len(dictout[1]) == 0)

        copy_of_the_graph.remove_vertex(1)
        assert(copy_of_the_graph.get_number_of_vertices() == 1) 
        assert(graph.get_number_of_vertices() == 2) 

        print("Graph copy test passed!")


    def test_read_graph_from_file(self):
        graph = DoubleDictGraph.read_graph_from_text_file("graph.txt")
        
        assert(graph.is_edge(0,0))
        assert(graph.is_edge(0,1))
        assert(graph.is_edge(1,2))
        assert(graph.is_edge(2,1))
        assert(graph.is_edge(1,3))
        assert(graph.is_edge(2,3))
        
        print("Graph reading from file test passed!")


    def test_write_graph_to_file(self):
        graph = DoubleDictGraph.read_graph_from_text_file("graph.txt")
        graph.write_graph_to_text_file("graph2.txt")
        
        f1 = open("graph.txt", "r")
        f2 = open("graph2.txt", "r")
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()
        file1_lines.sort()
        file2_lines.sort()

        assert(file1_lines == file2_lines)

        print("Graph writing to file test passed!")


    def test_create_random_graph(self):
        random_graph = DoubleDictGraph.create_random_graph(10, 25)
        
        """
        for node in random_graph.get_vertices():
            print(node, end=": ")

            for neighbour in random_graph.get_outbound_neighbours_of_vertex_X(node):
               print(neighbour, end="  ") 

            print("\n")
        
        print("Random graph generation test passed!")

        """
