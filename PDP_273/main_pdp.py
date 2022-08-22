import time
from itertools import permutations
import random_solution_gen as rnd
import random_initializer as rnd_init
import PDP_utils as pdp
import basic_operators as o
import localsearch as local
import simulated_annealing as sim
import simulated_annealing_init as s
import local_search_init as l
import greedy_operators as op
import check_validity as c
import route_operators as route
import random
import own_utils as own_pdp
from operators import insert_two_exchange, remove_from_dummy, remove_k_calls, escape, move_to_next_vehicle
from greedy_operators import  try_for_best
import ALNS 
import ALNS_inititalizer 

file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"


def get_runtime(): 
    dict = { file2: 40,file3:60, file4: 290}
    return dict

def main():
    """Initial solutions"""
    problem = pdp.load_problem(file2)
    init = rnd.random_dummy_route(problem)
    """Initializers for search"""
#   ALNS_inititalizer.ALNS_inititalizer(problem, 1, 500)
   


    for file, runtime in get_runtime().items(): 
        print("read file", file)
        problem = pdp.load_problem(file)
        ALNS_inititalizer.ALNS_inititalizer(problem, 10, runtime)

    

if __name__ == '__main__':
    main()
