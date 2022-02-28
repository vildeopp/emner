tekst = input("tekst her: ")
tall = int(input("tall her: "))

antall = tall - len(tekst) + 2

førsteDel = antall//2
sistedel = antall - førsteDel

print("*"*(tall+len(tekst)))
print("*" + " "*førsteDel + tekst  + " "*sistedel + "*")
print("*"*(tall+len(tekst)))