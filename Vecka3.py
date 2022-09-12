#YH Grundläggande Python Vecka 3 labbar

#DICTIONARIES
def dictKeyCheck(dict, key):
    if key in dict:
        return "Key is present in the dictionary"
    else:
        return "Key is not present in the dictionary"

d = {1: 15, 2: 18, 3: 22}
print(f"For 2 in d: {dictKeyCheck(d,2)}")
print(f"For 4 in d: {dictKeyCheck(d,4)}")

def dictPrintUnique(dict):
    uniqueDict = dict.copy()
    return uniqueDict

s =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
{"VIII":"S007"}]
print(f"Unique values: {dictPrintUnique(s)}")

def dictGetTopThree(dict):
    dictKeys = list(dict.keys())
    dictValues = list(dict.values())
    dictValues.sort()
    topThreeValues = [dictValues[-3:]] #USEFUL! Get the last three items in the sorted list (the three largest items)
    #topThreeItems = [
    #    [dict[] == topThreeValues[-1], topThreeValues[-1]]
    #]

    return topThreeValues

sample = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print(f"Top three items in shop: {dictGetTopThree(sample)}")