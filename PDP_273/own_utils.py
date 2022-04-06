import numpy as np

def cost_route(route, vehicle, problem):
    """
    :param Solution: the proposed solution for the order of calls in each vehicle
    :param problem:
    :return:
    """

    num_vehicles = problem['n_vehicles']
    Cargo = problem['Cargo']
    TravelCost = problem['TravelCost']
    FirstTravelCost = problem['FirstTravelCost']
    print(FirstTravelCost)
    PortCost = problem['PortCost']


    NotTransportCost = 0
    RouteTravelCost = np.zeros(num_vehicles)
    CostInPorts = np.zeros(num_vehicles)

    route = np.append(route, [0])

    currentVPlan = route
    currentVPlan = currentVPlan - 1
    NoDoubleCallOnVehicle = len(currentVPlan)

    i = vehicle - 1

    if i == num_vehicles:
        print("dummy")
        NotTransportCost = np.sum(Cargo[currentVPlan, 3]) / 2
    else:
        if NoDoubleCallOnVehicle > 0:
            sortRout = np.sort(currentVPlan, kind='mergesort')
            I = np.argsort(currentVPlan, kind='mergesort')
            Indx = np.argsort(I, kind='mergesort')
            PortIndex = Cargo[sortRout, 1].astype(int)
            PortIndex[::2] = Cargo[sortRout[::2], 0]
            PortIndex = PortIndex[Indx] - 1
            Diag = TravelCost[i, PortIndex[:-1], PortIndex[1:]]
            FirstVisitCost = FirstTravelCost[i, int(Cargo[currentVPlan[0], 0] - 1)]
            RouteTravelCost[i] = np.sum(np.hstack((FirstVisitCost, Diag.flatten())))
            CostInPorts[i] = np.sum(PortCost[i, currentVPlan]) / 2

    TotalCost = NotTransportCost + sum(RouteTravelCost) + sum(CostInPorts)
    return TotalCost