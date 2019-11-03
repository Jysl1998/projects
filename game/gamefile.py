'''
File for game code
Created Spring 2018
@author: Juliana Lim (jsl68)
'''
#import random for int and sys (just in case)
import  random
import sys

#create class Questions, this is where you will create the equations and return it for the gui
class Questions:
    #call out function calculate, receiving the operator and level 
    def calculate(self, operator, level):
        #create instance variables for var1 and var 2 (for now create default variable which is random.randint(0,9)- easy level)
        #create an empty list calling it equa (equations)
        self._var1 = random.randint(0,9)
        self._var2 = random.randint(0,9)
        equa = []
        
        #if operator is + and level is easy then make sure the random integer is from range (0,9) for both
        if operator == '+' and level == 'easy':
            #create self.total = var1 + var2 
            self.total = int(self._var1 + self._var2)
            #add var1, var2, operator, and total into a list (in order though)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            #return equa
            return equa
        
        #if operator is + and level is medium then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)
        elif operator == '+' and level == 'medium':
            self._var1 = random.randint(0,50)
            self._var2 = random.randint(0,10)
            self.total = int(self._var1 + self._var2)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            return equa
        
        #if operator is + and level is hard then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)
        elif operator == '+' and level == 'hard':
            self._var1 = random.randint(0,999)
            self._var2 = random.randint(0,99)
            self.total = int(self._var1 + self._var2)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            return equa
                
        #if operator is - and level is easy then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)        
        elif operator == '-' and level == 'easy':
            self._var1 = random.randint(0,10)
            self._var2 = random.randint(0,9)
            #create a loop where var1 must be higher than var2 (don't wany any negative ints for the kids!)
            while self._var1 >= self._var2:
                self.total = int(self._var1 - self._var2)
                equa.append(self._var1)
                equa.append(operator)
                equa.append(self._var2)
                equa.append(int(self.total))
                return equa
            
        #if operator is - and level is medium then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)        
        elif operator == '-' and level == 'medium':
            self._var1 = random.randint(0,50)
            self._var2 = random.randint(0,50)
            #create a loop where var1 must be higher than var2 (don't wany any negative ints for the kids!)
            while self._var1 >= self._var2:
                self.total = int(self._var1 - self._var2)
                equa.append(self._var1)
                equa.append(operator)
                equa.append(self._var2)
                equa.append(int(self.total))
                return equa
        
        #if operator is - and level is hard then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)
        #for this, negatives should not be a problem at all, since it's supposed to be hard! 
        elif operator == '-' and level == 'hard':
            self._var1 = random.randint(0,99)
            self._var2 = random.randint(0,50)
            self.total = int(self._var1 - self._var2)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            return equa
        
        #if operator is * and level is easy then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)                
        elif operator == '*' and level == 'easy':
            self._var1 = random.randint(0,10)
            self._var2 = random.randint(0,10)
            self.total = int(self._var1 * self._var2)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            return equa
        
        #if operator is * and level is medium then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)        
        elif operator == '*' and level == 'medium':
            self._var1 = random.randint(0,12)
            self._var2 = random.randint(0,12)
            self.total = int(self._var1 * self._var2)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            return equa
        
        #if operator is * and level is hard then change the random integer range for both
        #repeat the steps (add list and self.total returning the list of equa)        
        elif operator == '*' and level == 'hard':
            self._var1 = random.randint(0,20)
            self._var2 = random.randint(0,20)
            self.total = int(self._var1 * self._var2)
            equa.append(self._var1)
            equa.append(operator)
            equa.append(self._var2)
            equa.append(int(self.total))
            return equa
        
        

if __name__ == '__main__':
    #calc = Questions()
    calc = Questions()
    #create one test function and see if it passes
    #passed 
    #calc.calculate('+', 'easy')