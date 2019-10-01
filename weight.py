class Weight:
    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.units_dict = {'kg': 1, 'pound': 2.20462, 'gr': 1000, 'ounce': 35.274}

    def convert(self):
        try:
            return self.value * (self.units_dict[self.output_unit] / self.units_dict[self.input_unit])
        except KeyError:
            return "Not a valid weight unit is entered! Select from: kg, pound, gr, ounce"