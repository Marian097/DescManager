import tkinter as tk
from tkinter import messagebox
from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date
from refactoring_combustibil import Combustibil

conexiune_bd=Conexiune_cu_baza_de_date("test_baza_de_date.db")


class OptiuneCombustibilGUI:
    def __init__(self) -> None:
        conexiune_cu_baza_de_date.connect_baza_de_date()
        self.optiune_combustibil = Combustibil(conexiune_bd)
        self.root = tk.Tk()
        self.frame=tk.Tk()
        self.frame.geometry("600x280")
        self.frame.title("DescManager")
        self.root.title("DescManager")
        self.root.geometry("900x350")
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date


        self.creare_interfata()


    def creare_interfata(self):
        tk.Label(self.root, text="ID Combustibil: ").grid(row=0, column=0)
        self.entry_ID_COMBUSTIBIL = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID_COMBUSTIBIL.grid(row=0, column=1)

        tk.Label(self.root, text="ID Angajat: ").grid(row=1, column=0)
        self.entry_ID_ANGAJAT = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID_ANGAJAT.grid(row=1, column=1)

        tk.Label(self.root, text="Combustibil: ").grid(row=2, column=0)
        self.entry_combustibil = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_combustibil.grid(row=2, column=1)

        tk.Label(self.root, text="Pret: ").grid(row=3, column=0)
        self.entry_pret = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_pret.grid(row=3, column=1)

        tk.Label(self.root, text="Cantitate: ").grid(row=4, column=0)
        self.entry_cantitate = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_cantitate.grid(row=4, column=1)
        
        tk.Label(self.root, text="Data: ").grid(row=5, column=0)
        self.entry_data = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_data.grid(row=5, column=1)

        self.buton_adauga = tk.Button(self.root, text="Adauga", command=self.adauga)
        self.buton_adauga.grid(row=6, column=0, columnspan=2)

        self.buton_sterge = tk.Button(self.root, text="Sterge", command=self.sterge)
        self.buton_sterge.grid(row=7, column=0, columnspan=2)

        self.buton_actualizeaza = tk.Button(self.root, text="Actualizeaza", command=self.actualizeaza_combustibil)
        self.buton_actualizeaza.grid(row=8, column=0, columnspan=2)

        self.buton_afiseaza = tk.Button(self.root, text="Afiseaza", command=self.afiseaza_combustibil)
        self.buton_afiseaza.grid(row=9, column=0, columnspan=2)
        
        self.buton_refresh=tk.Button(self.root, text="Refresh", command=self.refresh_listbox)
        self.buton_refresh.grid(row=10, column=0, columnspan=2)
        
        self.buton_save=tk.Button(self.root, text="Save", command=self.Save)
        self.buton_save.grid(row=11, column=0, columnspan=2)
        
        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.grid(row=0, column=2, rowspan=5, padx=10)
        
        self.scroll_bar_orizontal=tk.Scrollbar(self.root, orient="horizontal", command=self.listbox.xview )
        self.scroll_bar_orizontal.grid(row=5, column=2, sticky="ew" )
        
        self.listbox_baza_de_date = tk.Listbox(self.root, height=9, width=40)
        self.listbox_baza_de_date.grid(row=0, column=5, rowspan=5, padx=10)
        
        scrollbar_verticala = tk.Scrollbar(self.root, orient="vertical", command=self.listbox_baza_de_date.yview)
        scrollbar_verticala.grid(row=0, column=6, rowspan=5, sticky="ns")
        
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID, Angajat FROM tabel_angajati")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
            
        for row in rezultat:
            text=f"ID: -{row[0]} - Angajat: -{row[1]}"
            self.listbox_baza_de_date.insert(tk.END, text)
            
        self.listbox_3 = tk.Listbox(self.frame, height=15, width=90)
        self.listbox_3.pack(pady=10, padx=10)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        
        self.listbox_3.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_3.yview)

        self.listbox_3.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        scrollbar_verticala = tk.Scrollbar(self.root, orient="vertical", command=self.listbox_baza_de_date.yview)
        scrollbar_verticala.grid(row=0, column=6, rowspan=5, sticky="ns")
        
        self.scroll_bar_orizontal=tk.Scrollbar(self.frame, orient="horizontal", command=self.listbox_3.xview )
        self.scroll_bar_orizontal.grid(row=4, column=0, sticky="ew" )
        
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_combustibil")
        rezultat_2=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for row in rezultat_2:
            text=f"ID: -{row[0]} - ID Angajat: -{row[1]} - Data: -{row[2]} -Combustibil: -{row[3]} - Pret: -{row[4]} - Cantitate: -{row[5]} - Total valoare: -{row[6]}"
            self.listbox_3.insert(tk.END, text)
    
        

    def adauga(self):
        ID_ANGAJAT=int(self.entry_ID_ANGAJAT.get())
        ID = int(self.entry_ID_COMBUSTIBIL.get())
        combustibil = self.entry_combustibil.get()
        pret = float(self.entry_pret.get())
        cantitate = int(self.entry_cantitate.get())
        data=self.entry_data.get()
        
        self.listbox.delete(0, tk.END)

        self.optiune_combustibil.adauga_combustibil(ID=ID, ID_ANGAJAT=ID_ANGAJAT, Data=data, combustibil=combustibil, pret=pret, cantitate=cantitate)
        text_element = f"{ID}:{ID_ANGAJAT}-{combustibil} - {pret} - {cantitate}"
        self.listbox.insert(tk.END, text_element)
        
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Adaugare reusita!")
        


        

    def sterge(self):
        ID_COMBUSTIBIL = int(self.entry_ID_COMBUSTIBIL.get())
        self.optiune_combustibil.sterge_combustibil(ID_COMBUSTIBIL=ID_COMBUSTIBIL)
        
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
        messagebox.showinfo("Succes", "Stergere reusita!")

    def actualizeaza_combustibil(self):
        self.listbox.delete(0, tk.END)
        ID_COMBUSTIBIL = int(self.entry_ID_COMBUSTIBIL.get())
        combustibil = self.entry_combustibil.get()
        pret = float(self.entry_pret.get())
        cantitate = int(self.entry_cantitate.get())
        data=self.entry_data.get()

        self.optiune_combustibil.actualizeaza_combustibil(ID_COMBUSTIBIL=ID_COMBUSTIBIL,Data=data, combustibil=combustibil, pret=pret, cantitate=cantitate)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID_COMBUSTIBIL}: {combustibil} - {pret} - {cantitate}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")

    def afiseaza_combustibil(self):
        self.listbox.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_combustibil.*, tabel_angajati.angajat FROM tabel_combustibil INNER JOIN tabel_angajati ON tabel_combustibil.IDAngajat = tabel_angajati.ID;")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text=f"ID Combustibil : {row[0]} - Angajat: {row[1]} - Combustibil : {row[2]} -  Pret: {row[3]} -  Cantitate : {row[4]} - Total lei: {row[5]} - Nume: {row[6]}" 
            self.listbox.insert(tk.END, text)
        self.sterge_text_casute()
        self.optiune_combustibil.afiseaza_combustibil()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def Save(self):
        ID=int(self.entry_ID_COMBUSTIBIL.get())
        self.optiune_combustibil.Adauga_combustibil_total_in_baza_de_date(ID=ID)
        messagebox.showinfo("Succes!", "Operatiune Reusita!")
        
        
    def refresh_listbox(self):    
        self.listbox_3.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_combustibil")
        rezultat_2=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for row in rezultat_2:
            text=f"ID: -{row[0]} - ID Angajat: -{row[1]} - Combustibil: -{row[2]} -Pret: -{row[3]} - Cantiate: -{row[4]} - Total valoare: -{row[5]} "
            self.listbox_3.insert(tk.END, text)
        
    
        
    def sterge_text_casute(self):
        self.entry_ID_ANGAJAT.delete(0, tk.END)
        self.entry_ID_COMBUSTIBIL.delete(0, tk.END)
        self.entry_combustibil.delete(0, tk.END)
        self.entry_pret.delete(0, tk.END)
        self.entry_cantitate.delete(0, tk.END)
        
        
    def run(self):
        self.root.mainloop()
        conexiune_cu_baza_de_date.disconnect_baza_de_date()




if __name__ == "__main__":
    conexiune_db = Conexiune_cu_baza_de_date("test_baza_de_date.db")
    app = OptiuneCombustibilGUI()
    app.run()

