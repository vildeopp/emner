reset; 

set COUNTRIES; 
set PRODUCTS; 

param minCap {COUNTRIES} >= 0; 
param maxCap {COUNTRIES} >= 0; 

param demand {PRODUCTS} >= 0; 
param cost {COUNTRIES, PRODUCTS} >= 0; 
param fixedCost {COUNTRIES} >= 0; 

var inProd {c in COUNTRIES} binary; 
var production {c in COUNTRIES, p in PRODUCTS} >= 0; 

minimize TC: 
	sum {i in COUNTRIES} (sum {p in PRODUCTS} production[i,p]*cost[i,p] + inProd[i]*fixedCost[i]); 

subject to MinCap {i in COUNTRIES}: minCap[i]*inProd[i] <= sum {p in PRODUCTS} production[i,p];
subject to MaxCap {i in COUNTRIES}: maxCap[i]*inProd[i] >= sum {p in PRODUCTS} production[i,p];
subject to Demand {p in PRODUCTS}: sum {i in COUNTRIES} (production[i,p]) >= demand[p]; 

data; 

param: COUNTRIES: maxCap minCap fixedCost:= 
		NET			325		100		1500
		DEN			300		150		2500
		SWE			950		700		1250; 
	
param: PRODUCTS: demand:= 
		A			550
		B			450; 
		
param cost:	A		B:= 
	NET 	14		13 
	DEN 	12.5	17.5
	SWE		21		22.5; 




