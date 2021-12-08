class Diagnostic:
    def __init__(self):
        self.diagnostic_input = []
        self.bit_dict = {}
        self.epsilon_rate = ""
        self.gamma_rate = ""
        self.o2_gen_rating = ""
        self.co2_scrub_rating = ""
        self.power_consumption = 0
        self.life_support_rating = 0

    def get_input(self, file):
        file_input = []
        with open(file) as f:
            lines = f.read().splitlines()
            # file_input = list(map(str, lines))

        self.diagnostic_input = lines

    def generate_bit_dict(self, input_sample):
        bit_dict = {}
        for i in range(len(input_sample)):
            bit_dict[f"bit{i}"] = [0, 0]

        return bit_dict

    def convert_binary(self, binary):
        decimal = int(binary, 2)

        return decimal

    def populate_bit_dict(self, diagnostic_input):
        bit_dict = self.generate_bit_dict(diagnostic_input[0])

        for i in range(len(diagnostic_input)):
            for j in range(len(diagnostic_input[i])):
                bit_key = f"bit{j}"
                if int(diagnostic_input[i][j]):
                    bit_dict[bit_key][1] += 1
                else:
                    bit_dict[bit_key][0] += 1

        self.bit_dict = bit_dict

    def calculate_gamma_epsilon_rates(self):
        for bit in self.bit_dict:
            if self.bit_dict[bit][0] > self.bit_dict[bit][1]:
                self.gamma_rate += str(0)
                self.epsilon_rate += str(1)
            elif self.bit_dict[bit][1] > self.bit_dict[bit][0]:
                self.gamma_rate += str(1)
                self.epsilon_rate += str(0)

    def calculate_o2_rate(self, numbers):
        values = numbers
        pos = 0
        iteration = 0

        while len(values) >= 2 or pos <= len(values[0]):
            if pos == 12 or len(values) == 1:
                break

            t_bit = 0
            t_list = []
            f_bit = 0
            f_list = []

            for i in range(len(values)):
                number = values[i]
                if number[pos] == "1":
                    t_bit += 1
                    t_list.append(number)
                else:
                    f_bit += 1
                    f_list.append(number)

            if t_bit >= f_bit:
                values = t_list
            else:
                values = f_list

            iteration += 1
            pos += 1

        if pos == len(values[0]) and len(values) > 1:
            for number in values:
                if number[-1] == "1":
                    self.o2_gen_rating = number
        else:
            self.o2_gen_rating = values[0]

    def calculate_co2_rate(self, numbers):
        values = numbers
        pos = 0
        iteration = 0

        while len(values) >= 2 or pos <= len(values[0]):
            if pos == 12 or len(values) == 1:
                break

            t_bit = 0
            t_list = []
            f_bit = 0
            f_list = []

            for i in range(len(values)):
                number = values[i]
                if number[pos] == "1":
                    t_bit += 1
                    t_list.append(number)
                else:
                    f_bit += 1
                    f_list.append(number)

            if f_bit <= t_bit:
                values = f_list
            else:
                values = t_list

            iteration += 1
            pos += 1

        if pos == len(values[0]) and len(values) > 1:
            for number in values:
                if number[-1] == "0":
                    self.o2_gen_rating = number
        else:
            self.co2_scrub_rating = values[0]

    def calculate_o2_co2_rates(self):
        self.calculate_o2_rate(self.diagnostic_input)
        self.calculate_co2_rate(self.diagnostic_input)

    def calculate_power_consumption(self):
        self.calculate_gamma_epsilon_rates()
        epsilon_decimal = self.convert_binary(self.epsilon_rate)
        gamma_decimal = self.convert_binary(self.gamma_rate)
        self.power_consumption = epsilon_decimal * gamma_decimal

    def calculate_life_support_rating(self):
        self.calculate_o2_co2_rates()
        o2_decimal = self.convert_binary(self.o2_gen_rating)
        co2_decimal = self.convert_binary(self.co2_scrub_rating)
        self.life_support_rating = o2_decimal * co2_decimal

    def generate_diagnostic(self, file):
        self.get_input(file)
        self.populate_bit_dict(self.diagnostic_input)
        self.calculate_power_consumption()
        self.calculate_life_support_rating()
        return f"""
    Diagnostic Report:
        Power Consumption: {self.power_consumption}
        Life Support Rating: {self.life_support_rating}
        """


def main():
    diagnostic = Diagnostic()
    diagnostic_report = diagnostic.generate_diagnostic(
        "diagnostic_input.txt")
    print(diagnostic_report)


if __name__ == "__main__":
    main()
