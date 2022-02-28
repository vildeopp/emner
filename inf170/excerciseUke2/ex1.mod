reset; 

var x1 >= 0; var x2 >= 0; var x3 >= 0; var x4 >= 0; var x5 >= 0; var x6 >= 0;
var s1 >= 0; var s2 >= 0; var s3 >= 0; var s4 >= 0; var s5 >= 0; var s6 >= 0; 

minimize cost: 50*x1 + 45*x2 + 55*x3 + 48*x4 + 52*x5 + 50*x6 
				+ 8*(s1 + s2 + s3 + s4 + s5 + s6); 

subject to _x1: x1 - s1 >= 100; 
subject to _x2: x2 + s1 - s2 >= 250; 
subject to _x3: x3 + s2 - s3 >= 190; 
subject to _x4: x4 + s3 - s4 >= 140; 
subject to _x5: x5 + s4 - s5 >= 220;
subject to _x6: x6 + s5 - s6 >= 110;

solve; 
display x1, x2, x3, x4, x5, x6; 

