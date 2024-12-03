from search.algorithms import State
from search.map import Map
import heapq

def h(state1, state2):
    x1 = state1.get_x()
    y1 = state1.get_y()
    x2 = state2.get_x()
    y2 = state2.get_y()

    xdif = abs(x1 - x2)
    ydif = abs(y1 - y2)
    
    m = min(xdif, ydif)
    cost = 1.5*m + abs(xdif-ydif)
    return cost
    
# start and goal are state objects
# they have x value, y value. g value is intially 0
# they can also be hashed

# gridded_map can return successors given a state, can return cost of action
# cost(self, x, y). basically if x value or y value is same cost is 1. Otherwise it is diagnaol so cost is 1.5
# i can probably use abs value of subtraction and then pass the x, y to cost function?

# open list is a heap, closed list is a hashtable / set of states
    
def dijkstra(start, goal, gridded_map):
    myheap = [] # open list
    start.set_g(0)
    hstart = h(start, goal)
    start.set_cost(hstart)
    heapq.heappush(myheap, start) # insert Sinit, g=0
    closed = {}
    closed[start.state_hash()] = start # insert Sinit
    
    
    while len(myheap) > 0: #stop when open is empty
        n = heapq.heappop(myheap)
        # print(f"popped:{n} cost: {n.get_g()}")
        if (n == goal):
            # need to return the cost and the # nodes
            print(f"a*: cost: {n.get_cost()}")
            print(f"a*: nodes: {len(closed)}")
            return n.get_cost(), len(closed)

        children = gridded_map.successors(n)
        for child in children:
            # cost function. f = g + h
            x = abs(n.get_x() - child.get_x())
            y = abs(n.get_y() - child.get_y())
            action_cost = gridded_map.cost(x, y)
            parent_cost = n.get_g()
            new_g = parent_cost + action_cost
            child.set_g(new_g)
            
            h_value = h(child, goal)
            f = h_value + new_g    
            child.set_cost(f)
            
            key = child.state_hash()
            
            if key not in closed: # new state add to open and closed        
                heapq.heappush(myheap, child)
                closed[key] = child
            
            if (key in closed) and (child.get_g() < closed[key].get_g()): # found better so update
                closed[key].set_g(child.get_g())
                closed[key].set_cost(child.get_cost())
                heapq.heapify(myheap)
        
    print("a* no solution")
    return -1, len(closed)