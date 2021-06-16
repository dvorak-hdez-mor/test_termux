class Coche:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def name(self):
        return self.__nombre
    
    @name.setter
    def name(self, nombre):
        self.__nombre = nombre
        print("Nombre modificado".center(30, "-"))

coche1 = Coche("Audi")
print(coche1.name)

coche1.name = "Volkswagen"
print(coche1.name)
