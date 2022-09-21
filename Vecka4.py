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

print("\n*KOLLA VOKAL")
def isVowel(input):
    input = input.lower()
    if input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u' or input == 'y' or input == 'å' or input == 'ä' or input == 'ö':
        return True
    else:
        return False

maybeVowel = input("Mata in en bokstav: ")
if isVowel(maybeVowel):
    print(f"{maybeVowel} är en vokal!")
else:
    print(f"{maybeVowel} är ej en vokal")

print("\n*RÖVARSPRÅK!")
def Translate(inputText):
    rövartext = ""
    for letter in inputText:
        if not isVowel(letter) and letter != ' ':
            rövartext = rövartext + letter + "o" + letter.lower()
        else:
            rövartext = rövartext + letter
    return rövartext

text = input("Skriv in en mening: ")
print(f"Din mening i Rövarspråk: {Translate(text)}")


#LECTURE
def GetIntMenuInput(prompt, minValue, maxValue): #Use in Bankomat!
    while True:
        try: #Don't question this for now
            sel = int(input(prompt))
            if sel < minValue or sel > maxValue:
                print(f"Mata in ett tal mellan {minValue} och {maxValue} tack") #Putting this in a while True works even
                #better than my if while loop
            else:
                break
        except: #"Don't go to exception and crash, do this instead" "Custom exception"
            print(f"Mata in ett tal, tack")
    return sel

#STACK/HEAP DEMO
# def addTo(x):
#     x = x + 1
#     print(x)

# x = 12
# addTo(x)
# print(x)

#FILES DEMO
#Read mode
with open("spelare.txt", "r") as f: #r for read, f is an optional name
    for line in f:
        #lista.append(line.replace("\n",""))
        pass

#Write mode
with open('spelare.txt', "w") as f:
    #for namn in lista:
    #    f.write(namn + "\n")
    pass
