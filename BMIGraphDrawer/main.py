import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt

name_list = []
bmi_list = []

def calculateBMI():
    try:
        height = heightEntry.get()
        weight = weightEntry.get()
        return float(weight) / (float(height) ** 2)
    except:
        messagebox.showinfo(title="Error!", message="Enter valid values")

def addPeople():
    if len(nameEntry.get())>0 and len(heightEntry.get())>0 and len(weightEntry.get())>0:
        name_list.append(nameEntry.get())
        bmi_list.append(calculateBMI())
        nameEntry.delete(0, tkinter.END)
        heightEntry.delete(0, tkinter.END)
        weightEntry.delete(0, tkinter.END)

def showGraph():
    if len(name_list) > 0 and len(bmi_list) > 0:
        plt.scatter(name_list, bmi_list, color=['red' if not (18.5 <= bmi < 25) else 'blue' for bmi in bmi_list], marker='o')
        plt.xlabel('Name')
        plt.ylabel('BMI')
        plt.title('BMI Graph')
        plt.grid(True)
        # show bmi values on the top of the points
        for i, bmi in enumerate(bmi_list):
            plt.annotate(f"{bmi:.2f}", (name_list[i], bmi + 0.10), ha='center')
        plt.show()

window = tkinter.Tk()
window.title("BMI Graph")
window.config(padx=0, pady=12)
window.geometry("250x125")
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
window.geometry()

FONT = ("Arial", 10, "bold")

nameLabel = tkinter.Label(text="Enter Name : ",font=FONT)
heightLabel = tkinter.Label(text=" Enter Height : ",font=FONT)
weightLabel = tkinter.Label(text="  Enter Weight : ",font=FONT)

nameEntry = tkinter.Entry()
heightEntry = tkinter.Entry()
weightEntry = tkinter.Entry()

nameLabel.grid(column=0,row=0)
heightLabel.grid(column=0,row=1)
weightLabel.grid(column=0,row=2)
nameEntry.grid(column=1,row=0)
heightEntry.grid(column=1,row=1)
weightEntry.grid(column=1,row=2)

addButton = tkinter.Button(text="Add",cursor="hand2",width=8,command=addPeople)
graphButton = tkinter.Button(text="Graph",cursor="hand2",width=8,command=showGraph)

addButton.place(x=50,y=75)
graphButton.place(x=130,y=75)

window.mainloop()