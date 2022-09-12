#YH Grundläggande Python Vecka 2 labbar
#while True: infinite loop with a break is suuuuper common
#can use pass as a temporary placeholder!
from dataclasses import replace
import random
import time
import termcolor

#LOOPAR
# for i in range(11):
#     print(i)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# tal1 = int(input("Skriv in tal#1: "))
# tal2 = int(input("Skriv in tal#2: "))
# for i in range(tal1, tal2+1): #Range won't include the upper limit by default
#     print(i)

# while tal1<=tal2:
#     print(tal1)
#     tal1 += 1

# JN = "J"
# while JN == "J": #ALSO A VIABLE OPTION FOR A MENU
#     tal1 = int(input("Skriv in tal#1: "))
#     tal2 = int(input("Skriv in tal#2: "))
#     print(f"Summa: {tal1+tal2}")
#     JN = input("Vill du fortsätta(J/N)? ").capitalize()
#     if JN == "N":
#         break

# b = int(input("Mata in ett tal: "))
# sum = 0
# for i in range(11):
#     b += b
# print(f"Summar av det du matat in är: {b}")

# c = int(input("Mata in ett tal: "))
# for i in range(c):
#     print(i)

# while True:
#     print("Rolling the dices...")
#     time.sleep(1)
#     print("The values are...")
#     time.sleep(2)
#     print(f"{random.randint(1,6)} and {random.randint(1,6)}!\n")
#     again = input("Roll the dices again? ").lower()
#     if again != "y" and again != "yes": #and eftersom att vi har negation
#         break

#LISTS
# numbers = []
# for x in range(0,4):
#     numbers.append(int(input(f"Mata in tal#{x+1}: ")))
# print(numbers)
# numbers.sort()
# print(f"Största numret är {numbers[-1]}") #list[-1] is SUPER USEFUL!!

# def listSum(list):
#     sum = 0
#     for x in list:
#         sum += x
#     return sum

# print(f"Summan av alla tal är {listSum(numbers)}")

# def listLargest(list): #I will most probably use this in the future
#     list.sort()
#     return list[-1]

# def listLen2(list):
#     counter = 0
#     for x in range(len(list)):
#         if len(list[x]) >= 2 and list[x][0] != list[x][-1]: #REMEMBER THIS!!!
#             counter += 1
#     return counter

# sample = ['abc', 'xyz', 'aba', '1221']
# print(listLen2(sample))

# def listRemoveDup(inputlist):
#     return list(dict.fromkeys(inputlist)) #Finns supersmidigt från w3schools

# chars = ["a", "b", "a", "c", "c"]
# print(f"Before: {chars}")
# chars_update = listRemoveDup(chars)
# print(f"After: {chars_update}")

# def listWordLongerN(list, n):
#     wordsLonger = []
#     for x in list:
#         if len(x) > n:
#             wordsLonger.append(x)
#     return wordsLonger

# words = ["monke", "Python", "hi", "USA", "Bruce Willis", "water"]
# print(listWordLongerN(words, 4))

board = []
for i in range(8):
    row = [f"{[i]}{[j]}" for j in range(8)] #This is the same as having two nested for loops
    board.append(row)

print(f"{board}\n")
board[1:8] = ["   b","  b","  b","  b","  b","  b","  b"]
#board[6:13] = ["  b"," b"," b"," b"," b"," b"," b"]
print(board)

#STRINGS
# a = input("Mata in sträng #1: ")
# b = input("Mata in sträng #2: ")
# c = input("Mata in sträng #3: ")
# print(a+b+c)

# hello = "Hello, world"
# def findPosition(word, letter):
#     letterPos = word.find(letter)
#     return letterPos

# print(f"Hello = {hello}")
# print(f"w is at position {findPosition(hello, 'w')}")

# namn = "kurt andersson"
# def capitalizeNames(full_name):
#     capitalized_name = ""
#     firstLetter = True
#     prevLetter = ""
#     #full_name[0] = full_name[0].upper()
#     #space_pos = full_name.find(" ")
#     for letter in full_name:
#         if firstLetter == True or prevLetter == " ":
#             capitalized_name = capitalized_name + letter.upper()
#         else:
#             capitalized_name = capitalized_name + letter
#         prevLetter = letter
#         firstLetter = False
#         # if letter == " ":
#         #     full_name[letter + 1] = full_name[letter + 1].upper()
#     # full_name_split = full_name.split()
#     # for name in full_name_split:
#     #     name = name.capitalize()
#     return capitalized_name

