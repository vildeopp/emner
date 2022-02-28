#Oppgave 1
#a) 
SELECT COUNT(*) FROM Codons; 
#b) 
SELECT * FROM `Amino_acid_properties` WHERE Polarity = 'Polar' AND Molecular_mass > 150; 
#c) 
SELECT * FROM `Nucleotides` WHERE Type = 'Purine' ORDER BY Symbol;
#d) 
SELECT Codon_sequence  FROM `Codons` WHERE Position2 LIKE Position3;
#e) 
SELECT Codon_sequence, Amino_acid_id FROM Codons GROUP BY Amino_acid_id HAVING COUNT(Amino_acid_id) = 1; 


#Oppgave2 
#a) 
CREATE TABLE Amino_acid_nomenclature(
    AminoId VARCHAR(10), 
    Symbol CHAR, 
    Name VARCHAR(30), 
    Code VARCHAR(10), 
    CONSTRAINT Amino_acid_nomenclaturePN PRIMARY KEY(aminoId),
    CONSTRAINT Amino_acid_nomenclatureFN FOREIGN KEY(Name) REFERENCES Amino_acid_properties(Name)
    ); 

#b) 

INSERT INTO Amino_acid_nomenclature (Amino_id, Symbol, Name, Code) 
VALUES ('a1', 'A', 'Alanine','Ala'),
('a2', 'C', 'Cysteine', 'Cys'), 
('a3', 'D', 'Aspartic acid', 'Asp'), 
('a4', 'E', 'Glutamic acid', 'Glu'), 
('a5', 'F', 'Phenylalanine', 'Phe'), 
('a6', 'G', 'Glycine', 'Gly'), 
('a7', 'H', 'Histidine', 'His'), 
('a8', 'I', 'Isoleucine', 'Ile'), 
('a9', 'K', 'Lysine', 'Lys'), 
('a10', 'L', 'Leucine', 'Leu'), 
('a11', 'M', 'Methionine', 'Met'), 
('a12', 'N', 'Asparagine', 'Asn'), 
('a13', 'P', 'Proline', 'Pro'), 
('a14', 'Q', 'Glutamine', 'Gln'), 
('a15', 'R', 'Arginine', 'Arg'), 
('a16', 'S', 'Serine', 'Ser'), 
('a17', 'T', 'Threonine', 'Thr'), 
('a18', 'V', 'Valine', 'Val'), 
('a19', 'W', 'Tryptophan', 'Trp'), 
('a20', 'Y', 'Tyrosine', 'Tyr'), 
('a21', null, null, 'Stop'), 
('a22', null, null, 'Stop'), 
('a23', null, null, 'Stop'), 

#c) i 
ALTER TABLE Amino_acid_properties ADD CONSTRAINT 
rule_Mass CHECK (Molecular_mass>70 AND 210<Molecular_mass); 
# ii 
ALTER TABLE Amino_acid_properties ADD CONSTRAINT 
rule_uncharged CHECK(Charge IN ('uncharged', 'positive', 'negative'); 

#d)
ALTER TABLE Codons ADD CONSTRAINT Amino_acid_idFN 
FOREIGN KEY (Amino_acid_id) REFERENCES Amino_acid_nomenclature(Amino_Id); 

#Oppgave3
#a) 
SELECT * FROM Codons WHERE Amino_acid_id IN ('a21', 'a22', 'a23');
#b)
SELECT Codon_sequence FROM `Codons` WHERE Position1 LIKE 'C';
#c)
SELECT Codon_sequence FROM Amino_acid_properties INNER JOIN Amino_acid_nomenclature 
INNER JOIN Codons ORDER BY Molecular_mass; 
#d) 
SELECT COUNT(A.Name) 
FROM Amino_acid_properties AS A INNER JOIN Amino_acid_nomenclature AS B ON A.Name = B.Name
INNER JOIN Codons AS C ON B.Amino_id = C.Amino_acid_id
WHERE A.Charge = 'uncharged' AND C.Codon_sequence LIKE '%A'
#e) 
SELECT C.Codon_sequence, A.Name            
FROM Amino_acid_properties AS A INNER JOIN Amino_acid_nomenclature AS B ON A.Name = B.Name
INNER JOIN Codons AS C ON B.Amino_id = C.Amino_acid_id
WHERE A.Charge = 'uncharged' AND A.Molecular_mass BETWEEN 130 AND 150;

#Oppgave4
#a) 
#Siden det bare er to typer av Nucleotides kan man bare gruppere 
#tabellen etter type og så telle størrelsen på gruppene
SELECT Type, COUNT(*) FROM Nucleotides GROUP BY Type; 
#b) 
SELECT B.Symbol, A.Codon_sequence
FROM Codons AS A INNER JOIN Amino_acid_nomenclature AS B ON A.Amino_acid_id = B.Amino_id
WHERE A.Position1 = A.Position2 AND A.Position2 = A.Position3 
ORDER BY B.Name
#c) 
SELECT C.Codon_sequence
FROM Amino_acid_properties AS A INNER JOIN Amino_acid_nomenclature AS B ON A.Name = B.Name 
INNER JOIN Codons AS C ON B.Amino_id = C.Amino_acid_id 
INNER JOIN Nucleotides AS D ON C.Position1 = D.Symbol 
WHERE (D.Type = 'Purine' AND A.Polarity = 'Polar' AND B.Name = '%ine')
#d) 
SELECT A.Polarity, COUNT(C.Codon_sequence)
FROM Amino_acid_properties AS A INNER JOIN Amino_acid_nomenclature AS B ON A.Name = B.Name 
INNER JOIN Codons AS C ON B.Amino_id = C.Amino_acid_id 
GROUP BY A.Polarity
#e) 
SELECT A.Polarity, COUNT(C.Codon_sequence) AS 'Number of Codons', A.Charge
FROM Amino_acid_properties AS A INNER JOIN Amino_acid_nomenclature AS B ON A.Name = B.Name 
INNER JOIN Codons AS C ON B.Amino_id = C.Amino_acid_id 
GROUP BY A.Polarity, A.Charge





