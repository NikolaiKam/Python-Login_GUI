import random

class Generate_Numbers():

    def __init__(self):
        self.options=0
        self.num=0
        self.letter=0

    def generate_options(self):    
        self.options=random.randint(1,2)
        return self.options
    
    def generate_numbers(self):
        self.num=random.randint(0,9)
        return self.num

    def generate_letters(self):
        self.letter=chr(random.randint(97,122))
        return self.letter.upper()

class Generate_Code(Generate_Numbers):
    
    def __init__(self):
        self.count_letter=0
        self.count_number=0
        self.code=''

    def generate_code(self):
        
        while len(self.code)<5:

            if self.generate_options()==1:
                if self.count_number==2:
                    continue
                self.code+=str(self.generate_numbers())
                self.count_number+=1

            else:
                if self.count_letter==3:
                    continue
                self.code+=self.generate_letters()
                self.count_letter+=1
        return self.code

    def __str__(self):
        self.generate_code()
        return self.code

code=Generate_Code()

