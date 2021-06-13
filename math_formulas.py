# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:32:20 2021

@author: Atharva
"""

from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title('Math formulas')
window.geometry("1000x800")
window.iconbitmap("C:/Users/athar/Desktop/Atharva/code/CodeDay_2021/icon.ico")
window.configure(bg='black')

#Update the listbox
def update(data):
    #Clear the listbox
    my_list.delete(0, END)
    #Add formulas
    for item in data:
        my_list.insert(END, item)
        
# Update entry box listbox clicked
def fillout(e):
    #Delete whatever is in the entry box
    my_entry.delete(0, END)
    
    #Add clicked list item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))
    
# Create function to check entry vs listbox
def check(e):
    # grab what was typed
    typed = my_entry.get()
    
    if typed == "":
        data = formulas
    else:
        data = []
        for item in formulas:
            if typed.lower() in item.lower():
                data.append(item)
                
    # update our listbox with selected items
    update(data)
    
def myClick():
    for item in formulas:
        if item == my_entry.get():
            my_list.delete(0, END)
            for i in formulas_dict.keys():
                if my_entry.get() == i:
                    global my_label2
                    img1 = Image.open(formulas_dict[i])
                    test = ImageTk.PhotoImage(img1)
                    my_label2 = Label(image=test)
                    my_label2.image = test
                    my_label2.place(x=21, y=125)
                    

def handle_click(event):
    try:
        my_label2.destroy()
        my_entry.delete(0, END)
        update(formulas)
        check(e)
    except NameError:
        return
    
#create a label
my_label = Label(window, text="Math Formula Finder", font=("helvetica", 30), fg="white", bg="black")
my_label.pack(pady=15)

#Create a button
my_button = Button(window, text="Search ", bg="white", font=("helvetica", 14), fg="black", width=5, height=0, command=myClick)
my_button.place(x=915, y=80)

#Create an entry box
my_entry = Entry(window, font=("Helvetica", 20), width=58)
my_entry.place(x=20, y=80)

#Create a listbox
my_list = Listbox(window, font=("Helvetica", 25), width=53, height=24)
my_list.pack(pady=50)

#Create a list
formulas = ['Area of a Circle', 'Area of a Cube', 'Area of a Rectangle', 'Area of a Rhombus', 'Area of a Square', 
            'Area of a Trapezoid', 'Area of a Triangle', 'Equation of a Circle', 'Combination Formula', 
            'Complex Numbers', 'Distance Formula', 'Law of Cosines', 'Law of Sines', 'Permutation Formula', 
            'Probability Density', 'Pythagorean Theorem', 'Quadratic Formula', 'Slope Intercept Form', 
            'Surface Area of a Rectangular Prism', 'Surface Area of a Sphere', 'Volume of a Triangular Prism', 
            'Volume of a Pyramid', 'Volume of a Rectangular Prism']

#Create a dictionary
BASEDIR = 'C:\\Users\\athar\\Desktop\\Atharva\\code\\CodeDay_2021\\Formulas\\'

# Formula List
formulas_dict = {'Area of a Circle': BASEDIR + "AreaCircle.jpg", 'Area of a Cube': BASEDIR + 'AreaCube.png', 
            'Area of a Rectangle': BASEDIR + 'AreaRectangle.jpg', 'Area of a Rhombus': BASEDIR + 'AreaRhombus.png', 
            'Area of a Square': BASEDIR + 'AreaSquare.jpg', 'Area of a Trapezoid': BASEDIR + 'AreaTrapezoid.png', 
            'Area of a Triangle': BASEDIR + 'AreaTriangle.png', 'Equation of a Circle': BASEDIR + 'CircleEquation.png', 
            'Combination Formula': BASEDIR + 'CombinationFormula.png', 'Complex Numbers': BASEDIR + 'ComplexNumber.jpg', 
            'Distance Formula': BASEDIR + 'Distance.png', 'Law of Cosines': BASEDIR + 'LawCosines.png', 'Law of Sines': BASEDIR + 'LawSines.png', 
            'Permutation Formula': BASEDIR + 'PermutationFormula.jpg', 'Probability Density': BASEDIR + 'ProbabilityDensity.jpg', 
            'Pythagorean Theorum': BASEDIR + 'PythagoreanTheorum.png', 'Quadratic Formula': BASEDIR + 'QuadraticFormula.png', 
            'Slope Intercept Form': BASEDIR + 'SlopeInterceptForm.png', 
            'Surface Area of a Rectangular Prism': BASEDIR + 'SurfaceAreaRectangularPrism.jpg', 
            'Surface Area of a Sphere': BASEDIR + 'SurfaceAreaSphere.jpg', 
            'Volume of a Triangular Prism': BASEDIR + 'VolmeTriangularPrism.png', 'Volume of a Pyramid': BASEDIR + 'VolumePyramid.jpg', 
            'Volume of a Rectangular Prism': BASEDIR + 'VolumeRectangularPrism.png'}

#Add the formulas to our list
update(formulas)

#Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

#Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)
my_entry.bind("<1>", handle_click)


window.mainloop()
