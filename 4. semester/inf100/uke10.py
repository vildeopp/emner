#oppgave 1 

def open_file(filename): 
    s = " "
    with open(filename, encoding= "utf8") as file: 
        for line in file: 
            s = s + line
            s = s.strip("\n")
    
    return s

#print(open_file("askeladden.txt"))

#oppgave 2 

def open_file2(filename): 
    s = " "
    with open(filename, encoding= "utf8") as file: 
        for line in file: 
            line = line.strip("\n")
            s = s + ">>>" + line + "<<<" + "\n"

    return s

#print(open_file2("askeladden.txt"))

#Oppgave 3 

def open_file3(filename): 
    s = ""
    c = 0
    with open(filename, encoding="utf8") as file:
        for line in file: 
            c += 1 
            words = line.split()
            lastword = words[-1]
            s = s + lastword[0]
    return s

#print(open_file3("askeladden.txt"))

#Oppgave 4 

def r_w_file(infile, outfile): 
    rFile = open(infile, "r", encoding="utf8")
    wFile = open(outfile, "w", encoding="utf8")

    for line in rFile: 
        if "lame" in line: 
            wFile.write(line)
    

#r_w_file("in.txt", "out.txt")

#Oppgave5 

def first_letters(filename): 
    try: 
        return open_file3(filename)
    except FileNotFoundError: 
        return ""

#Oppgave 6 

def dot_product(a, b):
    try:
        sum = 0
        for i in range(len(a)): 
            sum += a[i]*b[i]
        return sum
    
    except: 
        if len(a) != len(b): 
            raise ValueError("Listene er ikke like lange")
       

a = [1, 2, 3]
b = [4, 5]

print(dot_product(a, b))

#Oppgave 7

def add_together_safely(a, b, c, d): 
    try: 
        return a + b + c + d 
    except Exception as e: 
        return "Failed with error: " + str(e)

#print(add_together_safely('a', 'b', 1, 2))

#Oppgave 8

def my_get(key, value, dict): 
    try: 
        if key in dict.keys(): 
            return dict[key]
    except: 
        if key not in dict.keys(): 
            return value

#Oppgave 9 

def rename_from_datafile(filename): 
    
    with open(filename, encoding= "utf8") as file: 
        place = file.readline().strip("\n")
        date = file.readline().strip("\n")

        format = date + "_" + place + ".txt"

        with open(format, "w", encoding="utf8") as newFile: 
            newFile.writelines(file.readlines())
    
    return format

#print(rename_from_datafile("qwerty.txt"))

def rename_all(nameList): 
    for i in range(len(nameList)): 
        nameList[i] = rename_from_datafile(nameList[i])
    

#Oppgave 10 

def changeLineToTupple(line): 
    return tuple(line.split())

def readFile(filename):
    l = []
    with open(filename, encoding= "utf8") as file: 
        for line in file: 
            l.append(changeLineToTupple(line))
    
    return l

def avarage(data, month = None): 
    try: 
        sum = 0
        for d in data: 
            sum += d[-1]
        return sum/len(data)
    except: 
        if month != None: 
            sum = 0
            n = 0
            for d in data:
                if d[1] == int(month): 
                    n += 1 
                    sum = sum + d[-1]  

            return sum/n


def changeTuple(tuple, day): 
    l = list(tuple)
    l.append(day)
    return l

def addWeekday(data): 
    days = ("Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri")   
    hour = 0
    num = 0
    currWeekday = days[num]
    for d in data: 
        tuple(changeTuple(data, currWeekday))
        hour = data[3]

        if hour == "24": 
            num += 1
        if num == 6: 
            num = 0 

data = readFile("VIK_sealevel_2000.txt")

addWeekday(data)

print(data)
               







    

 





        
            


