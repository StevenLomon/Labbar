#YH Grundläggande Python Vecka 5 labbar
from datetime import datetime, timedelta

print("\nPRINT DATE IN TWO FORMATS")
nu = datetime.now()
print(f"Complete Date: {nu.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Short Date: {nu.strftime('%Y-%m-%d')}")

print("\nPARTS OF DATETIME")
nu = datetime.now()
print(f"Year = {nu.year}")
print(f"Month = {nu.month}")
print("etc etc")

print("\nDAY OF THE WEEK FROM A DATE")
def getWeekdayName(weekdaynum:int) -> str:
    if weekdaynum == 0:
        return "Måndag"
    if weekdaynum == 1:
        return "Tisdag"
    if weekdaynum == 2:
        return "Onsdag"
    if weekdaynum == 3:
        return "Torsdag"
    if weekdaynum == 4:
        return "Fredag"
    if weekdaynum == 5:
        return "Lördag"
    if weekdaynum == 6:
        return "Söndag"
    return "Ogiltig dag"

year = int(input("Ange ett år: "))
mon = int(input("Ange en månad: "))
dag = int(input("Ange en dag: "))
date = datetime(input(year, mon, dag))
weekday = getWeekdayName(date.weekday())
print(f"Datumet du matat in är en {weekday}")

#LECTURE
# fakturaDatum = datetime.now()
# forfallodag = fakturaDatum + timedelta(days=30)
# if forfallodag.weekday() == 5:
#     forfallodag = forfallodag + forfallodag(days=-1) #If Saturday, go back to Friday
# if forfallodag.weekday() == 6:
#     forfallodag = forfallodag + forfallodag(days=1) #If Sunday, go forward to Monday

# formattedForfallodag = forfallodag.strftime('%Y-%m-%d')
# print(f"Förfallodag: {formattedForfallodag}")

# def getWeekdayName(weekdaynum:int) -> str:
#     if weekdaynum == 0:
#         return "Måndag"
#     if weekdaynum == 1:
#         return "Tisdag"
#     if weekdaynum == 2:
#         return "Onsdag"
#     if weekdaynum == 3:
#         return "Torsdag"
#     if weekdaynum == 4:
#         return "Fredag"
#     if weekdaynum == 5:
#         return "Lördag"
#     if weekdaynum == 6:
#         return "Söndag"
#     return "Ogiltig dag"

# nu = datetime.now()
# jullovet = datetime(2022,12,14)
# print(f"Antal dagar till jullovet:{(jullovet-nu).days}")


# year = int(input("Ange år du är född: "))
# mon = int(input("Ange månad du är född: "))
# dag = int(input("Ange dag du är född: "))
# birthdate = datetime(year, mon, dag)
# weekday = getWeekdayName(birthdate.weekday())
# nu = datetime.now()
# diff = nu - birthdate 
# print(f"Du är född på en {weekday}")
# print(f"Du är {diff.days} dagar gammal")

# nu = datetime.now() #keep in mind, it doesn't update itself!!
# if nu.month == 9 or nu.month == 10 or nu.month == 11:
#     print("Beklagar... tråkig höst är det nu")
# elif nu.month == 12:
#     print("Julmånad")
# print(nu)