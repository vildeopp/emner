reset; 

set V; #vessels
set P; #ports

#loading cost pr. barrel at port p on vessel v
param cost{P,V};
#supply in port 
param s_P{P} >= 0; 
#fixed cost of using port
param c_P {P} >=0; 
#capacity of vessel 
param cap_V{V}>=0; 
#cost of using vessel
param c_V{V} >= 0; 
#demand at refinery
param d >= 0; 

#the amount loaded in port p on vessel v
var x{P,V}>= 0; 
#if vessel v have visited port p
var k{P,V}binary;
#if port have been visited
var y{P}binary; 
#if vessel have been used
var z{V}binary; 

#want to minimize the sum og loading cost and fixed costs
minimize total_cost: sum {i in P, j in V} cost[i,j] * x[i,j] + sum {i  in P} c_P[i] * y[i] + 
		sum {i in V} c_V[i] *  z[i];

#need to meet the refinerys daily demand
subject to demand: sum {p in P, v in V} x[p,v] = d; 

#the daily supply in each port
subject to supply {p in P}: sum {v in V} x[p,v] <= s_P[p]; 

#the loading capacity at each port
subject to cap {v in V}: sum {p in P} x[p,v] <= cap_V[v]; 

#Each vessel can only visit maximum two ports daily
subject to cap_ports {v in V}: sum{p in P} k[p,v] <=2; 

#keep track of which vessel have visited which port
subject to P_V_combo {p in P, v in V}: x[p,v] - k[p,v] * cap_V[v]<=0; 

#fixed cost of ports
subject to cost_P {p in P, v in V}: x[p,v] - y[p] * s_P[p] <=0; 

#fixed cost of vessels
subject to cost_V {p in P, v in V}: x[p,v] - z[v] * cap_V[v] <= 0; 


