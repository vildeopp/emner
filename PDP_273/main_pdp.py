
import random_solution_gen as rnd
import random_initializer as rnd_init
import PDP_utils as pdp

file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"

def main():
    problem = pdp.load_problem(file1)
    init = rnd.new_random_sol(problem)
    #init = [3, 3, 7, 7, 0, 5, 5, 4, 4, 1, 1, 2, 2, 6, 6, 0, 0]
    #print(pdp.feasibility_check(init, problem))
    
    rnd_init.random_init(init, 10, problem)

if __name__ == '__main__':
    main()