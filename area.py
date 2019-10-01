class Area:
    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.units_dict = {'cm2': 10000, 'm2': 1, 'ft2': 10.7639, 'ha': 1e-4}

    def convert(self):
        try:
            return self.value * (self.units_dict[self.output_unit] / self.units_dict[self.input_unit])
        except KeyError:
            return "Not a valid area unit is entered! Select from: cm2, m2, ft2, ha"
