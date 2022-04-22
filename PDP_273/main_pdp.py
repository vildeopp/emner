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
from operators import insert_two_exchange, remove_from_dummy

file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"


def main():
    """Read problem"""
    print("loads file")
    problem = pdp.load_problem(file5)
    print("finished loading file")

    """Initial solutions"""
    init = rnd.new_random_sol(problem)
    init2 = rnd.random_dummy_route(problem)

    """Initializers for search"""
    #print("simulated annealing")
    #s.intitalizer(init2, problem, 10)
    #print("local search")
    #l.initalizer(init2, problem, 10)

    travelCost = problem['TravelCost']
    vesselCargo = problem['VesselCargo']
    cargo = problem['Cargo']
    a = problem['PortCost']


    #print("simulated annealing equal weights ")
    s.initializer_weigths(init2, problem, 10)
 

if __name__ == '__main__':
    main()
