import tkinter
from tkinter import messagebox, filedialog

def accion():
	print("Hola Mundo!")

def selecionar():
	print("La opcion selecionada es {}".format(opcion.get()))

def verificar():
	valor = check1.get()
	if(valor == 1):
		print("El check esta activado")
	else:
		print("El check esta desactivado")

def subirCV():
	rutafichero = filedialog.askopenfilename(title="Selecionar CV")
	print(rutafichero)

def preguntar():
	resultado = tkinter.messagebox.askquestion("Seguro?", "Seguro que quieres enviar esa informacion?")
	if(resultado == "yes"):
		enviar()

def enviar():
	tkinter.messagebox.showinfo("Enviar", "Enviado!")


raiz = tkinter.Tk()
raiz.title("Mi programa")

frame = tkinter.Frame(raiz)
frame.config(bg="blue", width=4000, height=3000)
frame.pack()

texto = "Hola mundo grafico en Python"
etiqueta = tkinter.Label(frame,text=texto)
etiqueta.config(fg="green", bg="lightgrey", font=("Cortana",30))
etiqueta.pack()

entrada = tkinter.Entry(frame)
entrada.config(justify="center")
entrada.pack()

textBox = tkinter.Text(frame)
textBox.config(width=20, height=10, font=("Verdana",15), padx=10, pady=10)
textBox.pack()

botonCV = tkinter.Button(frame, text="Subir CV", command=subirCV)
botonCV.pack()

boton = tkinter.Button(frame, text="Enviar", command=preguntar)
boton.pack()

opcion = tkinter.IntVar()
radioboton1 = tkinter.Radiobutton(frame, text="Opcion 1", variable=opcion, value=1, command=selecionar)
radioboton1.pack()

radioboton2 = tkinter.Radiobutton(frame, text="Opcion 2", variable=opcion, value=2, command=selecionar)
radioboton2.pack()

radioboton3 = tkinter.Radiobutton(frame, text="Opcion 3", variable=opcion, value=3, command=selecionar)
radioboton3.pack()

check1 = tkinter.IntVar()
checkboton1 = tkinter.Checkbutton(frame, text="Opcion 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
checkboton1.pack()

raiz.mainloop()