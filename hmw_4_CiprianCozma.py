class Calculator():
    number1 = {}
    number2 = {}
    
    def sum(self):
        sum = self.number1 + self.number2
        print("Sum between {0} and {1} is: ".format(self.number1, self.number2), sum)
    
    def subtract(self):
        subtract = self.number1 - self.number2
        print("Subtract between {0} and {1} is :".format(self.number1, self.number2), subtract)
        
    def multiply(self):
        multiply = self.number1 * self.number2
        print("Multiply between {0} and {1} is: ".format(self.number1, self.number2), multiply)
        
    def division(self):
        if(self.number1 == 0 or self.number2 == 0):
             print("You cannot divide by 0!!!")
        else:
            division = self.number1 / self.number2
            print("Division between {0} and {1} is: ".format(self.number1, self.number2), division)
        

instance = Calculator()
instance.number1 = 3
instance.number2 = 5

instance.sum()
instance.subtract()
instance.multiply()
instance.division()