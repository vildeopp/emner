import sys
from basic_operators import reinsert, two_exchange, three_exchange
from PDP_utils import cost_function
from localsearch import local_search
import datetime as dt
from display import print_sol


def initalizer(init_sol, problem, iterations): 
    inital_cost = cost_function(init_sol, problem)
    operators = [reinsert, two_exchange, three_exchange]

    for operator in operators: 
        print("operator: ", operator.__name__)
        print("-"*25)

        best_sol = init_sol
        best_obj =inital_cost
        avg_of_best = 0 
        feasible_of_best = False 

        best_runtime = 0

        for i in range(iterations):
            print("iteration " , i+1)
            start_time = dt.datetime.now()
            new_solution, new_objective, feasible, avg_objective = local_search(init_sol, problem, operator)
            stop_time = dt.datetime.now()

            if new_objective < best_obj and feasible: 
                best_sol = new_solution
                best_obj = new_objective
                feasible_of_best = feasible
                avg_of_best = avg_objective

            runtime = (stop_time - start_time).total_seconds()
            best_runtime += runtime

        avg_runtime = best_runtime/iterations

        print_sol(avg_of_best, best_obj, inital_cost, avg_runtime, best_sol, feasible_of_best)