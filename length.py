class Length:
    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.units_dict = {'m': 1, 'km': 0.001, 'cm': 100, 'ft': 3.28084, 'in': 39.3701, 'yard': 1.09361}

    def convert(self):
        try:
            return self.value * (self.units_dict[self.output_unit] / self.units_dict[self.input_unit])
        except KeyError:
            return "Not a valid length unit is entered! Select from: m, km, cm, ft, in, yard"
