#YH Grundläggande Python Vecka 4 labbar
#Funktioner är ABSTRAKTIONER, en black box. Man stoppar in saker och saker ploppar ut
#input() is a black box!!

# def addTwoString(str1, str2):
#     return str1 + str2

# s1 = input("Input first string: ")
# s2 = input("Input second string: ")
# print(f"Plussar: {addTwoString(s1,s2)}")

# def beräknaMoms(pris):
#     momssats = float(input("Mata in moms (6%, 12% eller 25%): "))
#     if momssats != 1.06 and momssats != 1.12 and momssats != 1.25:
#         while momssats != 1.06 and momssats != 1.12 and momssats != 1.25:
#             print("Ange antingen 1.06, 1.12 eller 1.25: ")
#             momssats = float(input("Mata in moms (6%, 12% eller 25%): "))
    
#     prisMedMoms = pris * momssats
#     print(f"Pris med moms: {prisMedMoms}kr")
#     return prisMedMoms - pris

# prisUtanMoms = float(input("Skriv in pris utan moms: "))
# print(f"Momsen är {beräknaMoms(prisUtanMoms)}kr")

# def isMyndig(age):
#     # if age >= 18:
#     #     return True
#     # else:
#     #     return False
#     return age >= 18

# age = int(input("Ange ålder: "))
# myndig = isMyndig(age)
# if myndig:
#     print("Du är myndig")
# else:
#     print("Du är ej myndig")

# print("\n*HITTA LÄNGSTA ORDET*")
# def HittaLangstaOrdet(inputList):
#     longestSoFar = inputList[0]
#     for x in inputList:
#         if len(x) > len(longestSoFar):
#             longestSoFar = x
#     return longestSoFar

# ordlista = []
# print("Skriv in tre ord")
# for i in range(0,3):
#     ordlista.append(input(f"Ord #{i+1}: "))
# print(f"Längsta ordet är: {HittaLangstaOrdet(ordlista)}")

# print("\n*RÄKNA UT TAX")
# def CalculateTaxesOnSalary(salary):
#     if salary >= 30000:
#         return salary * 0.33
#     elif salary < 30000 and salary >= 15000:
#         return salary * 0.28
#     else:
#         return salary * 0.12

# salary = float(input("Skriv in månadslön: "))
# print(f"Din skattesats är: {CalculateTaxesOnSalary(salary)}")

# print("\n*TILL PROCENT")
# def ToPercentage(dec):
#     dec = str(dec)
#     if dec == "0":
#         return "0%"
#     elif dec == "1":
#         return "100%"
    
#     if dec[2] == "0":
#         return f"{dec[3]}%"
#     elif dec[2] == "0" and len(dec) > 3:
#         return f"{dec[3]}.{dec[3::]}%"
#     else:
#         if len(dec) == 3:
#             return f"{dec[2]}0%"
#         elif len(dec) == 4:
#             return f"{dec[2::]}%"
#         else:
#             return f"{dec[2:4]}.{dec[4::]}%"

# decimal = input("Skriv in ett decimaltal mellan 0 och 1: ")
# print(f"I decimalform: {ToPercentage(decimal)}")

# print("\n*KOLLA VOKAL")
# def isVowel(input):
#     input = input.lower()
#     if input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u' or input == 'y' or input == 'å' or input == 'ä' or input == 'ö':
#         return True
#     else:
#         return False

# maybeVowel = input("Mata in en bokstav: ")
# if isVowel(maybeVowel):
#     print(f"{maybeVowel} är en vokal!")
# else:
#     print(f"{maybeVowel} är ej en vokal")

# print("\n*RÖVARSPRÅK!")
# def Translate(inputText):
#     rövartext = ""
#     for letter in inputText:
#         if not isVowel(letter) and letter != ' ':
#             rövartext = rövartext + letter + "o" + letter.lower()
#         else:
#             rövartext = rövartext + letter
#     return rövartext

