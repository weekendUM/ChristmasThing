class present:
    color : str
    name : str
    pass

    

class letter:
    """
    item : present
    name : str
    addres : str
    text : str
    """
    def __init__(self, args = []):
        self.name =  args[0]
        self.address = args[1]
        self.text = args[2]
        self.item = present()
        self.item.name = args[3]
        self.item.color = args[4]

    def __str__(self):
        return f"Nume: {self.name}\nAdresa: {self.address}\nTextul scrisorii: {self.text}\nNumele cadoului: {self.item.name}\nCuloarea cadoului: {self.item.color}"


    def setName(self, name): self.name = name
    pass


