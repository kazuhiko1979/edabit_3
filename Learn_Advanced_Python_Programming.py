class Length_Conversion:
    value = {"mm":0.001, "cm":0.01, "m":1, "km":1000, "im": 0.0254,
            "ft":0.3048, "yd":0.9144, "mi":1609.344}
    
    def __init__(self, x, value_unit="m"):
        self.x = x
        self.value_unit = value_unit
    
    def Convert_to_Metres(self):
        return self.x * Length_Conversion.value[self.value_unit]
    
    def __add__(self, other):
        ans = self.Convert_to_Metres() + other.Convert_to_Metres()
        return Length_Conversion(ans / Length_Conversion.value[self.value_unit], self.value_unit)
    
    def __str__(self):
        return str(self.Convert_to_Metres)
    
    def __repr__(self):
        return "Length_Conversion(" + str(self.x) + " , " + self.value_unit + ")"

if __name__ == "__main__":
    obj1 = Length_Conversion(5.5, "yd") + Length_Conversion(1)
    
    print(repr(obj1))
    print(obj1)
    
    
    
    
        
    


