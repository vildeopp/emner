reset; 
var x1; var x2; var x3; var x4; 
var y1; var y2; var y3; var y4; 

maximize profit: (30*x1 + 40*x2 + 20*x3 + 10*x4) - 
			(15*(800 - x1) + 20*(750 - x2) + 10*(600-x3) + 8*(500-x4)); 
			
subject to cutting: 0.3*x1 + 0.3*x2 + 0.25*x3 + 0.15*x4 <= 1000;
subject to insulating: 0.25*x1 + 0.35*x2 + 0.3*x3 + 0.1*x4 <= 1000;
subject to sewing: 0.45*x1 + 0.5*x2 + 0.4*x3 + 0.22*x4 <= 1000;
subject to packaging: 0.15*x1 + 0.15*x2 + 0.1*x3 + 0.05*x4 <= 1000;

subject to dem1: x1 <= 800;
subject to dem2: x2 <= 750;
subject to dem3: x3 <= 600;
subject to dem4: x4 <= 500; 

solve; 

display x1, x2, x3, x4; 