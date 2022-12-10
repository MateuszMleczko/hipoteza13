class Num:
    real_num = 0
    total_num = 0

    def __init__(self, real_num, total_num):

        if not (0 <= real_num < 1) or total_num <= 0:
            print("Wrong numbers")
        else:
            self.real_num = real_num
            self.total_num = total_num

    def Binary(self):
        print(0)
        y = self.real_num
        for i in range(self.total_num):
            if y >= 1/2:
                print(1)
            else:
                print(0)
        y = y * 2
        if y >= 1:
            y = y - 1

    def Trinary(self):
        trinary = '0.'
        while self.real_num != 0 and len(trinary) <= self.total_num:
            self.real_num = self.real_num * 3
            trinary += str(int(self.real_num))
            self.real_num = self.real_num - int(self.real_num)
        return trinary

    # def Trinary(self):
    #     print(0)
    #     for i in range(self.total_num):
    #         if self.real_num % 3 == 0:
    #             print(0)
    #         elif self.real_num % 3 == 2:
    #             print(2)
    #         elif self.real_num % 3 == 1:
    #             print(1)
    #         self.real_num = self.real_num * 3

    # def Trinary(self):
    #     print(0)
    #     y = self.real_num
    #     for i in range(self.real_num):
    #         if y >= 2/3:
    #             print(2)
    #         if y >= 2:
    #             print(1)
    #         if y >= 1:
    #             print(0)
    #         y = y * 3

    # def Trinary(self):
    #     print(0)
    #     y = self.real_num
    #     for i in range(self.real_num):
    #         if y >= 2/3:
    #             print(2)
    #         if:
    #             print(1)
    #         if:
    #             print(0)
    #         y = y * 3
    #         if y >= 2:
    #
    #         if y >= 1:


    def MainProgram(self):
        print("Select what type you want to convert")
        while option != 1 or option !=0:
            option = int(input("Enter '1' --> BINARY  /  '2' --> TRINARY"))
        if option == 1:
            x = float(input("Enter the real number(x) specifying the interval [0, 1): "))
            k = int(input("Enter a positive integer(k): "))
            n = Num(x, k)
            n.Binary()
        elif option == 2:
            x = float(input("Enter the real number(x) specifying the interval [0, 1): "))
            k = int(input("Enter a positive integer(k): "))
            n = Num(x, k)
            print(n.Trinary())

Num.MainProgram()