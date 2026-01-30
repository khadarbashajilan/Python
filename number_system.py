import math
class NumberSystem:
    getDigit_hexa = {"A" : 10, "B" : 11, "C" : 12, "D": 13, "E" : 14, "F" : 15}
    getChar_hexa = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    
    def covertToDecimal(self, input, currentBase):
        res = 0
        pos = 0
        for i in range(len(input)-1 , -1, -1):

            char = input[i] 
            digit = self.getDigit_hexa[char.upper()]  if char.upper() in self.getDigit_hexa else int(char)

            res = res + digit * int(math.pow(currentBase, pos))
            pos += 1

        return res

    def convertFromDecimal(self, input, destinationBase):
        if input == 0: return "0"

        res = []

        while input > 0:
            rem = input % destinationBase

            char = self.getChar_hexa[rem] if rem in self.getChar_hexa else str(rem)

            res.append(char)

            input //= destinationBase

        res.reverse()
        return "".join(res)
    
    
test1 = NumberSystem()
print(f"Binary '1000' to Decimal: {test1.covertToDecimal('1000', 2)}") # Output: 8
print(f"Decimal 3 to Binary: {test1.convertFromDecimal(3, 2)}")         # Output: 11