reset; 

set V; #vessels
set P; #ports

#loading cost pr. barrel at port p on vessel v
param cost{P,V} >= 0;
#supply in port 
param s_P{P} >= 0; 
#fixed cost of using port
param c_P {P} >=0; 
#capacity of vessel 
param cap_V{V} >=0; 
#cost of using vessel
param c_V{V} >= 0; 
#demand at refinery
param d >= 0; 

param Q1 := 99999; #upper bound for first tariff 
param Q2 := 100000; #lower bound for second tariff 
param Q3 := 179999; #upper bound for second tariff 
param Q4 := 180000;  # lower bound for third traiff

param T1{P}; 
param T2{P}; 
param T3{P};  

#the amount loaded in port p on vessel v
var x{P,V} >= 0; 
#if vessel v have visited port p
var k{P,V}binary;
#if port have been visited
var y{P}binary; 
#if vessel have been used
var z{V}binary; 

var Qa{P,V} binary; 
var Qb{P,V} binary; 
var Qc{P,V} binary; 

var X1{P,V} >= 0; 
var X2{P,V} >= 0; 
var X3{P,V} >= 0; 



#want to minimize the sum og loading cost and fixed costs
minimize total_cost: sum {p in P, v in V} (X1[p,v]*T1[p]+X2[p,v]*T2[p]+X3[p,v]*T3[p]) + sum {i in P} c_P[i] * y[i] + sum {i in V} c_V[i] *  z[i];

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

subject to X1_upperbound {p in P, v in V}: X1[p,v] - Q1*Qa[p,v] <= 0; 

subject to X2_lowerbound {p in P, v in V}: X2[p,v] - Q2*Qb[p,v] >= 0; 

subject to X2_upperbound {p in P, v in V}:X2[p,v]-Q3*Qb[p,v]<= 0; 

subject to X3_lowerbound {p in P, v in V}:X3[p,v]-Q4*Qc[p,v]>=0; 

subject to X3_upperbound {p in P, v in V}:X3[p,v]<=cap_V[v]*Qc[p,v]; 

subject to maximum_traiff {p in P, v in V}: Qa[p,v]+Qb[p,v]+Qc[p,v] <= 1; 

subject to combines {p in P, v in V}:X1[p,v]+X2[p,v]+X3[p,v]=x[p,v]; 














 