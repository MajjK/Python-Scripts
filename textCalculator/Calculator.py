# Write a program that returns the result obtained from a set of instructions.
# The instructions consist of a keyword and a number separated by a space. The instructions are separated by a newline
# character. The set of instructions is taken from a file and the result should be printed on the screen.
# Instructions can be any operation taking two arguments (e.g. add, subtract, multiply, divide, etc.).
# Instructions should be interpreted in order of insertion (the order of operations in mathematics should be ignored).
# The last instruction should be apply and number.

class Calculator:
    def __init__(self, instruction):
        instruction = instruction.split('\n')
        self.instructions = [i.split(' ') for i in instruction]
        self.base = float(self.instructions[-1][1])

    def Compute(self):
        result = self.base
        for i in range(len(self.instructions)-1):
            operator = self.instructions[i][0]
            operand = float(self.instructions[i][1])
            if operator == "add":
                result += operand
            elif operator == "subtract":
                result -= operand
            elif operator == "multiply":
                result *= operand
            elif operator == "divide":
                result /= operand
        return result


if __name__ == "__main__":
    f = open("Instruction.txt", "r")
    Calculator = Calculator(f.read())
    f.close()
    print(Calculator.Compute())
