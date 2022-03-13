from collections import Counter

import random_solution_gen as rnd
import random_initializer as rnd_init
import PDP_utils as pdp
import operators as o
import localsearch as local
import simulated_annealing as sim 
import simulated_annealing_init as s
import local_search_init as l 

file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"

def main():
    """Read problem"""
    print("loads file")
    problem = pdp.load_problem(file6)
    print("finished loading file")

    """Initial solutions"""
    init = rnd.new_random_sol(problem)
    init2 = rnd.random_dummy_route(problem)

    """Initializers for search"""
    #print("simulated annealing")
    #s.intitalizer(init2, problem, 10)
    print("local search")
    l.initalizer(init2, problem, 10)

    #cnt = Counter([4, 4, 21, 21, 0, 30, 7, 7, 30, 29, 29, 0, 9, 9, 24, 24, 0, 16, 16, 1, 3, 3, 1, 32, 32, 0, 23, 8, 23, 27, 27, 8, 31, 31, 0, 14, 6, 6, 14, 13, 13, 0, 10, 10, 0, 35, 35, 28, 28, 20, 20, 22, 22, 11, 11, 18, 18, 19, 19, 12, 12, 17, 17, 33, 33, 15, 15, 25, 25, 2, 2, 34, 34, 5, 5, 26, 26])
    #print([value for key, value in cnt.items() if key != 0])

    #print(pdp.feasibility_check([0, 0, 0, 0, 0, 0, 0, 2, 2, 15, 15, 10, 10, 1, 1, 20, 20, 26, 26, 27, 27, 19, 19, 16, 16, 12, 12, 5, 5, 30, 30, 23, 23, 17, 17, 18, 18, 11, 11, 6, 6, 8, 8, 24, 24, 25, 25, 22, 22, 33, 33, 31, 31, 32, 32, 21, 21, 28, 28, 9, 9, 3, 3, 29, 29, 35, 35, 14, 14, 34, 34, 13, 13, 4, 4, 7, 7], problem))
if __name__ == '__main__':
    main()