# text = input("Skriv in en mening: ")
# print(f"Din mening i Rövarspråk: {Translate(text)}")

#FILES

# print("\nPRINT ODD LINES IN A FILE")
# def printOddLines(txtFile):
#     oddLine = True
#     with open(txtFile, "r") as f: 
#         for line in f:
#             if oddLine:
#                 print(line.replace("\n", ""))
#             oddLine = not oddLine

# def countLines(txtFile):
#     counter = 0
#     with open (txtFile, "r") as f:
#         for line in f:
#             counter += 1
#     return counter

# print(f"Our text file text.txt has {countLines('text.txt')} lines. Printing odd ones:")
# printOddLines("text.txt")

# print("\nMERGE TWO FILES INTO A THIRD FILE")
# def mergeTwoFiles(txt1, txt2, txtresult):
#     #if txtresult:
#     #    del txtresult
#     #No need to do this since we used write mode. It overwrites anything that is already in
#     #the result file. If we want to add something in a file we use append mode
    
#     with open (txtresult, "w") as resultFile:
#         with open (txt1, "r") as f1:
#             for line in f1:
#                 resultFile.write(line.replace("\n", "") + "\n")
#         with open (txt2, "r") as f2:
#             for line in f2:
#                 resultFile.write(line.replace("\n", "") + "\n")

# print(f"Merging txt1.txt and txt2.txt into txtResult.txt...")
# mergeTwoFiles("txt1.txt", "txt2.txt", "txtResult.txt")

# print("\nINSERT LINE NUMBERS INTO NEW FILE")
# def insertLineNumbers(txtFile, txtresult):
#     counter = 1
#     with open(txtresult, "w") as resultFile:
#         with open(txtFile, "r") as f:
#             for line in f:
#                 resultFile.write(str(counter) + " " + line.replace("\n", "") + "\n")
#                 counter += 1

# print("Taking text.txt, inserting line numbers and putting result into txtResult.txt...")
# insertLineNumbers("text.txt", "txtResult.txt")

print("\nSORT A LIST OF 800 BIRDS")
def sortNames(txtNames, txtSorted):
    names = []
    with open(txtSorted, "w") as resultFile:
        with open(txtNames, "r") as f:
            for line in f:
                names.append(line.replace("\n", "").capitalize())
        #names = sorted(names) #Puts the result in a new list
        names.sort() 
        for index in range(0, len(names)):
            resultFile.write(names[index] + "\n")

print("Sorting bird text document and putting result in sortedBirds.txt...")
sortNames("Lab5TextFile-InData1.txt", "birdsSorted.txt")

# print("\nMENU WITH USERNAMES AND PASSWORDS")
# def printMenu():
#     print("a. Login")
#     print("b. Registrera nytt konto")
#     print("c. Avsluta")

# def getMenuInput(prompt: str) -> str:
#     while True:
#         try:
#             sel = input(prompt)
#             if sel != 'a' and sel != 'b' and sel != 'c':
#                 print("Skriv in a, b eller c, tack")
#             else:
#                 break
#         except:
#             print("Skriv in en bokstav, tack")
#     return sel

# #str = 'Västerås'
# #print(str.find('g'))
# # if user.find(',') != -1: #If user contains ','
# # print("Username cannot contain ','")
# from dataclasses import dataclass
# import jsonpickle

# @dataclass
# class Account:
#     Username: str
#     Password: str

# def createAccount(allAccounts: str, accountsList: list[Account]):
#     while True:
#         try:
#             taken = False
#             user = input("Skriv in username: ")
#             for i in range(0, len(accountsList)):
#                 if accountsList[i].Username == user:
#                     taken = True
#             if len(user) < 2 or len(user) > 20:
#                 print("Please write a username within 2 and 20 characters")
#             elif taken:
#                 print("Username already taken")
#             else:
#                 break
#         except:
#             print("Ogiltig input. Försök igen")
#     while True:
#         try:
#             pw = input("Skriv in lösenord: ")
#             if len(pw) < 4 or len(pw) > 20:
#                 print("Please write a username within 4 and 20 characters")
#             else:
#                 break
#         except:
#             print("Ogiltig input. Försök igen")
    
