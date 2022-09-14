#YH Grundläggande Python Vecka 3 labbar

#DICTIONARIES
# def dictKeyCheck(dict, key):
#     if key in dict:
#         return "Key is present in the dictionary"
#     else:
#         return "Key is not present in the dictionary"

# d = {1: 15, 2: 18, 3: 22}
# print(f"For 2 in d: {dictKeyCheck(d,2)}")
# print(f"For 4 in d: {dictKeyCheck(d,4)}")

# def dictPrintUnique(dict):
#     dictValues = dict.values()
#     dictValuesNoDuplicates = list(dict.fromkeys(dictValues)) #remove duplicates
#     return dictValuesNoDuplicates

# s =  {"V":"S001", "V":"S002", "VI":"S001", "VI":"S005", "VII":"S005", "V":"S009", "VIII":"S007"}
# print(f"Unique values: {dictPrintUnique(s)}")

# def dictFromString(string):
#     listString = list(string)
#     listDict = dict.fromkeys(listString, 0)
#     for letter in listString:
#         listDict[letter] += 1
#     return listDict

# print(dictFromString('w3resource')) #Key order is different in Python 3.8

def dictGetTopThree(dict):
    keys = []
    values = []
    for key in dict:
        keys.append(key)
        values.append(dict[key])
    print(keys)
    print(values)
    indexLargest = 0


sample = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print(f"Top three items in shop: {dictGetTopThree(sample)}")

#LECTURE
# telefonregister = {}
# for i in range(0,5):
#     namnNummer = input(f"#{i+1}: Mata in förnamn och telefonnummer: ")
#     namn = namnNummer.split()[0]
#     nummer = namnNummer.split()[1]
#     telefonregister[namn] = nummer
#     #Alternative solution is to find the index of the space and take everything before it to name and everything after to nummer

# print(telefonregister)

# while True:
#     namn = input("Ange namn att kolla upp i registret: ")
#     if not namn in telefonregister:
#         print("Finns ej i registret!")
#     else:
#         print(f"{namn} har tel {telefonregister[namn]}")