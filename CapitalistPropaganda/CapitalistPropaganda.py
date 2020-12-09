from letter import letter
from letter import present
import json
from json import JSONEncoder

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

buffer = []
for i in range(5):
    if(i==0):
        buffer.append(input("Introduceti numele: "))        
    elif(i==1):
        buffer.append(input("Introduceti adresa: "))
    elif(i==2):
        buffer.append(input("Introduceti textul scrisorii: "))
    elif(i==3):
        buffer.append(input("Introduceti numele cadoului: "))
    elif(i==4):
        buffer.append(input("Introduceti culoarea cadoului: "))

test = letter(buffer)
print()
print(test)
with open("letters.json","w") as out:
    json.dump(test,out,cls=MyEncoder)