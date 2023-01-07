import random
from tkinter import *
from PIL import Image,ImageTk
# initialize GUI
root = Tk()

# Sit GUI Ditiles
root.title("Random Name")
root.geometry('300x450')
#sit icon image
root.iconbitmap("images/home1.ico")

#open image
b_image =Image.open("images/babay.png")
# Resize Image
resized = b_image.resize((300,200),Image.ANTIALIAS)

new_image =ImageTk.PhotoImage(resized)
# Set Image in lable
image_lable = Label(root, image=new_image)
image_lable.pack(padx=10,pady=10)

# Drop Down Menu
def show():
    # Open Files
    male_list = []
    with open("male.txt") as male_file:
        for male_name in male_file:
            male_name = male_name.strip()
            male_list.append(male_name[:1].upper()+male_name[1:])
            male = random.choice(male_list)
    female_list = []
    with open("female.txt") as female_file:
        for female_name in female_file:
            female_name = female_name.strip()
            female_list.append(female_name[:1].upper() + female_name[1:])
            female = random.choice(female_list)
    both_list = []
    with open("both.txt") as both_file:
        for both_name in both_file:
            both_name = both_name.strip()
            both_list.append(both_name[:1].upper() + both_name[1:])
            both = random.choice(both_list)
     #chek to valeu
    value_from_selection =clicked.get()
    if value_from_selection =="Male" or value_from_selection == "male":
        try:
            text.set(male)
        except :
            print("error")
    elif value_from_selection == "Female" or value_from_selection == "female":
        try:
            text.set(female)
        except:
            print("error")
    elif value_from_selection == "Both" or value_from_selection == "both":
        try:
            text.set(both)
        except:
            print("error")


    #Typing Code to open and show name

options =["Male","Female","Both"]
clicked =StringVar()
clicked.set(options[0])

Label(root, text="Choose Your Gander Please!", width=25, bg="white",
      font=("Helvetica", 13),
      bd=1).pack(pady=10)

drop = OptionMenu(root,clicked,*options)
drop.pack(pady=10,padx=10)


myButton = Button(root,text="Search",command=show,width=20,font=("Helcetica",10),bd=2,bg="green",fg="white").pack(pady=10)

text =StringVar()
text.set("Hello")
show_lable =Label(root,textvariable=text,font=("Helvetica",12)).pack(pady=20)

#Button(root,text="Exit",command=quit()).pack()



root.mainloop()
