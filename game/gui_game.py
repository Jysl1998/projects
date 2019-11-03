'''
Gui and animation for game
Created Spring 2018
@author: Juliana Lim (jsl68)
'''

#import tkinter, sys, time, and gamefile
from tkinter import *
from gamefile import *
import sys
import time

#create class Game 
class Game:
    #create a function receiving self and window
    def __init__(self, window):
        #create a canvas for the animation
        #create a blue and red circle (make red circle the bad one)
        self.canvas = Canvas(window, width = 700, height = 400, bg = 'light blue')
        blue_circle = self.canvas.create_oval(60,260,100,300,fill = 'blue')
        #create grass, this will not be moving 
        grass = self.canvas.create_rectangle(0,300,700,400, outline = 'green', fill = 'light green')
        #pack self.canvas
        self.canvas.pack()
        self.red_circle = self.canvas.create_oval(600,250,650,300, fill = 'red')

        #create instance variable for window and have self._game become the class Questions()
        self._root = window
        self._game = Questions()
        
        #create frame from window, and pack it
        frame = Frame(self._root)
        frame.pack()
        
        #make operator and level variables, set it to StringVar default setting it to nothing so far
        self._operator = StringVar()
        self._operator.set(NONE)
        self._level = StringVar()
        self._level.set(NONE)
        
        #create an add_button, receiving the variable self._operator
        add_button = Radiobutton(frame, text="+", variable=self._operator, value = '+')
        add_button.pack(side= LEFT)
        #create an mult_button, receiving the variable self._operator
        mult_button = Radiobutton(frame, text="*", variable=self._operator, value = '*')
        mult_button.pack(side= LEFT)
        #create an sub_button, receiving the variable self._operator
        sub_button = Radiobutton(frame, text="-", variable=self._operator, value = '-')
        sub_button.pack(side= LEFT)
        #create an easy_button, receiving the variable self._level
        easy_button = Radiobutton(frame, text = 'easy', variable = self._level, value = 'easy', bg = 'green')
        easy_button.pack(side= LEFT)
        #create an medium_button, receiving the variable self._level
        medium_button = Radiobutton(frame, text = 'medium', variable = self._level, value = 'medium', bg = 'yellow')
        medium_button.pack(side= LEFT)
        #create an hard_button, receiving the variable self._level
        hard_button = Radiobutton(frame, text = 'hard', variable = self._level, value ='hard', bg = 'red')
        hard_button.pack(side= LEFT)
        
        #create the start button, making variable button1 and pack it
        #button1 command will lead to page 2 
        button1 = Button(self._root, text = 'START', command = self.page2, width = 10, height = 1, fg = 'green').pack()
        #create text for the equation to be under
        Label(window, text = 'SOLVE THE PROBLEM:').pack()
        
        #create self._question variable and set default var to StringVar()
        #as for self._answer, IntVar() 
        self._question = StringVar()
        self._answer = IntVar()
        #create label for the question, textvariable should be self._question
        self._question_label = Label(self._root, textvariable= self._question, width = 6).pack()
        
        #you will need the current score to be an IntVar(), set up a counter and default it to 0 for now
        self.current_score = IntVar()
        self.counter = 0
        #set the counter to the current score
        self.current_score.set(self.counter)
        #set label for cs(current score)
        cs_label = Label(frame, text = 'YOUR SCORE:').pack()
        cs_label = Label(frame, textvariable = self.current_score).pack()

        
    #create function page2, the page the game will lead to when you click START   
    def page2(self):
        frame = Frame(self._root)
        #for question, have it receive the operator and level, using the game file class to create the equation
        question = self._game.calculate(self._operator.get(), self._level.get())
        #assign question as list (easier to keep track of, better variable name at the moment)
        list = question
        #final question is the list from 0 to 3 (gives you the equation) and final answer is the last part list[-1] or list[4]
        finalquestion = list[0:3]
        finalanswer = list[-1]
        #set the self._answer to finalanswer and self._question to finalquestion
        self._answer.set(finalanswer)
        self._question.set(finalquestion)
        #create an input variable setting it IntVar() default
        self._input = IntVar()
        self._input.set('')
        #create an entry, receiving the input
        self.answer_input_label = Entry(self._root, width = 10, textvariable = self._input)
        self.answer_input_label.pack()
        #create the second button enter having it confirm whether or not the user submitted in the right answer
        button2 = Button(self._root, text = 'ENTER', command = self.answer, width = 10, fg = 'green')
        button2.pack()
        #create a forever loop
        while True:
            #assign speed of x and y
            speedX = -2
            speedY = 0
            #make the red_circle move towards the blue circle
            self.canvas.move(self.red_circle, speedX, speedY)
            #update it and assign time.sleep
            self.canvas.update()
            time.sleep(0.02)
            #create pos to find the coords for self.red_circle
            self.pos = self.canvas.coords(self.red_circle)
            #during the loop if pos[0] the first x is ever less or equal to 100, then end the game
            if self.pos[0] <= 100:
                self.canvas.delete(self.red_circle)
                label = Label(self._root, text = 'Too late, you died!').pack()
                self.answer_input_label.pack_forget()
                button2.pack_forget()
                exitbutton = Button(self._root, text = 'GOODBYE', command = self.exit, width = 10, fg = 'blue').pack()
                break

    #create an answer definition page   
    def answer(self):
        frame = Frame(self._root)
        #if the users answer is equal to the actual answer
        #delete the circle and replace it with a new one
        #add one point to the counter (for current score)
        #repeat the process
        if self._input.get() == self._answer.get():
            self.canvas.delete(self.red_circle)
            self.counter = self.counter
            self.counter = self.counter + 1
            self.current_score.set(self.counter)
            self._input.set('')
            self.red_circle = self.canvas.create_oval(600,250,650,300, fill = 'red')
            question = self._game.calculate(self._operator.get(), self._level.get())
            list = question
            finalquestion = list[0:3]
            finalanswer = list[-1]
            self._answer.set(finalanswer)
            self._question.set(finalquestion)
            while True:
                speedX = -2
                speedY = 0
                self.canvas.move(self.red_circle, speedX, speedY)
                self.canvas.update()
                time.sleep(0.02)
                self.pos = self.canvas.coords(self.red_circle)
                if self.pos[0] <= 100:
                    self.canvas.delete(self.red_circle)
                    label = Label(self._root, text = 'Too late, you died!').pack()
                    self.answer_input_label.pack_forget()
                    exitbutton = Button(self._root, text = 'GOODBYE', command = self.exit, width = 10, fg = 'blue').pack()
                    break
        #if the answer is incorrect, then delete the circle and end the game        
        else:
            self.canvas.delete(self.red_circle)
            label = Label(self._root, text = 'Wrong! Try again next time!').pack()
            self.answer_input_label.pack_forget()
            exitbutton = Button(self._root, text = 'GOODBYE', command = self.exit, width = 10, fg = 'blue').pack()
            
    #this is for the exitbutton, if they choose exit, then it will exit the game       
    def exit(self):
        sys.exit()
        

    
if __name__ == '__main__':
    root = Tk()
    root.title('MATH IS FUN!')
    app = Game(root)
    root.mainloop()
