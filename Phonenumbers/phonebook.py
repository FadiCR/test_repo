class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]
    
    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
    
    def subtract(x,y):
        return x - y

    def multiply(x,y):
        return x*y
    
    def divide(x,y):
        return x/y
    
    def output(input):
        print(input)

    def isVowel(charac):
        if charac in "aeiou":
            return True
        return False
     
    def isBool(input):
        if input == True or input == False:
            return True
        return False
    
    def error(theoretical, experimental):
        result = abs(experimental - theoretical)/theoretical
        return result
    
    def myname():
        print("Fadi Charbel Rahme")

    def lunch():
        print("Chicken and pasta.")

    def time():
        print("this function was added at 10:20 AM")
    
    def meeting():
        print("we have a meeting at 11:15 AM")