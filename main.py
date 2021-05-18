#Pil Library for images. Use CMD in the search bar
from tkinter import *


class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="Darkolivegreen2"# to set it as background color for all the label widgets

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Welcome to the NCEA Level 2 Study Guide",bd=10, relief="ridge", font=("Ariel","25"))
        self.heading_label.grid(row=0, padx=225)
        #Doesn't work: self.heading_label.place(relx = 0.5, rely = 0.5, anchor = centre)
        self.var1=IntVar() #holds value of radio buttons
        root.configure(bg = background_color)
        
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","18"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=50) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame, font=("Ariel","18"))
        self.entry_box.grid(row=2,padx=20, pady=0)
        
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue",bd=10, relief="raised", font=("Ariel", "20", "bold"), compound = "c", bg="midnight blue", fg = "white", command=self.name_collection)
        self.continue_button.grid(row=3, padx=50, pady=200, sticky = E)
        

        #Exit button
        self.exit_button = Button(self.quiz_frame, text="Exit", bd=10, relief="raised", font=("Ariel", "20", "bold"), compound = "c", bg="Firebrick4", fg = "white", command=self.name_collection)
        self.exit_button.grid(row=3, padx=50, pady=200, sticky = W)
        
        
        #image
        #logo = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy()
        self.exit_button.destroy()
        self.quiz_frame.destroy()
        self.heading_label.destroy()
        self.user_label.destroy()#Destroy name frame then open the quiz runner
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
    
"""Whenever the Python interpreter reads a source file, it does two things:

it sets a few special variables like __name__, and then
it executes all of the code found in the file.

If you are running your module (the source file) as the main program, e.g. guiQuizPart1.py
the interpreter will assign the hard-coded string "__main__" to the __name__ variable

https://www.youtube.com/watch?v=sugvnHA7ElY

"""
