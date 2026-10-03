class Temperature:
    def __init__(self,celaius):
        self.celaius = celaius

    @staticmethod
    def celsius_to_fahrenheit(celaius):
        return (celaius *9/5) + 32

print(Temperature.celsius_to_fahrenheit(0))  
print(Temperature.celsius_to_fahrenheit(100))  