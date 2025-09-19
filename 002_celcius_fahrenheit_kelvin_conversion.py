class CelciusFahrenheitKelvinConversion:
    def __init__(self, temp, unit):
        self.temperature = temp
        self.unit = unit

    def convertCelciusToFahrenheit(self):
        return (((self.temperature)*9)/5)+32

    def convertCelciusToKelvin(self):
        return (self.temperature + 273.15)

    def convertFahrenheitToCelcius(self):
        return ((self.temperature-32)*5)/9

    def convertFahrenheitToKelvin(self):
        return (((self.temperature-32)*5)/9)+273.15

    def convertKelvinToCelcius(self):
        return self.temperature - 273.15

    def convertKelvinToFahrenheit(self):
        return (((self.temperature-273.15)*9)/5)+32
    
    def display_result(self):
        ALPHABET_C = "C"
        ALPHABET_F = "F"
        ALPHABET_K = "K"

        if self.unit.upper() == ALPHABET_C:
            print(f"{self.temperature} in celcius = {self.convertCelciusToFahrenheit()} in fahrenheit")
            print(f"{self.temperature} in celcius = {self.convertCelciusToKelvin()} in kelvin")
        elif self.unit.upper() == ALPHABET_F:
            print(f"{self.temperature} in fahrenheit = {self.convertFahrenheitToCelcius()} in celcius")
            print(f"{self.temperature} in fahrenheit = {self.convertFahrenheitToKelvin()} in kelvin")
        elif self.unit.upper() == ALPHABET_K:
            print(f"{self.temperature} in kelvin = {self.convertKelvinToCelcius()} in celcius")
            print(f"{self.temperature} in kelvin = {self.convertKelvinToFahrenheit()} in fahrenheit")
        else:
            print("Please enter correct unit of temperature (C/F/K).")

print("Please enter the temperature to be converted: ")
temp = float(input())

print("Please enter the unit of temperature (C for Celcius, F for Fahrenheit and K for Kelvin): ")
unit = input()

obj = CelciusFahrenheitKelvinConversion(temp, unit)
obj.display_result()