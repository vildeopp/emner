from collections import Counter

import operators as o
import PDP_utils as pdp
from display import print_sol

def local_search(init_sol, problem, operator):

    print("start local search\n")

    solution = init_sol
    objective = pdp.cost_function(init_sol, problem)
    sum_objective = 0
    
    for _ in range(1000):
        new_solution = operator(solution, problem)
        new_objective = pdp.cost_function(new_solution, problem)
        feasible, c = pdp.feasibility_check(new_solution, problem)
        #print(new_solution)
        sum_objective += new_objective
        if feasible and new_objective < objective:
            #print("better", new_solution)
            solution = new_solution
            objective = new_objective

    feasible, c = pdp.feasibility_check(solution, problem)
    return solution, objective, feasible, sum_objective/1000
    
