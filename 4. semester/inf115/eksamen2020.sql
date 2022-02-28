#Oppgave 1 
#a
SELECT Kunde.KundeNr, Forsikring.RegNr FROM Kunde, Forskikring 
WHERE ForsType = Kasko AND KmPrAaar > 20000
ORDER BY Kunde.KundeNr; 

#b 
SELECT ForsType AS ForsikringsType, COUNT(*) AS Antall
FROM Forsikring
GROUP BY ForsTYpe; 

#c 
SELECT ForsNr, COUNT(*) 
FROM Forsikring, Skadesak 
WHERE Forsikring.ForsNr = Skadesak.ForsNr 
GROUP BY Forsikring.ForsNr; 

#d
CREATE TABLE Forsikring{
    ForsNr INTEGER NOT NULL, 
    KundeNr INTEGER NOT NULL, 
    RegNr VARCHAR(7) NOT NULL, 
    RegAar INTEGER NOT NUll, 
    KmPrAar INTEGER NOT NULL, 
    ForsType VARCHAR(20) NOT NULL, 
    Bonus INTEGER NOT NULL, 
    AarsPremie INTEGER NOT NULL, 
    PRIMARY KEY (ForsNr)
    CONSTRAINT Forsikring_FK FOREIGN KEY (KundeNr)
    REFRENCES Kunde(KundeNr) 
}; 

#e
#Antar at SaksNr blir automatisk laget når man registrerer en ny sak ved hjelp av AUTO_INCREMENT
INSERT INTO Skadesak 
VALUES (2, CURDATE(), 'Kollisjon'); 

#f 
SELECT Skadesak.*, Kunde.*, Forsikring.ForsType, Forsikring.Bonus  
FROM Kunde, Forsikring, Skadesak 
WHERE Kunde.Knr = Forsikring.KNr AND Forsikring.ForsNr = Skadesak.ForsNr
AND YEAR(Skadesak.RegDato) = YEAR(CURDATE)-1; 

#g
SELECT Skadesak.KundeNr FROM Skadesak, Forsikring
WHERE Skadesak.ForsNr = Forsikring.ForsNr 
AND Skadesak.Skadetype = 'Tyveri' AND Forsikring.ForsType = 'Kasko';