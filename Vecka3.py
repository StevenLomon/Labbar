#YH Grundläggande Python Vecka 3 labbar

#DICTIONARIES

#print("\nCHECK IF KEY IS PRESENT IN DICT")
# def isPresentKey(dict, key):
#     if key in dict:
#         return True
#     else:
#         return False

# d = {1: 15, 6: 18, 9: 22}
# print(f"d = {d}")
# keyCheck = int(input("Enter a key to be checked: "))
# if isPresentKey(d,keyCheck):
#     print(f"For {keyCheck} in d: Key is present in the dictionary")
# else:
#     print(f"For {keyCheck} in d: Key is not present in the dictionary")

# print("\nGET UNIQUE VALUES FROM A DICT")
# def dictUniqueValues(dict):
#     uniqueVal = {}
#     for val in dict.values():
#         if not val in uniqueVal:
#             uniqueVal[val] = 1
#     return uniqueVal

# s =  {"V":"S001", "V":"S002", "VI":"S001", "VI":"S005", "VII":"S005", "V":"S009", "VIII":"S007"}
# print(f"Unique values in s = {s}:")
# for key in dictUniqueValues(s).keys():
#     print(key)

print("\nCOUNT LETTER OCCURENCE IN A STRING")
def stringCountLetters(string):
    letters = {} #maps letter to amount of times in string: letter - amount
    for letter in string.lower():
        if not letter in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters

theString = 'Steven Lomon Lennartsson'
print(f"String to count letter occurence: {theString}")
print(f"Result: {stringCountLetters(theString)}")


print("\nGET TOP THREE ITEMS FROM A DICT")
def dictGetTopThree(dict):
    itemShopCopy = dict.copy() #Copy the original dict since we will be removing
    theTopThree = {}
    largestSoFar = 0
    currentKey = ''
    while len(theTopThree) < 3:
        for key in itemShopCopy.keys(): #find the largest in the dict
            if itemShopCopy[key] > largestSoFar:
                largestSoFar = itemShopCopy[key]
                currentKey = key
        theTopThree[currentKey] = largestSoFar #"Transfer" the item
        largestSoFar = 0 #Reset largestSoFar
        itemShopCopy.pop(currentKey) #Delete from the copy dict
    return theTopThree

sample = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print(f"Our item shop: {sample}")
print(f"Top three items in shop: {dictGetTopThree(sample)}")
print(f"Our item shop: {sample}")

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