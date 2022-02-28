#Oppgave1
a) 
SELECT Name FROM Cities WHERE AREA < 2000 ORDER BY Area DESC;
b) 
SELECT Country1, COUNT(Country2) AS AntallNaboer FROM Border AS B
    GROUP BY Country1 HAVING AntallNaboer > 2
c) 
SELECT c.Name AS Country, p.Number AS Population FROM Countries AS c, Population AS p
    WHERE p.Name = c.Name AND Year = 1980 
    ORDER BY p.Number DESC
d) 
SELECT Cit.Name AS Captial FROM Population AS P, Countries AS Con, Cities AS Cit 
    WHERE P.Name = Con.Name AND Cit.Name = Con.Capital_city 
    AND P.number < 1000000 AND P.year = 2000
e) 
SELECT c.Name AS Country, c.Area/p.Number AS Density FROM Countries AS c, Population as p
    WHERE c.Name = p.Name AND Year = 2015
    ORDER BY Density DESC

#Oppgave2 
a) 

