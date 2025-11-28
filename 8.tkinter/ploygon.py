from tkinter import *
root=Tk()

canvas=Canvas(root,width=300,height=200)
canvas.pack()
canvas.create_polygon(10,10,200,150,100,180,fill="blue")
                      
root.mainloop()
