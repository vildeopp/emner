
import random_init as rnd_init
import random_solution as rnd
import PDP_utils as pdp

file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"

def main():
    problem = pdp.load_problem(file1)
    init_sol = rnd.random_dummy_route()
    rnd_init.random_solution_initializer(init_sol, 10)

if __name__ == '__main__':
    main()