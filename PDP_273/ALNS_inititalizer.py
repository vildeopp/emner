import datetime as dt
import sys
from statistics import mean

from random_solution_gen import random_dummy_route
from PDP_utils import cost_function, feasibility_check
from ALNS import adaptive_large_neighborhood_search
from display import print_sol


def ALNS_inititalizer(problem, iterations, runtime): 
    init_sol = random_dummy_route(problem)
    inital_cost = cost_function(init_sol, problem)


    best_it = 0
    best_objective = inital_cost
    best_solution = init_sol
    feasible_of_best, c = feasibility_check(init_sol, problem)
    objectives = []
    runtimes = 0
    
    for _ in range(iterations):
        runtime_start = dt.datetime.now()
        new_solution, new_objective = adaptive_large_neighborhood_search(problem, runtime)
        runtime_stop = dt.datetime.now()
        objectives.append(new_objective)
        if new_objective < best_objective:
            best_solution = new_solution
            best_objective = new_objective
            best_it = _ 

        total_runtime = (runtime_stop - runtime_start).total_seconds()

        runtimes += total_runtime

    print("best iteration", best_it)
    print("-"*25)

    print_sol(mean(objectives), best_objective, inital_cost, runtimes/iterations, best_solution, feasible_of_best)
