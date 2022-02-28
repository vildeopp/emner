
#Oppgave 1 
#a
SELECT * FROM Tur 
WHERE MONTH(Tur.StartDato) = 7 AND Tur.pris < 8000
ORDER BY Pris, StartDato;
#velger alle entries i tabellen tur hvor startmåneden er juli og prisen en under 8000 kr

#b 
SELECT m.* 
FROM Medlem AS m, Tur AS t, Hytte AS h
WHERE m.MNr = t.Mnr AND t.HNr = h.HNr
AND t.startHytte = 2; 
#velger unike medlemmer som skal være med på turer der hyttenummer to er start hytten.

#c 
SELECT TNr, Beskrivelse, startDato, COUNT(*) AS Antall 
FROM Tur, Påmelding 
WHERe Tur.TNr = Påmelding.TNr 
GROUP BY Påmelding.TNr; 

#d
CREATE TABLE Hytte{
    HNr INTEGER AUTO_INCREMENT, 
    Navn VARCHAR(50) NOT NULL, 
    AntSenger INTEGER, 
    HytteType VARCHAR(20), 
    CONSTRAINT Hytte_PK PRIMARY KEY (HNr)
};

#e
INSERT INTO Medlem
VALUES ('Ola', 'Nordmann', 99900022);
INSERT INTO Påmelding 
VALUES(3, LAST_INSERT_ID()); 
COMMIT; 

#f
SELECT * FROM Medlem 
WHERE MNr NOT IN (SELECT MNr FROM Påmelding); 

#Oppegave 3 
#a 
SELECT Tur.Pris
FROM Tur, Hytte 
WHERE Tur.TNr = Hytte.startHytte
AND Hytte.Type = Selbetjent 
AND Tur.Beskrivelse = Brevandring; 

