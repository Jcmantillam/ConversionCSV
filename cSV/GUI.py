from tkinter import *
from tkinter.ttk import *
from funtions import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('Nombre cliente', 'Apellidos cliente', 'Id cliente','Codigo del item', 'Descripcion del item', 'Cantidad del item', 'Precio unitario', 'Porcentaje descuento')
        tv.heading("#0", text='Numero Factura', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Nombre cliente', text='Nombre cliente')
        tv.column('Nombre cliente', anchor='center', width=100)
        tv.heading('Apellidos cliente', text='Apellidos cliente')
        tv.column('Apellidos cliente', anchor='center', width=100)
        tv.heading('Id cliente', text='Id cliente')
        tv.column('Id cliente', anchor='center', width=100)
        tv.heading('Codigo del item', text='Codigo del item')
        tv.column('Codigo del item', anchor='center', width=100)
        tv.heading('Descripcion del item', text='Descripcion del item')
        tv.column('Descripcion del item', anchor='center', width=100)
        tv.heading('Cantidad del item', text='Cantidad del item')
        tv.column('Cantidad del item', anchor='center', width=100)
        tv.heading('Precio unitario', text='Precio unitario')
        tv.column('Precio unitario', anchor='center', width=100)
        tv.heading('Porcentaje descuento', text='Porcentaje descuento')
        tv.column('Porcentaje descuento', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00','10:10', 'Ok'))
        self.treeview.insert('', 'end', text="Second", values=('10:00', '10:10', 'Ok'))

def main():
    init()
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()