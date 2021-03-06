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
        self.quantity = int(quantity)
        self.time=0
        self.adjectives = adjectives
        self.UID = uid
    def add_time_toy(self,time_toy):
        self.time= self.time+time_toy


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
#cineva care stie engleza sa explice dracia asta pls <3
class Time():
    def __init__(self):
        self.time_material=0
        self.time_individual_toy=0
        self.time_paint=0
    def add_individual_toy_time(self,time):
        self.time_individual_toy=self.time_individual_toy+time
    def add_paint_time(self,time):
        self.time_paint=self.time_paint+time
    def add_total_material_time(self,time):
        self.time_material=self.time_material+time
    def get_total_time(self):
        return self.time_individual_toy+self.time_material+self.time_paint

totalTime=Time()

# lists with keywords for searching specific gifts
electronics = ['huawei', 'iphone', 'xiaomi', 'samsung', 'nintendo', 'xbox', 'smartphone', 'console', 'phone', 'tablet',
               'oral-b', 'amd', 'nvidia', 'computer', 'laptop', 'tv', 'monitor', 'keyboard', 'microphone', 'headphones',
               'camera', 'electronic', 'kindle', 'smart', 'robot', 'earphones', 'buds']
food = ['cheese', 'candy', 'fruit', 'chocolate', 'wafers']
textiles = ['pants', 'shirt', 't-shirt', 'dress', 'shorts', 'sandals', 'shoes', 'stiletto', 'wig', 'scarf', 'backpack',
            'handbag', 'pillow', 'blanket', 'slippers', 'hoodie', 'hat', 'sweater', 'jeans', 'plush', 'nike', 'dior',
            'burlon', 'balenciaga', 'adidas', 'versace', 'jordan', 'prada', 'gucci', 'kors', 'chanel', 'lv', 'moschino',
            'zara', 'reserved', 'skirt']
paper = ['poster', 'book', 'giftcard']
 
time_common_toys={'huawei':38.35, 'iphone':49.42, 'xiaomi':33.25, 'samsung':53.65, 'nintendo':65.37, 'xbox':85.28, 'smartphone':31.87, 'console':78.63, 'phone':30.23, 'tablet':41.56,
               'oral-b':12.40, 'amd':37.79, 'nvidia':34.53, 'computer':98.99, 'laptop':113.43, 'tv':57.55, 'monitor':50.36, 'keyboard':23.44, 'microphone':18.76, 'headphones':27.77,
               'camera':50.36, 'electronic':20.20, 'kindle':39.52, 'smart':26.49, 'robot':279.96, 'earphones':16.40, 'buds':23.63,
               
               'cheese':30.12, 'candy':15.23, 'fruit':3.53, 'chocolate':25.11, 'wafers':9.83,

               'pants':10.23, 'shirt':12.20, 't-shirt':7.03, 'dress':18.34, 'shorts':8.80, 'sandals':13.25, 'shoes':20.97, 'stiletto':21.59, 'wig':13.40, 'scarf':4.20, 'backpack':21.89,
               'handbag':19.08, 'pillow':8.28, 'blanket':7.54, 'slippers':5.84, 'hoodie':16.87, 'hat':9.12, 'sweater':15.05, 'jeans':11.13, 'plush':15.67, 'nike':23.24, 'dior':20.38,
               'burlon':9.24, 'balenciaga':28.30, 'adidas':21.07, 'versace':25.26, 'jordan':24.20, 'prada':17.74, 'gucci':10.43, 'kors':18.27, 'chanel':20.76, 'lv':5.52, 'moschino':12.36,
                'zara':16.95, 'reserved':17.99, 'skirt':8.09,

                "skateboard":6.23,"skate":6.23,"doll":16.23,"bike":23.34,"bicycle":23.34,

                'poster':3.13, 'book':10.65, 'giftcard':1.84}

# initializing child and materials
MalumaLaurentiu = Child()
MatL = Materials()

