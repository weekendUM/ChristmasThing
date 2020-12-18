import re
import random
# classes for child gift, and materials


class Child:
    UUID = '1234AV'
    name = 'Alex NewFolder'

    class Adress:
        Country = 'Romania'
        City = 'Galati'
        street = 'Strada Vietii'
        number = '420'
    gifts = []


class Gift:
    def __init__(self, obj, quantity, adjectives, uid):
        self.obj = obj
        self.quantity = quantity
        self.adjectives = adjectives
        self.UID = uid


class Materials:
    #quantities used in g
    quantities = {
                'plastic': 0,
                'glass': 0,
                'textile' : 0,
                'iron' : 0,
                'aluminium' : 0,
                'copper' : 0,
                'gold' : 0,
                'silver' : 0,
                'wood' : 0,
                'porcelain' : 0,
                'rubber' : 0,
                'paper' : 0,
                'groceries' : 0
                }
    #speed in kg/hr
    speed = {
        'plastic': 72000000,
        'glass': 6833333,
        'textile' : 496564,
        'iron' : 4333333,
        'aluminium' : 33500,
        'copper' : 2833333,
        'gold' : 408.3,
        'silver' : 2566,
        'wood' : 78869,
        'porcelain' : 316666,
        'rubber' : 3833333,
        'paper' : 84500,
        'groceries' : 1
        }

    #total time to produce each material
    time = {
        'plastic': 0,
        'glass': 0,
        'textile' : 0,
        'iron' : 0,
        'aluminium' : 0,
        'copper' : 0,
        'gold' : 0,
        'silver' : 0,
        'wood' : 0,
        'porcelain' : 0,
        'rubber' : 0,
        'paper' : 0,
        'groceries' : 0
        }

    def get_mat_qtt(self, material : str):
        return self.quantities[material]

    def get_mat_speed(self, material : str):
        return self.speed[material]

    def add_mat(self, material : str, qtt):
        self.quantities[material] += qtt

    def add_time(self, material : str, add_time):
        self.time[material] += add_time

    def get_mat_time(self, material : str):
        return self.time[material]


    def __getitem__(self, material : str): #handles the [] operator
        qtt = self.quantities[material]
        time = self.speed[material]
        return (qtt, time)


# lists with keywords for searching specific gifts
electronics = ['huawei', 'iphone', 'xiaomi', 'samsung', 'nintendo', 'xbox', 'smartphone', 'console', 'phone', 'tablet', 'oral-b', 'amd', 'nvidia', 'computer', 'laptop', 'tv', 'monitor', 'keyboard', 'microphone', 'headphones', 'camera', 'electronic']
food = ['cheese', 'candy', 'fruit', 'chocolate', 'wafers']
textiles = ['pants', 'shirt', 't-shirt', 'dress', 'shorts', 'sandals', 'shoes', 'stiletto', 'wig', 'scarf', 'backpack', 'handbag', 'pillow', 'blanket', 'slippers', 'hoodie']
paper = ['poster', 'book', 'giftcard']

# initializing child and materials
MalumaLaurentiu = Child()
MatL = Materials()

