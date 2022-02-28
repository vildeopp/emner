reset; 

set Nv; #nodes that can be visited
set Np within Nv; #loading nodes 
set Nd within Nv; #unloading nodes
set A := {i in Nv,j in Nv: i <> j}; #arches 

param o ; #origin
param d ; #destination

param Q {Np}; #amount of cargo

param K; #capacity

param BigM; #large number
param cs; #cost of spot charter

param D {Nv, Nv}; #cost and traveltime from node i to node j

param t0 := 0; 
param n := 10; 
 
var t{Nv} >= 0; #total of service time at node i
var l{Nv} >= 0;  #total load on board after completing service at node i
var x {Nv, Nv} binary; #if a cargo is shiped directly from node i to node j
var y {Np} binary; #if a cargo is shiped with spot charter

#Objective function
minimize objective: 
	sum {(i,j) in A} D[i,j]*x[i,j] + sum {i in Np} cs*y[i];

subject to ship {i in Np}: sum {(i,j) in A} x[i,j] + y[i] = 1; 

subject to start: sum {j in Nv: j<>o} x[o,j]=1;

subject to goBack {i in Np union Nd}: sum {(i,j) in A} x[i,j] - sum{(w,i) in A: i <> w} x[w,i] = 0;

subject to destination: sum {j in Nv: j<>d} x[j,d] = 1; 

subject to cons {j in Np, (i,j) in A}: l[i] + Q[j] - l[j] <= K*(1 - x[i,j]); #denne her skjønte jeg ikke 

subject to six {j in Np, (i,n+j) in A: i <> n+j}: l[i] - Q[j] - l[(n+j)] <= K*(1-x[i,j+n]);

subject to pos_load_cap {i in Np}: 0 <= l[i] <= K;

subject to bigM1 {(i,j) in A: i = o}:t0+D[i,j]-t[j]<=BigM*(1 - x[i,j]); 

subject to bigM2 {(i,j) in A: i<>o}: t[i] + D[i,j] - t[j] <= BigM * (1 - x[i,j]); 

subject to ring {i in Np}: sum {(i,j) in A} x[i,j] - sum {(n+i,j) in A: j<>n+i} x[n+i,j] = 0; 

subject to cons2 {i in Np}: t[i] + D[i, i+n] - t[n+i] <= 0; 

subject to boolean_Y {i in Np}: y[i]in{0,1}; 

subject to boolean_X {i in Nv, j in Nv}: x[i,j]in{0,1}; 

subject to pos_load {i in Nv}: l[i]>=0; 

subject to pos_time {i in Nv}: t[i]>=0; 
