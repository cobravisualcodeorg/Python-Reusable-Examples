import tkinter as tk 


root = tk.Tk()


def Activo():

    print("HOLA")



boton1 = tk.Button(root,text="boton", command=Activo)

boton1.pack(pady=80)


root.mainloop()
