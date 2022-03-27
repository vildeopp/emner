
import statistics
import datetime as dt
import sys

from operators import reinsert, two_exchange, three_exchange
from simulated_annealing import simulated_annealing, simulated_annealing_equal_weigths
from PDP_utils import cost_function, feasibility_check
from display import print_sol



def intitalizer(init_sol, problem, times):
    inital_cost = cost_function(init_sol, problem)

    operators = [reinsert, two_exchange, three_exchange]

    for operator in operators:
        print("operator: ", str(operator.__name__))
        print("- " * 25)

        best_objective = inital_cost
        best_solution = init_sol
        avg_of_best = best_objective*times
        feasible_of_best, c = feasibility_check(init_sol, problem)

        best_runtime = sys.maxsize
        for _ in range(times):
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

def initializer_weigths(init_sol, problem, iterations):
    cost = cost_function(init_sol,problem)
    solution = init_sol
    feasible = feasibility_check(init_sol, problem)

    runtimes = 0
    objectives = 0

    for _ in range(iterations):
        print("iterations", _)
        start = dt.datetime.now()
        new_solution, new_objective, new_feasible = simulated_annealing_equal_weigths(solution, problem)

        stop = dt.datetime.now()
        total = (stop-start).total_seconds()
        runtimes += total
        objectives += new_objective

        if feasible and new_objective < cost:
            solution = new_solution
            cost = new_objective
            feasible = new_feasible

    mean_objectives = objectives/iterations
    mean_runtimes = runtimes/iterations

    print_sol(mean_objectives, cost, cost_function(init_sol, problem), mean_runtimes, solution, feasible)
