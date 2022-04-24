
import random

from random_solution_gen import random_dummy_route
from PDP_utils import cost_function as cost
from operators import insert_two_exchange, try_for_best, remove_from_dummy
from basic_operators import reinsert, two_exchange, three_exchange


def adaptive_large_neighborhood_search(problem): 
    #generate initial solution
    initial = random_dummy_route(problem)
    initial_cost = cost(sol, problem)

    best = sol
    best_cost = initial_cost


    #variables to keep track of iterations
    weights_update_rate = 100
    curr_weights = []
    used = []
    total_used = []
    
    avail_operators = operators()
    for i in range(len(avail_operators)): 
        curr_weights.append(1.0 / len(avail_operators))
        used.append(0)
        total_used.append(0)

    prev_w = curr_weights.copy()
    i_since_new_sol, div_its = 0,0

    for it in range(10000): 

        sol = initial 
        cost = initial_cost
       
        if it % weights_update_rate == 0 and it > 0: 
            prev_w = curr_weights
            curr_weights = normalize_weights(prev_w, curr_weights, used)
            used = [0 for elem in used]


        op = random.choices(avail_operators, weigths = prev_w, k = 1) #choose only one operator with the given weights
        if op == insert_two_exchange.__name__: 
            sol = insert_two_exchange(sol, problem)
        elif op == try_for_best.__name__: 
            sol = try_for_best(sol, problem)
        elif op == remove_from_dummy.__name__: 
            sol = remove_from_dummy(sol, problem)
        elif op == reinsert.__name__: 
            sol = reinsert(sol, problem)
        elif op == two_exchange.__name__: 
            sol = two_exchange(sol, problem)
        elif op == three_exchange.__name__: 
            sol = three_exchange(sol, problem)


        new_cost = cost(sol, problem)



def operators():
    return [insert_two_exchange.__name__, try_for_best.__name__, remove_from_dummy.__name__ \
        , reinsert.__name__, two_exchange.__name__, three_exchange.__name__] 

def set_parameters(): 
    refresh_weigths = 100 
    div_rate = 200 
    return [refresh_weigths, div_rate]

solutions = set()

def update_weight(current, weights, index, cost_curr, cost_s, cost_best ): 
    if cost_curr < cost_s: 
        weights[index] += 2 
    global solutions
    id_curr = id(current)
    if id_curr not in solutions:
        weights[index] += 1 
        solutions.add(id_curr) 
    if cost_curr < cost_best: 
        weights += 4
    return weights

def normalize_weights(prev, current, usage): 
    r = 0.6

    new_current = prev 
    for i in range(len(new_current)): 
        new_current[i] = prev[i]*(1-r) + r*(current[i]/max(usage[i], 1))
    return new_current

