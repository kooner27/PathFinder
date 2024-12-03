from search.algorithms import State
from search.map import Map
import heapq
import numpy

'''
cost function is min(f, 2*g)
stop condition is u <= min(pf,)

'''



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


def mm(start, goal, gridded_map):

    
    # open list is a heap, closed list is a hashtable / set of states
    open_f = [] # open list
    open_b = [] # open backwards list    
    heapq.heappush(open_f, start) # insert start, g = 0
    heapq.heappush(open_b, goal) # insert goal, g  = 0
    closed_f = {} # closed forwards
    closed_b = {} # closed backwards
    closed_f[start.state_hash()] = start # insert Start
    closed_b[goal.state_hash()] = goal # insert goal
    
    # source: https://www.geeksforgeeks.org/python-infinity/
    # used the above source for representing 
    u = numpy.inf
    
    while (len(open_f) > 0) and (len(open_b) > 0): 
        
        c1 = (u<= open_f[0].get_cost())
        c2 = (u<= open_b[0].get_cost())
    
        stop = min(open_f[0].get_cost(), open_b[0].get_cost())
        c = (u<= stop)
        if (c): # if best solution so far is optimal
            print(f"mm: cost: {u}")
            print(f"mm: nodes: {len(closed_f) + len(closed_b)}")
            return u, len(closed_f) + len(closed_b)
        
    
        if (open_f[0].get_cost() < open_b[0].get_cost()): # if forward is smaller then expand forward
            n = heapq.heappop(open_f) # pop cheapest from forward
            children = gridded_map.successors(n)
            for child in children:
                key = child.state_hash()
                
                ## cost function
                x = abs(n.get_x() - child.get_x())
                y = abs(n.get_y() - child.get_y())
                action_cost = gridded_map.cost(x, y)
                parent_cost = n.get_g()
                new_g = parent_cost + action_cost
                child.set_g(new_g)
                
                h_value = h(child, goal)
                f = h_value + new_g    
                child.set_cost(min(f, 2*new_g)) 
                
                # unlike dijkstra we need to check if nodes are also in other search
                if key in closed_b:
                    u = min(u, child.get_g() + closed_b[key].get_g()) # update u if we found better value
                
                #### below is same as dijkstra. We expand the forward list.
                if key not in closed_f:
                    heapq.heappush(open_f, child) # open.insert
                    closed_f[key] = child
                    
                if (key in closed_f) and (child.get_g() < closed_f[key].get_g()):
                    closed_f[key].set_g(child.get_g())
                    closed_f[key].set_cost(child.get_cost())
                    heapq.heapify(open_f)

        
            
        else:
            n = heapq.heappop(open_b) 
            children = gridded_map.successors(n)
            for child in children:
                key = child.state_hash()
                x = abs(n.get_x() - child.get_x())
                y = abs(n.get_y() - child.get_y())
                action_cost = gridded_map.cost(x, y)
                parent_cost = n.get_g()
                new_g = parent_cost + action_cost
                child.set_g(new_g)
        
                h_value = h(child, start)
                f = h_value + new_g    
                child.set_cost(min(f, 2*new_g)) 
                
                if key in closed_f:
                    u = min(u, child.get_g() + closed_f[key].get_g()) 
                
                #### below is same as dijkstra.
                if key not in closed_b:
                    heapq.heappush(open_b, child) # open.insert
                    closed_b[key] = child

                if (key in closed_b) and (child.get_g() < closed_b[key].get_g()):
                    closed_b[key].set_g(child.get_g())
                    closed_b[key].set_cost(child.get_cost())
                    heapq.heapify(open_b)
    
    # if we finish the loop then no solution
    print("mm no solution")
    return -1, len(closed_b) + len(closed_f)
    
    
    
