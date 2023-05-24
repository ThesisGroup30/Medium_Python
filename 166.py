class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = ""
        if (numerator < 0) ^ (denominator < 0):
            result += "-"

        numerator, denominator = abs(numerator), abs(denominator)
        result += str(numerator // denominator)

        remainder = numerator % denominator
        if remainder == 0:
            return result

        result += "."
        decimal = ""
        remainders = {}

        while remainder != 0:
            if remainder in remainders:
                decimal = decimal[:remainders[remainder]] + "(" + decimal[remainders[remainder]:] + ")"
                break

            remainders[remainder] = len(decimal)
            remainder *= 10
            decimal += str(remainder // denominator)
            remainder %= denominator

        if decimal:
            result += decimal

        return result
