from mimetypes import init

from numpy import nested_iters
from operators import reinsert, two_exchange, three_exhcange
from simulated_annealing import simulated_annealing
import datetime as dt
import sys
from PDP_utils import cost_function
from display import print_sol

def intitalizer(init_sol, problem, times): 

    inital_cost = cost_function(init_sol, problem)
    
    operators = [reinsert]

    for operator in operators:
        print("operator: ", str(operator))
        print("-"*25)

        best_objective = sys.maxsize
        best_solution = []
        avg_of_best = 0 
        feasible_of_best = False

        best_runtime = sys.maxsize
        for _ in range(times):
            print("iteration: ", _+1)
            runtime_start = dt.datetime.now()
            new_solution, new_objective, feasible, avg_objectives = simulated_annealing(init_sol, problem, operator)
            runtime_stop = dt.datetime.now()
            if feasible and new_objective < best_objective: 
                best_solution = new_solution
                best_objective = new_objective
                avg_of_best = avg_objectives
                feasible_of_best = feasible

            total_runtime = (runtime_stop - runtime_start).total_seconds()

            if total_runtime < best_runtime: 
                best_runtime = total_runtime
        
        print_sol(avg_of_best, best_objective, inital_cost, best_runtime, best_solution, feasible_of_best)


