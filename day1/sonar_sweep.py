class SonarSweep:
    def __init__(self):
        self.sonar_input = []
        self.first_answer = 0
        self.second_answer = 0

    def get_input(self, file):
        file_input = []
        with open(file) as f:
            lines = f.read().splitlines()
            file_input = list(map(int, lines))

        return file_input

    def find_measurements(self, input):
        num_increases = 0

        for i in range(len(input)):
            if input[i] > input[i - 1]:
                num_increases += 1

        return num_increases

    def find_window_measurements(self, input):
        num_increases = 0

        for i in range(1, len(input) - 2):
            three_sum = input[i] + input[i + 1] + input[i + 2]
            prev_sum = input[i - 1] + input[i] + input[i + 1]
            if three_sum > prev_sum:
                num_increases += 1

        return num_increases

    def get_first_solution(self, file):
        self.sonar_input = self.get_input(file)
        self.first_answer = self.find_measurements(self.sonar_input)
        return self.first_answer

    def get_second_solution(self, file):
        self.sonar_input = self.get_input(file)
        self.second_answer = self.find_window_measurements(self.sonar_input)
        return self.second_answer


def main():
    sonar = SonarSweep()
    first_solution = sonar.get_first_solution("sonar_input.txt")
    print("first solution:", first_solution)
    second_solution = sonar.get_second_solution("sonar_input.txt")
    print("second solution:", second_solution)


if __name__ == "__main__":
    main()
