
import random
import math
from tqdm import tqdm

from random_solution_gen import random_dummy_route
from PDP_utils import cost_function, feasibility_check 
from operators import insert_two_exchange, try_for_best, remove_from_dummy
from basic_operators import reinsert, two_exchange, three_exchange
from display import print_sol
import matplotlib.pyplot as plt


def adaptive_large_neighborhood_search(problem): 
    #generate initial solution
    initial = random_dummy_route(problem)
    initial_cost = cost_function(initial, problem)
    
    best = initial
    best_cost = initial_cost

    #variables to keep track of iterations
    par = set_parameters()
    weights_update_rate, div_rate = par[0], par[1]
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

    a = 0.998 
    t = 70
    temps = [t]

    global solutions_found
    solutions_found = set()
    
    pbar = tqdm(total=25000, position=0, leave=True)

    sol = initial 
    sol_cost = initial_cost
    
    for it in range(25000): 
        pbar.update(1)
       
        #updates weights
        if it % weights_update_rate == 0 and it > 0: 
            prev_w = curr_weights
            curr_weights = normalize_weights(prev_w, curr_weights, used)
            used = [0 for elem in used]

        #TO DO! diversification operator
        if i_since_new_sol == div_rate: 
            for _ in range(10): 
                sol = reinsert(sol, problem)
            div_its += 1 

        #chooses operator   
        operation = choose_operator(avail_operators, prev_w, used, total_used \
            , sol, problem, sol_cost, best_cost)

        #updates variables
        new_sol, new_cost, curr_weights, used, total_used = operation[0], operation[1], operation[2], operation[3], operation[4]
        feas, c = feasibility_check(new_sol, problem)

        #acceptance criteria 
        delta = new_cost - sol_cost
        rand = random.random()
        p = math.pow(math.e, - abs(delta)/t)

        #checks solution 
        if feas and delta < 0: 
            sol = new_sol
            sol_cost = new_cost
            i_since_new_sol = 0 
            if sol_cost < best_cost: 
                best = sol 
                best_cost = sol_cost
        elif feas and rand < p: 
            sol = new_sol 
            sol_cost = new_cost
        else: 
            i_since_new_sol += 1 

        t = a*t #new temprature = cooling rate times current temperature
        temps.append(t)

    total_used_operators = {}
    for idx in range(len(avail_operators)): 
        total_used_operators[avail_operators[idx]] = total_used[idx]

    print(total_used_operators)
    plot(temps)
    return [best, best_cost]

def operators():
    return [insert_two_exchange.__name__, try_for_best.__name__, remove_from_dummy.__name__ \
        , reinsert.__name__, two_exchange.__name__, three_exchange.__name__] 

def set_parameters(): 
    refresh_weigths = 100 
    div_rate = 200 
    return [refresh_weigths, div_rate]

def update_weight(current, weights, index, cost_curr, cost_s, cost_best ): 
    if cost_curr < cost_s: 
        weights[index] += 2 
    id_curr = id(current)
    if id_curr not in solutions_found:
        weights[index] += 1 
        solutions_found.add(id_curr) 
    if cost_curr < cost_best: 
        weights[index] += 4
    return weights

def choose_operator(avail_operators, weights, usage, tot_usage, sol, problem, cost_s, cost_best):
    #choose only one operator with the given weights
    current = None
    op = random.choices(avail_operators, weights = weights, k = 1)[0]
    if op == insert_two_exchange.__name__: 
        current = insert_two_exchange(sol, problem)
    elif op == try_for_best.__name__: 
        current = try_for_best(sol, problem)
    elif op == remove_from_dummy.__name__: 
        current = remove_from_dummy(sol, problem)
    elif op == reinsert.__name__: 
        current = reinsert(sol, problem)
    elif op == two_exchange.__name__: 
        current = two_exchange(sol, problem)
    elif op == three_exchange.__name__: 
        current = three_exchange(sol, problem)
    
    cost_curr = cost_function(current, problem)
    op_idx = avail_operators.index(op)
    current_weight = update_weight(current, weights, op_idx, cost_curr, cost_s, cost_best)
    usage[op_idx] += 1
    tot_usage[op_idx] += 1

    return [current, cost_curr, current_weight, usage, tot_usage]

def normalize_weights(prev, current, usage): 
    r = 0.6
    new_current = prev 
    for i in range(len(new_current)): 
        new_current[i] = prev[i]*(1-r) + r*(current[i]/max(usage[i], 1))
    return new_current

def plot(data): 
    plt.plot(data)
    plt.show()