# random input for testing the code
MalumaLaurentiu.gifts.append(Gift("zee beez zing toy", "1", "khaki", "1234AV"))
MalumaLaurentiu.gifts.append(Gift("Huawei Media Pad T2 7", "1", "", "1234AV"))
# checking the keywords, first for the object and if that fails for the material -- if that also fails we're making it a plastic toy, all values are assigned randomly for variation
for i in MalumaLaurentiu.gifts:
    declassified = ""
    toy = re.split(" ", i.obj)
    for j in toy:
        declassified=""
        if j.lower() in electronics:
            declassified = j.lower()
            qtt = random.randrange(10, 18)
            qtt *= i.quantity
            MatL.add_mat('copper', qtt)
            qtt = round(random.uniform(0.01, 1), 2)
            qtt *= i.quantity
            MatL.add_mat('gold', round(MatL.get_mat_qtt('gold') + qtt, 2))
            qtt = round(random.uniform(0.3, 0.6), 2)
            qtt *= i.quantity
            MatL.add_mat('silver', round(MatL.get_mat_qtt('silver') + qtt, 2))
            qtt = random.randrange(100, 500)
            qtt *= i.quantity
            MatL.add_mat('plastic', qtt)            
            qtt = random.randrange(10, 50)
            qtt *= i.quantity
            MatL.add_mat('glass', qtt)            
            qtt = round(random.uniform(10, 60), 2)
            qtt *= i.quantity
            MatL.add_mat('iron', round(MatL.get_mat_qtt('iron') + qtt, 2))
            break
        elif j.lower() in food:
            declassified = j.lower()
            qtt = random.randrange(500, 2000)
            qtt *= i.quantity
            MatL.add_mat('groceries', qtt)
            break
        elif j.lower() in textiles:
            declassified = j.lower()
            qtt = random.randrange(250, 1000)
            qtt *= i.quantity
            MatL.add_mat('textile', qtt)
            break
        elif j.lower() in paper:
            declassified = j.lower()
            qtt = random.randrange(25, 250)
            qtt *= i.quantity
            MatLaadd_mat('paper', qtt)            
            break
        elif j.lower() == 'bike' or j.lower() == 'bicycle':
            declassified = j.lower()
            qtt = round(random.uniform(1000, 5000), 2)
            qtt *= i.quantity
            MatL.add_mat('aluminium', round(MatL.get_mat_qtt('aluminium') + qtt, 2))
            qtt = round(random.uniform(500, 750), 2)
            qtt *= i.quantity
            MatL.add_mat('rubber', round(MatL.get_mat_qtt('rubber') + qtt, 2))
            qtt = random.randrange(250, 500)
            qtt *= i.quantity
            MatL.add_mat('textile', qtt)
            break
        elif j.lower() == 'doll':
            declassified = j.lower()
            qtt = random.randrange(10, 20)
            qtt *= i.quantity
            MatL.add_mat('textile', qtt)
            qtt = random.randrange(100, 250)
            qtt *= i.quantity
            MatL.add_mat('plastic', qtt)
            break
        elif j.lower() == 'skateboard' or j.lower() == 'skate':
            declassified = j.lower()
            qtt = random.randrange(450, 900)
            qtt *= i.quantity
            MatL.add_mat('wood', qtt)
            qtt = round(random.uniform(100, 250), 2)
            qtt *= i.quantity
            MatL.add_mat('iron', round(MatL.get_mat_qtt('iron') + qtt, 2))
            qtt = round(random.uniform(100, 150), 2)
            qtt *= i.quantity
            MatL.add_mat('rubber', round(MatL.get_mat_qtt('rubber') + qtt, 2))
            break
    if declassified!="":
        i.add_time_toy(time_common_toys[declassified]*float(i.quantity))
        totalTime.add_individual_toy_time(time_common_toys[declassified]*float(i.quantity))


    if declassified == "":
        adj = re.split(" ", i.adjectives)
        for j in adj:
            if j == 'copper':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= i.quantity
                MatL.add_mat('copper', qtt)
                break
            elif j == 'gold':
                declassified = 1
                qtt = random.randrange(5, 200)
                qtt *= i.quantity
                MatL.add_mat('gold', round(MatL.get_mat_qtt('gold') + qtt, 2))
                break
            elif j == 'silver':
                declassified = 1
                qtt = random.randrange(5, 300)
                qtt *= i.quantity
                MatL.add_mat('silver', round(MatL.get_mat_qtt('silver') + qtt, 2))
                break
            elif j == 'aluminium':
                declassified = 1
                qtt = random.randrange(100, 500)
                qtt *= i.quantity
                MatL.add_mat('aluminium', round(MatL.get_mat_qtt('aluminium') + qtt, 2))
                break
            elif j == 'glass':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= i.quantity
                MatL.add_mat('glass', round(MatL.get_mat_qtt('glass') + qtt, 2))
                break
            elif j == 'porcelain':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= i.quantity
                MatL.add_mat('porcelain', round(MatL.get_mat_qtt('porcelain') + qtt, 2))
                break
            elif j == 'rubber':
                declassified = 1
                qtt = random.randrange(50, 500)
                qtt *= i.quantity
                MatL.add_mat('rubber', round(MatL.get_mat_qtt('rubber') + qtt, 2))
                break
            elif j == 'wooden':
                declassified = 1
                qtt = random.randrange(200, 1000)
                qtt *= i.quantity
                MatL.add_mat('wood', round(MatL.get_mat_qtt('wood') + qtt, 2))
                break
    if declassified == "":
        qtt = random.randrange(200, 600)
        qtt *= i.quantity
        MatL.add_mat('plastic', qtt)
        var=random.randrange(6, 70)
        i.add_time_toy= var*i.quantity #random time cuz why not lmao

        #bere Alex.Suciu

# random print to check the values
print(MatL.get_mat_qtt('plastic'))

##################################################################################
#material times here

M_Names = ['plastic','glass','textile','iron','aluminium','copper', 'gold','silver', 'wood', 'porcelain','rubber', 'paper','groceries']

total_time=0

for material in M_Names:
    buffer = MatL[material]
    #in hrs (t_buffer)
    t_buffer = MatL[material][0] / 1000 / MatL[material][1]
    MatL.add_time(material, t_buffer)
    print(f"The production time of {material} is: {MatL.get_mat_time(material)}")
    total_time+=t_buffer
#minutes (totalTime)
totalTime.add_total_material_time(total_time)
print(totalTime.get_total_time())