# random input for testing the code
MalumaLaurentiu.gifts.append(Gift("zee beez zing toy", "1", "khaki", "1234AV"))
MalumaLaurentiu.gifts.append(Gift("Huawei Media Pad T2 7", "1", "", "1234AV"))
# checking the keywords, first for the object and if that fails for the material -- if that also fails we're making it a plastic toy, all values are assigned randomly for variation
for i in MalumaLaurentiu.gifts:
    declassified = 0
    toy = re.split(" ", i.obj)
    for j in toy:
        if j.lower() in electronics:
            declassified = 1
            qtt = random.randrange(10, 18)
            qtt *= int(i.quantity)
            MatL.add_mat('copper', qtt)
            qtt = round(random.uniform(0.01, 1), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('gold', round(MatL.get_mat_qtt('gold') + qtt, 2))
            qtt = round(random.uniform(0.3, 0.6), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('silver', round(MatL.get_mat_qtt('silver') + qtt, 2))
            qtt = random.randrange(100, 500)
            qtt *= int(i.quantity)
            MatL.add_mat('plastic', qtt)            
            qtt = random.randrange(10, 50)
            qtt *= int(i.quantity)
            MatL.add_mat('glass', qtt)            
            qtt = round(random.uniform(10, 60), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('iron', round(MatL.get_mat_qtt('iron') + qtt, 2))
            break
        elif j.lower() in food:
            declassified = 1
            qtt = random.randrange(500, 2000)
            qtt *= int(i.quantity)
            MatL.add_mat('groceries', qtt)
            break
        elif j.lower() in textiles:
            declassified = 1
            qtt = random.randrange(250, 1000)
            qtt *= int(i.quantity)
            MatL.add_mat('textile', qtt)
            break
        elif j.lower() in paper:
            declassified = 1
            qtt = random.randrange(25, 250)
            qtt *= int(i.quantity)
            MatLaadd_mat('paper', qtt)            
            break
        elif j.lower() == 'bike' or j.lower() == 'bicycle':
            declassified = 1
            qtt = round(random.uniform(1000, 5000), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('aluminium', round(MatL.get_mat_qtt('aluminium') + qtt, 2))
            qtt = round(random.uniform(500, 750), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('rubber', round(MatL.get_mat_qtt('rubber') + qtt, 2))
            qtt = random.randrange(250, 500)
            qtt *= int(i.quantity)
            MatL.add_mat('textile', qtt)
            break
        elif j.lower() == 'doll':
            declassified = 1
            qtt = random.randrange(10, 20)
            qtt *= int(i.quantity)
            MatL.add_mat('textile', qtt)
            qtt = random.randrange(100, 250)
            qtt *= int(i.quantity)
            MatL.add_mat('plastic', qtt)
            break
        elif j.lower() == 'skateboard' or j.lower() == 'skate':
            declassified = 1
            qtt = random.randrange(450, 900)
            qtt *= int(i.quantity)
            MatL.add_mat('wood', qtt)
            qtt = round(random.uniform(100, 250), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('iron', round(MatL.get_mat_qtt('iron') + qtt, 2))
            qtt = round(random.uniform(100, 150), 2)
            qtt *= int(i.quantity)
            MatL.add_mat('rubber', round(MatL.get_mat_qtt('rubber') + qtt, 2))
            break
    if declassified == 0:
        adj = re.split(" ", i.adjectives)
        for j in adj:
            if j == 'copper':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.add_mat('copper', qtt)
                break
            elif j == 'gold':
                declassified = 1
                qtt = random.randrange(5, 200)
                qtt *= int(i.quantity)
                MatL.add_mat('gold', round(MatL.get_mat_qtt('gold') + qtt, 2))
                break
            elif j == 'silver':
                declassified = 1
                qtt = random.randrange(5, 300)
                qtt *= int(i.quantity)
                MatL.add_mat('silver', round(MatL.get_mat_qtt('silver') + qtt, 2))
                break
            elif j == 'aluminium':
                declassified = 1
                qtt = random.randrange(100, 500)
                qtt *= int(i.quantity)
                MatL.add_mat('aluminium', round(MatL.get_mat_qtt('aluminium') + qtt, 2))
                break
            elif j == 'glass':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.add_mat('glass', round(MatL.get_mat_qtt('glass') + qtt, 2))
                break
            elif j == 'porcelain':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.add_mat('porcelain', round(MatL.get_mat_qtt('porcelain') + qtt, 2))
                break
            elif j == 'rubber':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= int(i.quantity)
                MatL.add_mat('rubber', round(MatL.get_mat_qtt('rubber') + qtt, 2))
                break
    if declassified == 0:
        qtt = random.randrange(200, 600)
        qtt *= int(i.quantity)
        MatL.add_mat('plastic', qtt)

# random print to check the values
print(MatL.get_mat_qtt('plastic'))

##################################################################################
#material times here

M_Names = ['plastic','glass','textile','iron','aluminium','copper', 'gold','silver', 'wood', 'porcelain','rubber', 'paper','groceries']

for material in M_Names:
    buffer = MatL[material]
    #print(buffer)
    t_buffer = MatL.get_mat_qtt(material) / 1000 / MatL.get_mat_speed(material)
    MatL.add_time(material, t_buffer)
    print(f"The production time of {material} is: {MatL.get_mat_time(material)}")
