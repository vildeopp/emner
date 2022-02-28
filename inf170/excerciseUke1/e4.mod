reset; 
var xbread >= 0; var xmeat >=0; var xpot >= 0; var xcab >= 0; 
var xmilk >= 0; var xgel >= 0;
 
minimize cost: 0.30*xbread + xmeat + 0.05*xpot + 0.08*xcab + 0.23*xmilk + 0.48*xgel;

subject to calories: 1245*xbread + 1457*xmeat + 318*xpot + 46*xcab + 309*xmilk + 1725*xgel >= 3000; 
subject to protein: 39*xbread + 73*xmeat + 8*xpot + 4*xcab + 16*xmilk + 43*xgel >= 70; 
subject to calcium: 418*xbread + 41*xmeat + 42*xpot + 141*xcab + 536*xmilk >= 800; 
subject to vitaminA: 70*xpot + 860*xcab + 720*xmilk >= 500; 
solve; 
display xbread, xmeat, xpot, xcab, xmilk, xgel; 