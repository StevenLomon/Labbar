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

def myndigEllerEj(ålder):
    if ålder >= 18:
        return "Du är myndig"
    else:
        return "Du är ej myndig"

age = int(input("Ange ålder: "))
print(myndigEllerEj(age))

def isVowel(input):
    input = input.lower()
    if input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u':
        return True
    else:
        return False

maybeVowel = input("Mata in en bokstav: ")
if isVowel(maybeVowel):
    print(f"{maybeVowel} är en vokal!")
else:
    print(f"{maybeVowel} är ej en vokal")