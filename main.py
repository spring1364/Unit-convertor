from temperature import Temperature
from length import Length
from area import Area
from volume import Volume
from weight import Weight


class Convertor():
    def __init__(self, measurement):
        self.measurement = measurement

    def convert_unit(self, value, input_unit, output_unit):
        if self.measurement is 'length':
            return Length(value, input_unit, output_unit).convert()
        if self.measurement is 'temperature':
            return Temperature(value, input_unit, output_unit).convert()
        if self.measurement is 'area':
            return Area(value, input_unit, output_unit).convert()
        if self.measurement is 'volume':
            return Volume(value, input_unit, output_unit).convert()
        if self.measurement is 'weight':
            return Weight(value, input_unit, output_unit).convert()
        return "Not a valid measurement is entered! Select from : length, temperature, volume, area, weight"


###############################################################################
measurement = 'weight'
value = 100
input_unit = 'gr'
ouput_unit = 'ounce'

converted_value = Convertor(measurement).convert_unit(value, input_unit, ouput_unit)
try:
    if abs(converted_value) >= 0.01:
        print(f'{value: 0.2f} {input_unit} is equal to {converted_value:0.2f} {ouput_unit}')
    else:
        print(f'{value: 0.2f} {input_unit} is equal to {converted_value:0.2e} {ouput_unit}')
except ValueError and TypeError:
    print(converted_value)
