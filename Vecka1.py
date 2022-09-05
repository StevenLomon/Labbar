#YH Grundläggande Python Vecka 1 labbar
#ctrl k c för att multi line kommentera
#ctrl k u för att multi line un-kommentera

print("Hello! :D")

# #VARIABLER
# name = "Steven"
# age = 26
# print(f"Jag heter {name} och är {age} år")

# userName = input("Skriv in ditt förnamn: ")
# userSurname = input("Skriv in ditt efternamn: ")
# print(f"Du heter: {userSurname}, {userName}")

# #OPERATORS
# tal1 = float(input("Mata in tal 1: "))
# tal2 = float(input("Mata in tal 2: "))
# upphöjt = tal1**tal2
# gånger = tal1*tal2
# delat = tal1/tal2
# plus = tal1+tal2
# minus = tal1-tal2
# heltalsdividerat = tal1//tal2
# modulo = tal1%tal2
# print(f"tal1^tal2 = {upphöjt}")
# print(f"tal1*tal2 = {gånger}")
# print(f"tal1/tal2 = {delat}")
# print(f"tal1+tal2 = {plus}")
# print(f"tal1-tal2 = {minus}")
# print(f"tal1//tal2 = {heltalsdividerat}")
# print(f"tal1%tal2 = {modulo}")

# namn = input("Vad heter du: ")
# print(namn*5)

# print(int(input("Enter an integer: ")) >= 100)

#IF
# a = float(input("Mata in ett tal: "))
# if a > 10:
#     print("Talet är större än tio")
# else:
#     print("Talet är mindre än 10")

# milkcount = int(input("Hur många mjölk finns kvar? "))
# if milkcount < 10:
#     print("Beställ 30 paket")
# elif milkcount > 10 and milkcount < 20:
#     print("Beställ 20 paket")
# else:
#     print("Du behöver inte beställa någon mjölk")

# number1 = int(input("Mata in tal #1: "))
# number2 = int(input("Mata in tal #2: "))
# number3 = int(input("Mata in tal #3: "))
# if number1 > number2 and number1 > number3:
#     largest = number1
# elif number2 > number1 and number2 > number3:
#     largest = number2
# else:
#     largest = number3
# print(f"Det största talet är {largest}")

# anv = input("Ange kategori- vuxen, pensionär eller student: ").lower()
# if (anv != "vuxen" and anv != "pensionär" and anv != "student"):
#     while (anv != "vuxen" and anv != "pensionär" and anv != "student"):
#         print("Felaktig kategori. Försök igen")
#         anv = input("Ange kategori- vuxen, pensionär eller vuxen: ").lower()
# if anv == "vuxen":
#     print("Din resa kommer kosta 30kr")
# else:
#     print("Din resa kommer kosta 20kr")

# land = input("Mata in land du bor i: ").capitalize()
# if land == "Sverige" or land == "Danmark" or land == "Norge":
#     print("Du bor i Skandinavien")
# else:
#     print("Du bor inte i Skandinavien")

pengar = float(input("Ange hur mycket pengar du har: "))
rabbat = input("Har du rabbat? ").lower()
if rabbat == "ja":
    rabbat = True
elif rabbat == "nej":
    rabbat = False

if 15 < pengar < 25 and not rabbat: #THIS IS A HUGE W
    print("Du kan köpa hamburgare")
elif 15 < pengar < 25 and rabbat:
    print("Du kan köpa en liten hamburgare och en pommes frites")
elif 25 > pengar <= 50 and not rabbat:
    print("Du kan köpa en stor hamburgare")
elif 25 > pengar <= 50 and rabbat:
    print("Du kan köpa en stor hamburgare och pommes frites")
elif (pengar > 60 or 50 < pengar < 60) and rabbat:
    print("Du kan köpa ett meal med dryck")