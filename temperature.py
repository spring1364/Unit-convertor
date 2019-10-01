class Temperature:
    def __init__(self, value, input_unit, output_unit):
        self.value = value
        self.input = input_unit
        self.output = output_unit
        self.units_dict = {'c': [1, 0],
                           'f': [9 / 5, 32],
                           'k': [1, 273.15],
                           'r': [9 / 5, 490]}

    def convert(self):
        try:
            return self.value * self.units_dict[self.output][0] / self.units_dict[self.input][0] + \
                   self.units_dict[self.output][1] - (self.units_dict[self.output][0] /
                   self.units_dict[self.input][0]) * \
                   self.units_dict[self.input][1]
        except KeyError:
            return "Not a valid temperature unit is entered! Select from: c, f, k, r"