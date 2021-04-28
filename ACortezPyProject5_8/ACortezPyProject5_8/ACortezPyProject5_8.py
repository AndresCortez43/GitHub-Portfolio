import tkinter as tk
import tkinter.font as tkFont

#Create tkinter object
app = tk.Tk()
#Set up app title
app.winfo_toplevel().title("Python GUI Lab 5_8")

app.geometry("640x480")

fontStyle = tkFont.Font(family="Times New Roman", size=20)
labelExample = tk.Label(app, text="The system is idle", font = fontStyle)



def SystemOn():

     #Change label text
    labelExample.configure(text = "System Running")

    


def SystemOff():
      #Change label text
    labelExample.configure(text = "System Off")




pixelVirtual = tk.PhotoImage(width=1, height=1)
labelExample.pack(side=tk.TOP)
systemOnButton = tk.Button(app, text = "System On", bg = "gray", fg="white", image = pixelVirtual, width = 200, height = 100, compound="c", command=SystemOn)
systemOnButton.place(x=100, y=400)


systemOffButton = tk.Button(app, text = "System Off", bg = "gray", fg="white", image = pixelVirtual, width = 200, height = 100, compound="c", command=SystemOff)
systemOffButton.place(x=340, y=400)


exitButton = tk.Button(app, text="EXIT", command=app.quit)
exitButton.pack(side=tk.BOTTOM)

app.mainloop()


