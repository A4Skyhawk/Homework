d = {'Moskow':'Russia','Mtsensk':'Russia', 'Washington':'USA','London':'UK'}

S = str(input())

def get_value(d, value):
    for v, k in d.items():
        if v == value:
            return k

if str((get_value(d,S))) != 'None':
    print(get_value(d,S))
else:
    print("I don't get it")