#     acc = Account(user, pw)
#     return acc

# def login(allAccounts: str, accountsList: list[Account]) -> bool:
#     foundUser = False
#     foundPw = False
#     user = input("Skriv in username: ")
#     pw = input("Skriv in lösenord: ")
#     for i in range(0, len(accountsList)):
#         if accountsList[i].Username == user:
#             foundUser = True
#         if accountsList[i].Password == pw:
#             foundPw = True
#     if foundUser == True and foundPw == True:
#         return True
#     return False

# accounts = "allAccounts.txt"
# accountsList = []
# with open(accounts, "r") as f:
#     accountsList = jsonpickle.decode(f.read())
# print(accountsList)

# while True:
#     printMenu()
#     val = getMenuInput("Val: ")
#     if val == 'a':  
#         if(login(accounts, accountsList)):
#             print("Login successful!")
#         else:
#             print("Wrong username or password. Try again")
#     elif val == 'b':
#         accountsList.append(createAccount(accounts, accountsList))
#         with open(accounts, "w") as f:
#             f.write(jsonpickle.encode(accountsList))
#     elif val == 'c':
#         break

#LECTURE
# def GetIntMenuInput(prompt, minValue, maxValue): #Use in Bankomat!
#     while True:
#         try: #Don't question this for now
#             sel = int(input(prompt))
#             if sel < minValue or sel > maxValue:
#                 print(f"Mata in ett tal mellan {minValue} och {maxValue} tack") #Putting this in a while True works even
#                 #better than my if while loop
#             else:
#                 break
#         except: #"Don't go to exception and crash, do this instead" "Custom exception"
#             print(f"Mata in ett tal, tack")
#     return sel

# #STACK/HEAP DEMO
# # def addTo(x):
# #     x = x + 1
# #     print(x)

# # x = 12
# # addTo(x)
# # print(x)

# #FILES DEMO
# #Read mode
# # with open("spelare.txt", "r") as f: #r for read, f is an optional name
# #     for line in f:
# #         #lista.append(line.replace("\n",""))
# #         pass

# # #Write mode
# # with open('spelare.txt', "w") as f:
# #     #for namn in lista:
# #     #    f.write(namn + "\n")
# #     pass

# #INTRO TO OBJECT ORIENTATION
# #Spelare ska ha namn, JerseyNr och Team name
# from dataclasses import dataclass

# import jsonpickle

# @dataclass
# class Player:
#     Namn: str
#     JerseyNumber: int
#     Teamname: str

# # p2 = Player("Mats Sundin", 13, "Toronto")
# # p2.Teamname
# # l = []
# # l.append(p1)
# # .Teamname = "Tre Kronor"
# # print(p1.Namn)
# # print(p2.Namn)


# def GetIntMenuInput(prompt, minValue, maxValue):
#     while True:
#         try:
#             sel = int(input(prompt))
#             if sel < minValue or sel > maxValue:
#                 print(f"Mata in ett tal mellan {minValue} och {maxValue} tack")
#             else:
#                 break
#         except:
#             print("Mata in ett tal tack")
#     return sel

# def CreatePlayer(): # black box - kommer ut ut den så ska vi ha en ny player (namn - string)
#     namn = input("Ange namn:")
#     team = input("Ange lag:")
#     jersey = int(input("Ange jersey:"))
#     player = Player(namn,jersey,team) 
#     return player
    
# def ListPlayers(listOfPlayers): 
#     for player in listOfPlayers:
#         print(f"{player.JerseyNumber} {player.Namn} {player.Teamname}")

