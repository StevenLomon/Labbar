#YH Grundläggande Python Vecka 2 labbar
#while not finished
import random
import time
from tkinter import Y

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
numbers = []
numbers.append(int(input("Mata in tal#1: ")))
numbers.append(int(input("Mata in tal#2: ")))
numbers.append(int(input("Mata in tal#3: ")))
numbers.append(int(input("Mata in tal#4: ")))
print(numbers)
numbers.sort()
print(f"Största numret är {numbers[-1]}") #list[-1] is SUPER USEFUL!!

def listSum(list):
    sum = 0
    for x in list:
        sum += x
    return sum

print(f"Summan av alla tal är {listSum(numbers)}")

def listLargest(list): #I will most probably use this in the future
    list.sort()
    return list[-1]

def listLen2(list):
    counter = 0
    for x in range(len(list)):
        if len(list[x]) >= 2 and list[x][0] != list[x][-1]: #REMEMBER THIS!!!
            counter += 1
    return counter

sample = ['abc', 'xyz', 'aba', '1221']
print(listLen2(sample))

def listRemoveDup(inputlist):
    return list(dict.fromkeys(inputlist)) #Finns supersmidigt från w3schools

chars = ["a", "b", "a", "c", "c"]
print(f"Before: {chars}")
chars_update = listRemoveDup(chars)
print(f"After: {chars_update}")

def listWordLongerN(list, n):
    