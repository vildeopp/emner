navn = str(input("Navn: "))
adresse = str(input("Adresse: "))
post = str(input("PostSted/Nummer: "))

longest = max(navn, adresse, post, key = len)
print(longest)



if len(navn) > len(adresse) and (len(navn) > len(post)):
    print(navn)
elif len(adresse) > len(navn) and len(adresse) > len(post): 
    print(adresse)
elif len(post) > len(navn) and len(post) > len(adresse): 
    print(post)
else: 
     print(max(navn, adresse, post, key = len))