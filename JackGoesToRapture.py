# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import Queue

class Graph:
  def __init__(self):
    self.nodes = Queue.PriorityQueue()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.put(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  rev = Queue.PriorityQueue()
  rev.put((0, initial))

  path = {}

  nodes = graph.nodes

  while not rev.empty(): 
    a = rev.get()

    min_node = a[1]

    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + max(0, graph.distances[(min_node, edge)] - current_weight)
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        rev.put((weight, edge))
        path[edge] = min_node

  return visited, path
        

N, E = map(int, raw_input().split())
g = Graph()
for i in range(0, E):
    a, b, c = map(int, raw_input().split())
    g.add_node(a)
    g.add_node(b)
    g.add_edge(a, b, c)
   
result = dijsktra(g, 1)[0]
if result.has_key(N):
    print result[N]
else:
    print "NO PATH EXISTS"

    