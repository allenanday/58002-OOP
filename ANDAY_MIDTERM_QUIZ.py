class TempConversion:
    def __init__(self, temp):
        self.temperature = temp

    def to_celsius(self, source_scale):
        if source_scale == 'f':
            return (self.temperature - 32) * 5 / 9
        elif source_scale == 'k':
            return self.temperature - 273.15
        else:  # source_scale == 'c'
            return self.temperature

    def to_fahrenheit(self, source_scale):
        if source_scale == 'c':
            return self.temperature * 9 / 5 + 32
        elif source_scale == 'k':
            return (self.temperature - 273.15) * 9 / 5 + 32
        else:  # source_scale == 'f'
            return self.temperature

    def to_kelvin(self, source_scale):
        if source_scale == 'c':
            return self.temperature + 273.15
        elif source_scale == 'f':
            return (self.temperature - 32) * 5 / 9 + 273.15
        else:  # source_scale == 'k'
            return self.temperature

    def fahrenheit_to_celsius(self):
        return self.to_celsius('f')

    def kelvin_to_celsius(self):
        return self.to_celsius('k')

    def celsius_to_fahrenheit(self):
        return self.to_fahrenheit('c')

    def kelvin_to_fahrenheit(self):
        return self.to_fahrenheit('k')

    def celsius_to_kelvin(self):
        return self.to_kelvin('c')

    def fahrenheit_to_kelvin(self):
        return self.to_kelvin('f')

temperature = float(input("Enter a temperature: "))
conversion = TempConversion(temperature)

print(conversion.fahrenheit_to_celsius())
print(conversion.kelvin_to_celsius())
print(conversion.celsius_to_fahrenheit())
print(conversion.kelvin_to_fahrenheit())
print(conversion.celsius_to_kelvin())
print(conversion.fahrenheit_to_kelvin())