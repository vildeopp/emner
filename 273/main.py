from feasibility_check import feasibility
import random_solution as rnd
import random_init as init
from search_algorithms import local_search
from operators import basic as b

files = ["data/Call_7_Vehicle_3.txt", "data/Call_18_Vehicle_5.txt", "data/Call_35_Vehicle_7.txt", \
         "data/Call_80_Vehicle_20.txt", "data/Call_130_Vehicle_40.txt", "data/Call_300_Vehicle_90.txt"]
def main():

    init_solution = rnd.random_dummy_route()
    init.random_solution_initializer(init_solution, 10)

    init_solution = rnd.new_random_sol()
    local_search.local_search(init_solution, b.one_reinsert)


if __name__ == '__main__': 
    main()