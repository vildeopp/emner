import time
import PDP_utils as pdp
import random as rnd
import math
from display import print_sol
from statistics import mean
from greedy_operators import replace_vehicles_calls, two_exchange_reinsert, try_for_best_dummy_insert
import random
from tqdm import tqdm
from basic_operators import two_exchange
from operators import insert_two_exchange, remove_from_dummy, try_for_best, escape

import matplotlib.pyplot as plt

def simulated_annealing(init_sol, problem, operator):
    pbar = tqdm(total=10000, position=0, leave=True)

    Tf = 0.1  # final temperature
    incumbent = init_sol
    inc_objective = pdp.cost_function(incumbent, problem)
    best_solution = init_sol
    best_objective = pdp.cost_function(best_solution, problem)

    delta = []  # store the feasible deltas

    sum_objectives = pdp.cost_function(init_sol, problem)  # sum of objectives to calculate average objective
    # "warm-up"
    for _ in range(100):
        pbar.update(1)
        new_solution = operator(incumbent, problem)
        new_objective = pdp.cost_function(new_solution, problem)
        delta_E = new_objective - inc_objective
        feasible, c = pdp.feasibility_check(new_solution, problem)
        sum_objectives += new_objective
        if feasible and delta_E < 0:  # if the new solution is feasible and the incumbent objective is larger than the objective of the new solution
            incumbent = new_solution
            inc_objective = new_objective
            if inc_objective < best_objective:
                best_solution = incumbent
                best_objective = inc_objective
        elif feasible:
            rand = rnd.random()  # returns a floating point between 0 and 1
            if rand < 0.8:
                incumbent = new_solution
                inc_objective = new_objective

            delta.append(delta_E)  # adds delta E to the deltas

    delta_avg = mean(delta)
    t_null = (-delta_avg) / math.log(0.8)
    alpha = pow(Tf / t_null, 1 / 9900)
    t = t_null

    for _ in range(9900):
        pbar.update(1)
        new_solution = operator(incumbent, problem)
        new_objective = pdp.cost_function(new_solution, problem)
        delta_E = new_objective - inc_objective
        feasible, c = pdp.feasibility_check(new_solution, problem)
        sum_objectives += new_objective
        if feasible and delta_E < 0:
            incumbent = new_solution
            inc_objective = new_objective
            if inc_objective < best_objective:
                best_solution = incumbent
                best_objective = inc_objective
            elif feasible:
                rand = rnd.random()
                p = math.pow(math.e, (-delta_E / t))
                if rand < p:
                    incumbent = new_solution
                    inc_objective = new_objective
            t = alpha * t
    avg_objectives = sum_objectives / 1000

    return best_solution, best_objective, feasible, avg_objectives


def simulated_annealing_equal_weigths(init_sol, problem, runtime):

    tempratures = [] #store each iterations tempratures to plot
    prob = []
    
    pbar = tqdm(total=10000, position=0, leave=True)
    Tf = 0.1  # final temperature
    incumbent = init_sol
    inc_objective = pdp.cost_function(incumbent, problem)
    best_solution = init_sol
    best_objective = pdp.cost_function(best_solution, problem)

    delta = []  # store the feasible deltas

    sum_objectives = pdp.cost_function(init_sol, problem)

    last_impr = 0 
    its_since_update = 0

    #parameters 
    div_rate = 250 

    stop = time.time() + runtime 
    
    for _ in range(100):
        pbar.update(1)
        new_solution = choose_operator(incumbent, problem)
        objective = pdp.cost_function(new_solution, problem)

        delta_E = objective - inc_objective
        feasible, c = pdp.feasibility_check(new_solution, problem)
        sum_objectives += objective
        if feasible and delta_E < 0:
            incumbent = new_solution
            inc_objective = objective
            if inc_objective < best_objective:
                best_objective = inc_objective
                best_solution = incumbent
                last_impr = _
        elif feasible:
            rand = rnd.random()
            if rand < 0.8:
                incumbent = new_solution
                inc_objective = objective
            delta.append(delta_E)

    
    t_null = 0.999 #(-delta_avg) / math.log(0.8)
    alpha = pow(Tf / t_null, 1 / 9900)
    t = t_null
    it = 0

    while it < 19900 or time.time() < stop: 
        if it == 19900: 
            break 

        tempratures.append(t)
        pbar.update(1)

        if its_since_update == div_rate: 
            incumbent = escape(incumbent, problem)
            its_since_update = 0 
            continue

        new_solution = choose_operator(incumbent, problem)
        objective = pdp.cost_function(new_solution, problem)

        delta_E = objective - inc_objective
        feasible, c = pdp.feasibility_check(new_solution, problem)
        sum_objectives += objective
        if feasible and delta_E < 0:
            incumbent = new_solution
            inc_objective = objective
            if inc_objective < best_objective:
                best_objective = inc_objective
                best_solution = incumbent
                last_impr = it
                its_since_update = 0
        elif feasible:
            rand = rnd.random()
            p = math.pow(math.e, (-delta_E / t))
            if rand < p:
                incumbent = new_solution
                inc_objective = objective
            else: 
                its_since_update += 1
            t = alpha * t
        else: 
            its_since_update += 1 
        it += 1 
    print("last improvement", last_impr) 

    #plot_data(data = tempratures)
    return best_solution, best_objective, pdp.feasibility_check(best_solution, problem)


def choose_operator(incumbent, problem):
    p1 = 0.33
    p2 = 0.33
    prob = random.uniform(0, 1)
    if prob < p1:
        new_solution = try_for_best_dummy_insert(incumbent, problem)
    elif p1 < prob < p2:
        new_solution = try_for_best(incumbent, problem)
    else:
        new_solution = insert_two_exchange(incumbent, problem)
    return new_solution

def plot_data(data): 
    plt.plot(data)
    plt.show()


