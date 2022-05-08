import datetime as dt
import sys
from statistics import mean

from random_solution_gen import random_dummy_route
from PDP_utils import cost_function, feasibility_check
from ALNS import adaptive_large_neighborhood_search
from display import print_sol


def ALNS_inititalizer(problem, iterations): 
    init_sol = random_dummy_route(problem)
    inital_cost = cost_function(init_sol, problem)


    best_it = 0
    best_objective = inital_cost
    best_solution = init_sol
    avg_of_best = best_objective*iterations
    feasible_of_best, c = feasibility_check(init_sol, problem)
    objectives = []

    best_runtime = sys.maxsize
    for _ in range(iterations):
        runtime_start = dt.datetime.now()
        new_solution, new_objective = adaptive_large_neighborhood_search(problem)
        runtime_stop = dt.datetime.now()
        objectives.append(new_objective)
        if new_objective < best_objective:
            best_solution = new_solution
            best_objective = new_objective
            best_it = _ 

        total_runtime = (runtime_stop - runtime_start).total_seconds()

        if total_runtime < best_runtime:
            best_runtime = total_runtime

    print("best iteration", best_it)
    print("-"*25)

    print_sol(mean(objectives), best_objective, inital_cost, best_runtime, best_solution, feasible_of_best)
