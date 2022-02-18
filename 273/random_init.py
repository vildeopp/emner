from audioop import avg
from datetime import date, datetime
import sys

import cost_calculation as cost
import blind_r_search as random_search
import read_data as r
import feasibility_check as f
import print as p

problem = r.read_problem()


def random_solution_initializer(init_solution: list, iterations: int):
    print("Starting search\n")

    init_cost = cost.f(problem, init_solution)

    best_objective = init_cost
    sum_objectives = 0
    best_solution = init_solution
    best_runtime = sys.maxsize  # the largest size in python
    for _ in range(iterations):
        start_run = datetime.now()
        new_sol, new_cost = random_search.blind_random_search(init_solution)
        if new_cost < best_objective and f.feasibility(problem, new_sol):
            best_solution = new_sol
            best_objective = new_cost
        sum_objectives += new_cost
        stop_run = datetime.now()
        total_runtime = (stop_run - start_run).total_seconds()
        if total_runtime < best_runtime:
            best_runtime = total_runtime


    avg_obj = sum_objectives/iterations
    
    p.print_sol(avg_obj, best_objective, init_cost, best_runtime, 
                best_solution, f.feasibility(problem, best_solution))

    print("\nSearch ended")