# def DeletePlayer(listOfPlayer):
#     index = 1
#     for playerName in listOfPlayer:
#         print(f"{index} {playerName}")
#         index = index + 1
#     sel = GetIntMenuInput("Ange spelare att ta bort:",1, len(listOfPlayer))
#     del listOfPlayer[sel-1]

# def ChangePlayer(listOfPlayer):
#     while True:
#         print(" *** PLAYER MENU *** ")
#         print("1. Ändra namn")
#         print("2. Ändra jersey")
#         print("3. Tillbaka till huvudmenyn")
#         sel = GetIntMenuInput("Ange val:", 1, 3)
#         if sel == 1:
#             index = 1
#             for playerName in listOfPlayer:
#                 print(f"{index} {playerName}")
#                 index = index + 1
#             sel = GetIntMenuInput("Ange spelare att ändra namn på:",1, len(listOfPlayer))

#             namn = input("Ange nytt namn")
#             listOfPlayer[sel-1] = namn
#         elif sel == 2:
#             print("To be implemented")
#         elif sel == 3:
#             return          

# def MenuPrint():
#     print("1. Skapa spelare")
#     print("2. Lista spelare")
#     print("3. Ändra spelare")
#     print("4. Ta bort spelare")
#     print("5. Avsluta")
# # ibland så returnerar INTE en funktion nånting

# def AddTwoNumbers(tal1:int, tal2:int) -> int:
#     return tal1 + tal2

# with open("spelare-objekt.txt", "r") as filen:
#     lista = jsonpickle.decode(filen.read())

# def HuvudMenyInput(lista):        
#     while True:
#         MenuPrint()
#         sel = GetIntMenuInput("Ange val:", 1, 5)
#         if sel == 1:
#             player = CreatePlayer()
#             lista.append(player)
#         if sel == 2:
#             ListPlayers(lista)
#         if sel == 4:
#             DeletePlayer(lista)
#         if sel == 3:
#             ChangePlayer(lista)
#         if sel == 5:
#             break

# lista = []
# HuvudMenyInput(lista)

# with open("spelare-objekt.txt", "w") as f:
#     f.write(jsonpickle.encode(lista))


#MONEY LAUNDRY
#We get files from Bakomat on format WITHDRAWALxxxx.txt and DEPOSITxxxx.txt
#Look for suspicious money laundring transactions

import os
path = "c:\\transactions" #We don't repeat ourselves and if the locations is changed we only change here
#Loop all files in PATH
#If deposit, print DEPOSIT
#If withdrawal, print WITHDRAWAL
listOfFileNames = os.listdir(path)
depCount = 0
witCount = 0
for fileName in listOfFileNames:
    if fileName.lower().startswith('deposit'):
        print("DEPOSIT")
        depCount += 1
    elif fileName.lower().startswith('withdrawal'):
        print("WITHDRAWAL")
        witCount += 1
    os.remove(path + "\\" + fileName)

print(f"Antal deposits: {depCount} Antal withdrawals: {witCount}")

print("\n***LOOK FOR FILES***")
import os

def searchInDir(filesList:list[str], searchterm: str) -> list[str]:
    result = []
    for fileName in filesList:
        if fileName.find(searchterm) != -1:
            result.append(fileName)
    return result

while True:
    try:
        path = input("Ange path ->.")
        listOfFileNames = os.listdir(path)
        searching = input("Ange del av filnamn ->.")
        relevantFiles = searchInDir(listOfFileNames, searching)
        for file in relevantFiles:
            info = os.stat(path + "\\" + file)
            bytesize = info[6]
            print(f"{file} - bytes = {bytesize}")
    except:
        print("Invalid input. Try again")

#FUNCTIONS #2
def getAllOlympicGameYears(startYear:int, endYear:int = 2022) -> list[int]: #SINGLE SOURCE OF TRUTH
    years = []
    for x in range(startYear,endYear+1,4):
        years.append(x)
    return years

start = int(input("Start year: "))
end = int(input("End year: "))
ol = getAllOlympicGameYears(start, end)
for year in ol:
    print(year)