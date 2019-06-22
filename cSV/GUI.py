from tkinter import *
from tkinter.ttk import *
from funtions import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror



class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.master.title("Caraga de facturas CSV")
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Cargar CSV", command=self.load_file)
        fileMenu.add_command(label="Guardar en BD", command=self.save)
        fileMenu.add_command(label="Cargar datos de BD", command=self.load_table)
        fileMenu.add_command(label="Borrar BD(Es solo para pruebas)", command=self.delete_BD)
        menubar.add_cascade(label="Archivo", menu=fileMenu)
        self.CreateUI()
        self.grid(row=1, column=0, sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J')
        tv.heading("#0", text='', anchor='w')
        tv.column("#0", anchor="w", width=1)
        tv.heading('A', text='A')
        tv.column('A', anchor='center', width=100)
        tv.heading('B', text='B')
        tv.column('B', anchor='center', width=100)
        tv.heading('C', text='C')
        tv.column('C', anchor='center', width=100)
        tv.heading('D', text='D')
        tv.column('D', anchor='center', width=100)
        tv.heading('E', text='E')
        tv.column('E', anchor='center', width=100)
        tv.heading('F', text='F')
        tv.column('F', anchor='center', width=100)
        tv.heading('G', text='G')
        tv.column('G', anchor='center', width=100)
        tv.heading('H', text='H')
        tv.column('H', anchor='center', width=100)
        tv.heading('I', text='I')
        tv.column('I', anchor='center', width=100)
        tv.heading('J', text='J')
        tv.column('J', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def load_file(self):
        fname = askopenfilename(filetypes=(("CSV", "*.csv"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*")))
        if fname:
            try:
                info = load(fname)
                count = 0
                for i in self.treeview.get_children():
                    self.treeview.delete(i)
                for r in info:
                    count += 1
                    print(r)
                    self.treeview.insert('', 'end', text='', values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
            except:
                showerror("Abrir archivo CSV", "No se pudeo abrir el archivo \n'%s'" % fname)
            return

    def save(self):
        values = []
        try:
            content = read_jason()
            for c in content:
                values.append(c)
        except:
            pass
        count =  0
        if len(values) == 0:
            values.append(['Numero de factura', 'Nombre del cliente', 'Apellido del cliente', 'Identificacion del cliente','Codigo del item', 'Descripcion del item', 'Cantidad de items', 'Precio unitario', 'Porcentaje de descuento', 'precio total'])

        for i in self.treeview.get_children():
            if count>0:
                vector = self.treeview.item(i)['values']
                try:
                    cantidad = vector[6]
                    precio = vector[7]
                    descuento = vector[8]
                    precio_total = float(cantidad) * float(precio)
                    precio_total = precio_total - precio_total * (float(descuento)/100)
                    vector.append(precio_total)
                    values.append(vector)
                except:
                    showerror("Error de carga", "No fue posible cargar los datos de la fila \n'%s'" % count)
            count += 1

        write_jason(values)

    def load_table(self):
        try:
            content = read_jason()
            count = 0
            for i in self.treeview.get_children():
                self.treeview.delete(i)
            for i in content:
                print(i)
                count += 1
                self.treeview.insert('', 'end', text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9]))
        except:
            showerror("No hay datos", "No se han encontrado datos en la BD, porfavor carge datos antes de realizar la consulta")

    def delete_BD(self):
        write_jason(None)
        showerror("Borrar datos","Tabla borrada")

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()