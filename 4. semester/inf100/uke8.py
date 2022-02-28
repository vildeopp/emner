#Oppgave 1 

def door_open(argument): 
    open = []
    #Hvis bilen er åpen og den står i park 
    if argument[3] == '1' or argument[8] == 'P': 
        #Hvis left dashboard switch eller left outside handle eller 
        if (argument[0] == '1' or argument[5] == '1') or (argument[4] == '1' or argument[2] == '1'): 
            open.append('left')
        if( argument[1] == '1' or argument[7] == '1') or (argument[6] == '1' or argument[2] == '1'): 
            open.append('right')

    return open

print(door_open('00010010P'))
    
