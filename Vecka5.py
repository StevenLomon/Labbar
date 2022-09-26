#YH Grundläggande Python Vecka 5 labbar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dataclasses import dataclass

#***DATETIME***
def getWeekdayName(weekdaynum:int) -> str:
    if weekdaynum == 0:
        return "Monday"
    if weekdaynum == 1:
        return "Tuesday"
    if weekdaynum == 2:
        return "Wednesday"
    if weekdaynum == 3:
        return "Thursday"
    if weekdaynum == 4:
        return "Friday"
    if weekdaynum == 5:
        return "Saturday"
    if weekdaynum == 6:
        return "Sunday"
    return "Invalid day"

def convertToDatetime(date: str) -> datetime: #from format yyyy-mm-dd (Can we add this?)
    year = int(date[0:4])
    mon = int(date[5:7])
    day = int(date[8:10])
    convDate = datetime(year, mon, day)
    return convDate

def getDate(prompt = "Enter a date on the format yyyy-mm-dd, or 'today' for today's date: ") -> str:
    while True:
        try:
            date = input(prompt)
            if date.lower() == 'today':
                return datetime.now()
            else:
                if len(date) != 10:
                    print("Invalid input")
                else:
                    break
        except:
            print("Invalid input")
    return convertToDatetime(date)

# print("\n**PRINT DATE IN TWO FORMATS**")
# nu = datetime.now()
# print(f"Complete Date: {nu.strftime('%Y-%m-%d %H:%M:%S')}")
# print(f"Short Date: {nu.strftime('%Y-%m-%d')}")

# print("\n**PARTS OF DATETIME**")
# nu = datetime.now()
# print(f"Year = {nu.year}")
# print(f"Month = {nu.month}")
# print("...")
# print(f"Second = {nu.second}")
# print(f"Millisecond = {nu.microsecond}")

# print("\n**DAY OF THE WEEK FROM A DATE**")
# year = int(input("Enter a year: "))
# mon = int(input("Enter a month: "))
# dag = int(input("Enter a day: "))
# date = datetime(year, mon, dag)
# weekday = getWeekdayName(date.weekday())
# print(f"{date.strftime('%Y-%m-%d')} is a {weekday}")

# print("\n**ADD n DAYS**")
# now = datetime.now()
# print(f"Today = {now.strftime('%Y-%m-%d %H:%M:%S')}")
# n = int(input("Enter amount of days to add: "))
# diff = now + timedelta(days=n)
# print(f"{n} days from now is {getWeekdayName(diff.weekday())}")

# print("\n**INPUT PARSING**")
# date = getDate()
# print(date.strftime('%Y-%m-%d'))

# print("\n**DAY DIFF BETWEEN TWO DATES**")
# date1 = getDate("Enter first date on the format yyyy-mm-dd, or 'today' for today's date: ")
# date2 = getDate("Enter second date on the format yyyy-mm-dd, or 'today' for today's date: ")
# diff = abs(date1 - date2)
# print(f"Difference in days: {diff.days}")

# print("\n**NUMBER OF DAYS IN A MONTH**")
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# date = datetime(year, month, 1)
# newDate = date + relativedelta(months=+1) + timedelta(days=-1)
# print(f"Month {month} year {year} conains {newDate.day} days")

#***OOB CLASSES***
@dataclass
class Dish:
    Name: str
    Price: float
    Type: str
    Calories: float

dishList = []
for i in range(0,3):
    print(f"Dish #{i+1}:")
    name = input("Enter a name: ").capitalize()
    price = float(input("Enter a price: "))
    type = input("Enter a type: ").capitalize()
    cal = float(input("Enter amount of calories: "))
    d = Dish(name, price, type, cal)
    dishList.append(d)

print("***TODAY'S MENU***")
print(f"Starter: The {dishList[0].Type} {dishList[0].Name} costing ${dishList[0].Price} and consisting of {dishList[0].Calories} calories")
print(f"Main course: The {dishList[1].Type} {dishList[1].Name} costing ${dishList[1].Price} and consisting of {dishList[1].Calories} calories")
print(f"Desert: The {dishList[2].Type} {dishList[2].Name} costing ${dishList[2].Price} and consisting of {dishList[2].Calories} calories")

@dataclass
class Person:
    BirthDate: datetime
    Name: str
    StreetAddress: str
    ZIPCode: str
    City: str



#***POINT***
from point import Point

myPoint = Point( 1.5, 2.5 )
print( myPoint.x )
print( myPoint.y )

#***LECTURE***
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