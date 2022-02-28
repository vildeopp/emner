reset; 
var x1 >= 0; var x2 <= 2; 

maximize profit: 5*x1 + 4*x2; 

subject to M1: 6*x1 + 4*x2 <= 24; 
subject to M2: x1 + 2*x2 <= 6; 
subject to demandx1: x2 - x1 <= 1; 
subject to demandx2: x2 <= 2; 

solve; 

display x1, x2; 