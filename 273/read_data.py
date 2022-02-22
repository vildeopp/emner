
file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"

def read_data(filename): 

    all_data = {}

    with open(filename, "r") as f: 
        file = f.readlines()

    line = iter(file)
    next(line) #skips a line 
    nodes = int(next(line)) #number of nodes 
    next(line) #skips line 
    vehicles = int(next(line)) #number of vehicles

    next(line) #skips line

    vehicle_info = {}
    #vehicle_number: home node, starting time, capacity
    for _ in range(vehicles): 
        s_list = list(map(int, next(line).split(",")))
        vehicle_info[s_list[0]] = s_list[1:]
    
    next(line)

    calls = int(next(line)) #number of calls 

    next(line)

    vehicle_trans = {}
    #vehicle index: list of calls that can be transported by that vehicle. 
    for _ in range(vehicles):
        l = list(map(int, next(line).split(",")))
        vehicle_trans[l[0]] = l[1:]
    
    next(line)

    call_info = {}
    #call index: origin node, destination node, size(load), cost of not transporting, lowerbound timewindow for pickup, 
    #upper_timewindow for pickup, lowerbound timewindow for delivery, upper_timewindow for delivery
    for _ in range(calls): 
        l = list(map(int, next(line).split(",")))
        call_info[l[0]] = l[1:]
    
    next(line)

    travel_cost = {}
    #key = (vehicle, node1, node2): travel time (hours), travel cost (euro)
    for _ in range(vehicles*nodes*nodes): 
        l = list(map(int, next(line).split(",")))
        key = (l[0], l[1], l[2])
        travel_cost[key] = l[3:]

    next(line)

    node_time_cost = {}
    #describe each call the timeslot and cost to pickup from pickup node and the timeslot and cost to deliver to destination node
    #key = (vehicle index, calls index), origin node timeslot, origin node cost, destination time slot, destination cost
    for _ in range(calls*vehicles): 
        l = list(map(int, next(line).split(",")))
        key = (l[0], l[1])
        node_time_cost[key] = l[2:]

    f.close()
    
    all_data = dict({'nodes': nodes, 
                    'vehicles': vehicles, 
                    'calls': calls,
                    'call_info': call_info, 
                    'vehicle_info': vehicle_info, 
                    'vehicle_trans':vehicle_trans, 
                    'travel_cost': travel_cost, 
                    'node_time_cost': node_time_cost})
    
    return all_data

def read_problem(): 
    return read_data(file3)



