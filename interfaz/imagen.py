import tkinter as tk

root = tk.Tk()
root.title("Interfaz con Botones")
root.geometry("600x500")


label = tk.Label(root, text="¡Hola Pvtos!",font=("Arial", 20))
label.pack()
img = tk.PhotoImage(file="logo2.png")
lbl_img = tk.Label(root, image = img)
lbl_img.pack()


root.mainloop()



