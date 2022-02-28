#Oppgave 1
names = ['Jakob', 'Emma', 'Ola', 'Sondre', 'Maia', 'Emilie', 'Noa']


newList = [[x[::-1], len(x)] for x in names]
print(newList)

#Oppgave 2
def reverse(x): 
    return x[::-1]
reversedList = map(reverse, names)

newList2 = [[x, len(x)] for x in reversedList]
print(newList2)

#Oppgave 3 
cat = ('aloof', 'meow', 'tuna')

dog = ('friendly', 'woof', 'sausage')

zipped = zip(cat, dog)

for t in zipped: 
    x = [t[0], t[1]]
    print(x)

#Oppgave 4

catList = list(cat)
catList.remove('tuna')
catList.append('laks')

cat = tuple(catList)

print(cat)

#Oppgave 5

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

while len(stack) != 0: 
    print(stack.pop())

#Oppgave 6 

inputList = []

while len(inputList) < 3: 
    i = str(input('Enter word: '))
    inputList.append(i)

vokaler = ['a', 'e', 'i', 'o', 'u', 'y']

def pigify(word): 
    if word[0] in vokaler: 
        word = word + 'way'
        
    else:
        for c in word: 
            if c in vokaler: 
                index = word.index(c)
                word = word[index: ] + word[0: index] + 'ay'
                break
    
    return word

pigLatin = map(pigify, inputList)
print(inputList)
print(list(pigLatin))

#Oppgave 7 
frukt = ['eple', 'appelsin', 'ananas', 'kokosnøtt', 'banan', 'kirsebær']

print(sorted(frukt, key = len))

#Oppagve 8 