#namn = input("Mata in namn: ")
# def capitalizeNames(full_name):
#     name_split = full_name.split()
#     result = ""
#     for name in name_split:
#         name = name.capitalize()
#         result = result + name + " "
    
#     print(result)
#     #Count and remove all but the last space
#     space_count = result.count(" ")
#     result = result.replace(" ", "", space_count-1)
#     return result

# namn = "steven"
# namn = namn.capitalize()
# print(namn)

# #steven lomon lennartsson
# namn = input("Mata in namn: ")
# def capitalizeNames(full_name):
#     name_split = full_name.split()
#     for index in range(len(name_split)):
#         name_split[index] = name_split[index].capitalize()
#     result = ' '.join(name_split)
#     return result

# print(f"Before: {namn}")
# namn_capitalized = capitalizeNames(namn)
# print(f"After: {namn_capitalized}")

# text = "Detta är en sträng som du skall ändra"
# spaceCounter = text.count(" ")
# # for s in text:
# #     if s == " ":
# #         spaceCounter += 1
# text_space_replaced = text.replace(" ", "*")

# print(f"Before: {text}")
# print(f"After: {text_space_replaced}")
# print(f"There were {spaceCounter} spaces replaced")

# mail = input("Mata in en mailadress: ")
# def mailControl(input_mail):
#     length = len(input_mail) - 1
#     atCounter = input_mail.count("@")
#     lastDotPosition = input_mail.rfind(".")
#     dotBool = False
#     if length - lastDotPosition == 2 or length - lastDotPosition == 3:
#         dotBool = True
#     if atCounter == 1 and dotBool:
#         return True
#     else:
#         return False

# if mailControl(mail):
#     print("Du har matat in en giltig e-mail")
# else:
#     print("Du har matat in en ogiltig e-mail")

# text = "Detta är min text som jag matar in"
# #text = input("Mata in en text: ")
# def countWords(text):
#     text_split = text.split()
#     return len(text_split) #return size of the list

# print(f"Texten innehåller {countWords(text)} ord")

# maybePalindrome = input("Mata in text för att checka palindrom: ")
# def isPalindrome(input):
#     input_spaces_removed = input.replace(" ", "")
#     indexLength = len(input_spaces_removed) - 1
#     input_reversed = ""
#     for index in range(indexLength,-1,-1):
#         input_reversed = input_reversed + input_spaces_removed[index]
#     if input_reversed == input_spaces_removed:
#         return True
#     else:
#         return False

# if isPalindrome(maybePalindrome):
#     print(f"{maybePalindrome} is a palindrome!")
# if not isPalindrome(maybePalindrome):
#     print(f"{maybePalindrome} is a not palindrome")

#LECTURE
# while True: #THIS IS A SUPER USEFUL INFINITE LOOP, WILL BE USED A LOT!!
#     print("Spelet spelas")
#     inmatning = input("Vill du spela igen Ja/Nej? ").lower()
#     if inmatning == "nej":
#         break
#     print("Vi avslutar...")

# while True:
#     inmatning = input(":")
#     #if inmatning.find("jäkla") != -1: #THIS LINE IS NOT USED ANYMORE
#         #if we can't find the position of a char, the position is -1
#     inmatning = inmatning.replace("jäkla", "*****")
#     print(inmatning)

# namn = "Steven Lomon Lennartsson"
# length = len(namn)
# for index in range(length):
#     print(namn[index])

# print(namn[-1])

# allAccounts = ["1212", "3311", "9999"]
# while True:
#     print("1. Lista alla konton")
#     print("2. Skriv ut hur många konton")
#     print("3. Lägg till konton")
#     print("4. Ta bort konton")
#     print("5. Söka")
#     action = input("Ange val:")
#     if action == "2":
#         print(f"Antal konton:{len(allAccounts)}")
#     elif action == "1":
#         for namn in allAccounts:
#             print(namn)
#     elif action == "3":
#         namn = input("Ange namn på nya kontot")
#         allAccounts.append(namn)
#     elif action == "4":
#         for index in range(0,len(allAccounts)):
#             print(f"{index+1} {allAccounts[index]}")
        
#         index = input("Ange kontonummer på kontot som ska tas bort: ")
#         index = index = index - 1
#         del allAccounts[index]
#     elif action == "5":
#         searchQuery = input("Sök efter:").lower()
#         for namn in allAccounts:
#             lowerCaseNamn = namn.lower()
#             index = lowerCaseNamn.find(searchQuery)
#             if index != -1:
#                 print(namn)