import tkinter as tk
from tkinter import messagebox
from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date
from modul_tabel_stocuri import Intrari

conexiune= Conexiune_cu_baza_de_date("test_baza_de_date.db")
class IntrariGUI:
    def __init__(self):
        conexiune_cu_baza_de_date.connect_baza_de_date()
        self.optiune_intrari = Intrari(conexiune)
        self.root = tk.Tk()
        self.root.title("DescManager")
        self.root.geometry("950x460")
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date


        self.creare_interfata()


    def creare_interfata(self):
        tk.Label(self.root, text="ID: ").grid(row=0, column=0)
        self.entry_ID = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID.grid(row=0, column=1)

        tk.Label(self.root, text="Denumire: ").grid(row=1, column=0)
        self.entry_denumire = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_denumire.grid(row=1, column=1)
        
        tk.Label(self.root, text="Furnizor").grid(row=2, column=0)
        self.entry_furnizor=tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_furnizor.grid(row=2, column=1)

        tk.Label(self.root, text="UM/Unitate de masura: ").grid(row=3, column=0)
        self.entry_um = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_um.grid(row=3, column=1)

        tk.Label(self.root, text="Pret: ").grid(row=4, column=0)
        self.entry_pret = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_pret.grid(row=4, column=1)

        tk.Label(self.root, text="Cantitate: ").grid(row=5, column=0)
        self.entry_cantitate = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_cantitate.grid(row=5, column=1)

        self.buton_adauga = tk.Button(self.root, text="Adauga", command=self.adauga)
        self.buton_adauga.grid(row=6, column=0, columnspan=2)
        
        self.buton_actualizeaza = tk.Button(self.root, text="Actualizeaza stoc", command=self.actualizeaza_stocuri)
        self.buton_actualizeaza.grid(row=7, column=0, columnspan=2)
        
        self.buton_actualizeaza = tk.Button(self.root, text="Actualizeaza pret", command=self.actualizeaza_pret_stocuri)
        self.buton_actualizeaza.grid(row=8, column=0, columnspan=2)
               
        self.buton_actualizeaza = tk.Button(self.root, text="Actualizeaza denumire", command=self.actualizeaza_denumire_stoc)
        self.buton_actualizeaza.grid(row=9, column=0, columnspan=2)
        
        self.buton_actualizeaza = tk.Button(self.root, text="Actualizeaza furnizor", command=self.actualizeaza_furnizor_stoc)
        self.buton_actualizeaza.grid(row=10, column=0, columnspan=2)
        
        self.buton_actualizeaza = tk.Button(self.root, text="Actualizeaza UM", command=self.actualizeaza_um_stocuri)
        self.buton_actualizeaza.grid(row=11, column=0, columnspan=2)

        self.buton_sterge = tk.Button(self.root, text="Sterge", command=self.sterge)
        self.buton_sterge.grid(row=12, column=0, columnspan=2)

        self.buton_afiseaza = tk.Button(self.root, text="Afiseaza", command=self.afiseaza_stocuri)
        self.buton_afiseaza.grid(row=13, column=0, columnspan=2)
        
        self.buton_refresh=tk.Button(self.root, text="Refresh", command=self.refresh_listbox)
        self.buton_refresh.grid(row=14, column=0, columnspan=2)
        
        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.grid(row=0, column=2, rowspan=5, padx=10)
        
        self.scroll_bar_orizontal=tk.Scrollbar(self.root, orient="horizontal", command=self.listbox.xview )
        self.scroll_bar_orizontal.grid(row=5, column=2, sticky="ew" )
        
        scrollbar_verticala = tk.Scrollbar(self.root, orient="vertical", command=self.listbox.yview)
        scrollbar_verticala.grid(row=0, column=3, rowspan=5, sticky="ns")
        
        self.listbox_baza_de_date = tk.Listbox(self.root, height=9, width=40)
        self.listbox_baza_de_date.grid(row=0, column=5, rowspan=5, padx=10)
        
        scrollbar_verticala = tk.Scrollbar(self.root, orient="vertical", command=self.listbox_baza_de_date.yview)
        scrollbar_verticala.grid(row=0, column=6, rowspan=5, sticky="ns")
        
        self.scroll_bar_orizontal=tk.Scrollbar(self.root, orient="horizontal", command=self.listbox_baza_de_date.xview )
        self.scroll_bar_orizontal.grid(row=5, column=5, sticky="ew" )
        
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_stocuri")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
            
        for row in rezultat:
            text=f"ID: {row[0]} - Denumire: {row[1]} - Furnizor : {row[2]} -  UM: {row[3]} -  Stoc : {row[4]} - Pret: {row[5]} - Total lei: {row[6]}" 
            self.listbox_baza_de_date.insert(tk.END, text)
       

    def adauga(self):
        ID = int(self.entry_ID.get())
        denumire= self.entry_denumire.get()
        furnizor=self.entry_furnizor.get()
        UM=self.entry_um.get()
        pret = float(self.entry_pret.get())
        cantitate = int(self.entry_cantitate.get())
        
        self.listbox.delete(0, tk.END)

        self.optiune_intrari.adauga_intrari(ID=ID, denumire=denumire, furnizor=furnizor, unitate_de_masura=UM,  pret=pret, stoc=cantitate)
        text_element = f"{ID}: {denumire} - {furnizor} - {UM} - {pret} - {cantitate}"
        self.listbox.insert(tk.END, text_element)
        
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Adaugare reusita!")
        
        
    def sterge(self):
        ID= int(self.entry_ID.get())
        self.optiune_intrari.sterge_intrare(ID=ID)
        
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
        messagebox.showinfo("Succes", "Stergere reusita!")

    def actualizeaza_stocuri(self):
        self.listbox.delete(0, tk.END)
        ID = int(self.entry_ID.get())
        cantitate = int(self.entry_cantitate.get())

        self.optiune_intrari.actualizeaza_stoc(ID=ID, stoc=cantitate)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID}: {cantitate} - {cantitate}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_pret_stocuri(self):
        self.listbox.delete(0, tk.END)
        ID = int(self.entry_ID.get())
        pret_nou = int(self.entry_pret.get())

        self.optiune_intrari.actualizeaza_pret(ID=ID, pret_nou=pret_nou)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID}: {pret_nou}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_denumire_stoc(self):
        self.listbox.delete(0, tk.END)
        ID = int(self.entry_ID.get())
        denumire=self.entry_denumire.get()
        self.optiune_intrari.actualizeaza_denumire(ID=ID, denumire=denumire)
        selected_index = self.listbox.curselection()
        if selected_index:
            text_element = f"{ID}: {denumire}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_um_stocuri(self):
        self.listbox.delete(0, tk.END)
        ID = int(self.entry_ID.get())
        um=self.entry_um.get()
        self.optiune_intrari.actualizeaza_um(ID=ID, unitate_de_masura=um)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID}: {um}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_furnizor_stoc(self):
        self.listbox.delete(0, tk.END)
        ID = int(self.entry_ID.get())
        furnizor=self.entry_furnizor.get()

        self.optiune_intrari.actualizeaza_furnizor(ID=ID, furnizor=furnizor)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID}: {furnizor}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")

    def afiseaza_stocuri(self):
        self.listbox.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_stocuri")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text=f"ID: {row[0]} - Denumire: {row[1]} - Furnizor : {row[2]} -  UM: {row[3]} -  Stoc : {row[4]} - Pret: {row[5]} - Total lei: {row[6]}" 
            self.listbox.insert(tk.END, text)
        self.sterge_text_casute()
        self.optiune_intrari.afisare_intrari()
        
        
    def refresh_listbox(self):    
        self.listbox_baza_de_date.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_stocuri")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text=f"ID: {row[0]} - Denumire: {row[1]} - Furnizor : {row[2]} -  UM: {row[3]} -  Stoc : {row[4]} - Pret: {row[5]} - Total lei: {row[6]}" 
            self.listbox_baza_de_date.insert(tk.END, text)
       
        
    def sterge_text_casute(self):
        self.entry_ID.delete(0, tk.END)
        self.entry_denumire.delete(0, tk.END)
        self.entry_furnizor.delete(0, tk.END)
        self.entry_pret.delete(0, tk.END)
        self.entry_cantitate.delete(0, tk.END)
        
        
    def run(self):
        self.root.mainloop()
        conexiune_cu_baza_de_date.disconnect_baza_de_date()




if __name__ == "__main__":
    conexiune= Conexiune_cu_baza_de_date("test_baza_de_date.db")
    app = IntrariGUI()
    app.run()