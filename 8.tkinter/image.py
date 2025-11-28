from tkinter import *
root=Tk()

canvas=Canvas(root,width=300,height=200)
canvas.pack()

img=PhotoImage(file="dog.gif")
canvas.create_image(20,20,anchor="nw",image=img)

root.mainloop()
