class DigitSumCalculator:
    def extract_digits(self, number):
        num_str = str(number)
        digits = [int(digit) for digit in num_str]
        return len(digits)

    def find_number_with_sum(self, target_sum):
        sum = 0
        i = 1
        while True:
            sum = sum + self.extract_digits(i)
            if sum >= target_sum:
                break
            i += 1
        return i

# Example usage
if __name__ == "__main__":
    calculator = DigitSumCalculator()
    target_sum = 35
    number = calculator.find_number_with_sum(target_sum)
    print("Number:", number)
