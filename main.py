class Num:
    real_num = 0
    total_num = 0

    def __init__(self):
        if (0 <= self.real_num < 1) or self.total_num <= 0:
            self.real_num = self.real_num
            self.total_num = self.total_num
        else:
            print("Wrong numbers")

    def Binary(self):
        binary = "0."

        while Num.CheckInput(self, binary):
            self.real_num = self.real_num * 2
            binary += str(int(self.real_num))
            self.real_num = self.real_num - int(self.real_num)
        return binary

    def Trinary(self):
        trinary = '0.'

        while Num.CheckInput(self, trinary):
            self.real_num = self.real_num * 3
            trinary += str(int(self.real_num))
            self.real_num = self.real_num - int(self.real_num)
        return trinary

    def CheckInput(self, variable):
        return self.real_num != 0 and len(variable) <= self.total_num + 1

    def MainProgram(self):
        while True:
            print("Enter '1' --> BINARY  /  '2' --> TRINARY  /  '3' --> EXIT")
            option = int(input())
            if option == 1:
                self.CollectInputs()
                print(self.Binary())
            elif option == 2:
                self.CollectInputs()
                print(self.Trinary())
            elif option == 3:
                break
            else:
                print("Wrong value")

    def CollectInputs(self):
        self.real_num = float(input("Enter the real number(x) specifying the interval [0, 1): "))
        self.total_num = int(input("Enter a positive integer(k): "))

n = Num()
n.MainProgram()

