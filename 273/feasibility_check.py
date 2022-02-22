from collections import Counter
import time_calc as time

def feasibility(problem, solution): 
   
    feasible = True
    calls_info = problem['call_info']
    current_vehicle = 1
    current_load = 0 #variable to keep track of the current load on the current vehicle

    current_route = []

    for calls in solution:

        if calls == 0: #this marks the switch of vehicles
            current_vehicle += 1 

            cnt_calls = Counter(current_route) 
            for call, value in cnt_calls.items(): 
                if value < 2: 
                    feasible = False
                    print("node appears more than twice")
                    break
            current_load = 0 #when changing to next vehicle, also change the current load to zero
            current_route = [] #empty the current route
            continue
      
        if current_vehicle <= problem['vehicles']: #checks if there are less current vehicles than what is given
            current_cap = problem['vehicle_info'].get(current_vehicle)[2] #the capacity of the current vehicle
                #checks if the current load is larger than the current capacity 
            if current_load > current_cap: 
                feasible = False
                print("Load is larger than capacity")
                break
                
                #Check call and vehicle compatibility
            valid_calls = problem['vehicle_trans']
            if calls not in valid_calls:
                feasible = False
                break

            if calls not in current_route: 
                current_route.append(calls)
                current_load += calls_info.get(calls)[2]  #gets the size of the current call
            else: 
                current_route.append(calls)
                current_load -= calls_info.get(calls)[2] #subtracts the size of the delivery load

        
        #break if the route uses the dumme vehicle because that is not supposed to feasiblity checked 
        else:
            break

    for v in range(1, problem["vehicles"]+1):
        if not time.time_feasability(solution, v):
            feasible = False
            break
        
    return feasible





