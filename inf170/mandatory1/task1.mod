reset;
var a;
var b;

maximize profit: (20-b)*a + (57-0.1*a)*b - (7*a + 11*b + 100);

subject to aNotNull: a >= 0;
subject to bNotNull: b >= 0;
subject to tot: a+b = 50;

solve;
display a, b, profit;