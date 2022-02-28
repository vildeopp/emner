reset; 
set INTER; 

param entr symbolic in INTER; 
param exit symbolic in INTER, <> entr; 

set ROADS within (INTER diff {exit}) cross (INTER diff {entr}); 

param cap {ROADS} >= 0; 
var Traf {(i,j) in ROADS} >= 0, <= cap[i,j]; 

maximize enteringTraffic: sum {(entr, j) in ROADS} Traf[entr, j]; 

subject to Balance {k in INTER diff {entr, exit}}: 
	sum {(i,k) in ROADS} Traf[i,k] = sum {(k,j) in ROADS} Traf[k,j]; 

