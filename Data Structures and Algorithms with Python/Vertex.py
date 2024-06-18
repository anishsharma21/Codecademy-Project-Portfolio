class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex):
    self.edges[vertex] = True

  def get_edges(self):
    return list(self.edges.keys())

class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

my_list = [1, 2, 4, 6, 22, 4]
filtered_list = list(filter(lambda x: x <= 4, my_list))
print(filtered_list)