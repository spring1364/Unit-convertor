class Volume:
    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.units_dict = {'ml': 1, 'm3': 1, 'ft3': 35.3147, 'litre': 1000, 'cup': 4166.67, 'tbs': 67628.0995061}

    def convert(self):
        try:
            return self.value * (self.units_dict[self.output_unit] / self.units_dict[self.input_unit])
        except KeyError:
            return "Not a valid volume unit is entered! Select from: ml, m3, ft3, litre, cup, tbs"
