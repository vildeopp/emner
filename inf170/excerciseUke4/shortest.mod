reset; 

set INTER; 

param entr symbolic in INTER; 
param exit symbolic in INTER, <> entr; 

set ROADS within (INTER diff {exit}) cross (INTER diff {entr}); 

param time {ROADS} >= 0; 
var Use {(i,j) in ROADS} >= 0;

minimize Total_Time: sum {(i,j) in ROADS} time[i,j] * Use[i,j];

subject to Start:  sum {(entr,j) in ROADS} Use[entr,j] = 1;

subject to Balance {k in INTER diff {entr,exit}}:
   sum {(i,k) in ROADS} Use[i,k] = sum {(k,j) in ROADS} Use[k,j];
