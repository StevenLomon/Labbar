#YH Grundläggande Python Vecka 3 labbar

#DICTIONARIES
def dictKeyCheck(dict, key):
    if key in dict:
        print("Key is present in the dictionary")
    else:
        print("Key is not present in the dictionary")

d = {1: 15, 2: 18, 3: 22}
dictKeyCheck(d,2)
dictKeyCheck(d,4)