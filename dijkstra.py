class DijkstraClass:
  """...write comment for this class..."""
  '''
  The main goal of this class is to find the lowest-cost path
  from start (s) to finish (f) using Dijkstra's shortest path algorithm

  graph_one = {
    's': {'a': 6, 'b': 2},
    'a': {'c': 1},
    'b': {'a': 3, 'c': 5},
    'c': {'f': 2},
    'f': {},
}

  graph_two = {
    's': {},
    'a': {'c': 1},
    'b': {'a': 3, 'c': 5},
    'c': {'f': 2},
    'f': {},
}

  '''

  def __init__(self, graph):
    """...write comment about this method...
    Initialize the  class with a graph map

    Parameters
    ----------
    grid : hash graph map
        (dict[str, Dict[str, float]])
        Dictionary of dictionaries. Each key is a 'node' and its value i another dictionary of 
        neighbors with edge weights

    Notes
    ----------
    Use 's' as the start and 'f' as the finsih
    """
    #graph to be compute shortest path
    self.graph = graph

    #start/finish labels used for this assignment 
    self.start = "s"
    self.finish = "f"

    #define infinity to be used through out class
    self.infinity = float("inf")
    
    # define known/computed costs to node
    self.costs = {}

    # define parts of each node in the beginning or at each moment
    self.parents = {}

    # used if this node have been processed
    self.processed = []



  def initial_costs_parents(self):
      """...write comment about this method...
      Initialize the costs and parents tables

      Notes
      ----------
      -> set everyone to INF cost and no parent 
      cost(start) = 0 
      cost(start's neighbors) = edge weights
      everything else = infinity 
      
      """
      #TODO: function logic

      #start at INF
      for node in self.graph.keys():
         self.costs[node] = self.infinity
         self.parents[node] = None

      #starting node has cost 0
      self.costs["s"] = 0 

      #neighbors of the start need to be assigned their edge weights and parent = start node
      for neighbor in self.graph["s"]:
         self.costs[neighbor] = self.graph["s"][neighbor]
         self.parents[neighbor] = "s"

      #nothing will be processed as of yet
      self.processed = []



  def find_shorted_path(self):
      """...write comment about this method...
      Here we need to run Dijkstra's algo to update the costs and parents
      """
      #TODO: function logic
      node = self.find_lowest_cost_node(self.costs)

      while node is not None:
         cost = self.costs[node]
         #check each neighbor of node
         for neighbor in self.graph[node]:
            new_cost = cost + self.graph[node][neighbor]
            #if a cheaper path is found, we need to then update the cost and parent
            if new_cost < self.costs[neighbor]:
               self.costs[neighbor] = new_cost
               self.parents[neighbor] = node
            
         #now we can mark node as 'processed' 
         self.processed.append(node)
         node = self.find_lowest_cost_node(self.costs)


  def find_lowest_cost_node(self, costs):
      """...write comment about this method...
      here we want to return the lowest-cost (unprocessed) node, or 'None' if none are left
      """
      #TODO: function logic
      lowest_cost = self.infinity
      lowest_cost_node = None

      for node in costs:
         if costs[node] < lowest_cost and node not in self.processed:
            lowest_cost = costs[node]
            lowest_cost_node = node

      return lowest_cost_node

  def print_path(self):
      """...write comment about this method...
      Print the path from 's' to 'f' or 'No path to finish' if unreachable
      """
      #TODO: function logic
      path=[]
      #starting from the finish node
      node = "f"

      #if finish is not reachable, then we want to match instructions and print the below string
      if self.costs.get("f", self.infinity) == self.infinity:
         print("No path to finish")
         return

      #if we made it to the finish node, we need to walk backwards from the finish 'f' to start 's' using parents to print the full path
      while node is not None:
         path.append(node)
         node = self.parents[node]

      path.reverse()
      print(path)
