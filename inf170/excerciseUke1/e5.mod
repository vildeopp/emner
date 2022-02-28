
reset; 
var walk >= 0; var jogg >= 0; var swim >= 0; var mach >= 0; 
var indo >= 0; var push >= 0; 

minimize time: walk + jogg + swim + mach + indo + push; 
subject to Calories: 100*walk + 200*jogg + 300*swim + 
		150*mach + 300*indo + 500*push >= 2000; 
subject to tolWalk: 1 <= walk <= 5; 
subject to tolJogg: 1 <= jogg <= 2; 
subject to tols: 1 <= swim <= 3; 
subject to tolm: 1 <= mach <= 3.5;
subject to toli: indo <= 3; 
subject to tolp: push <= 0.5;
subject to notToMuch: walk + jogg + mach <= 4; 
solve; 
display walk, jogg, swim, mach, indo, push; 


