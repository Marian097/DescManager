import tkinter as tk
from tkinter import messagebox
from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date
from tabel_iesiri import Iesiri




class IesiriGUI:
    def __init__(self):
        conexiune_cu_baza_de_date.connect_baza_de_date()
        self.optiune_iesiri = Iesiri(conexiune_bd_iesiri)
        self.root = tk.Tk()
        self.frame=tk.Tk()
        self.frame.title("DescManager")
        self.frame.geometry("600x300")
        self.root.title("DescManager")
        self.root.geometry("900x350")
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date


        self.creare_interfata()


    def creare_interfata(self):
        
        tk.Label(self.root, text="ID IESIRI: ").grid(row=0, column=0)
        self.entry_ID_IESIRI = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID_IESIRI.grid(row=0, column=1)

        tk.Label(self.root, text="COD CLIENT: ").grid(row=1, column=0)
        self.entry_COD_CLIENT = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_COD_CLIENT.grid(row=1, column=1)

        tk.Label(self.root, text="ID STOC: ").grid(row=2, column=0)
        self.entry_ID_STOC = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID_STOC.grid(row=2, column=1)

        tk.Label(self.root, text="UM/Unitate de masura: ").grid(row=3, column=0)
        self.entry_um = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_um.grid(row=3, column=1)

        tk.Label(self.root, text="Cantitate: ").grid(row=4, column=0)
        self.entry_cantitate = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_cantitate.grid(row=4, column=1)

        self.buton_adauga = tk.Button(self.root, text="Adauga vanzari", command=self.adauga)
        self.buton_adauga.grid(row=5, column=0, columnspan=2)

        self.buton_sterge = tk.Button(self.root, text="Sterge vanzari", command=self.sterge)
        self.buton_sterge.grid(row=6, column=0, columnspan=2)

        self.buton_afiseaza = tk.Button(self.root, text="Afiseaza vanzari", command=self.afiseaza_vanzari)
        self.buton_afiseaza.grid(row=7, column=0, columnspan=2)
        
        self.buton_inapoi=tk.Button(self.root, text="Inapoi", command=self.inapoi)
        self.buton_inapoi.grid(row=9, column=0, columnspan=2)
        
        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.grid(row=0, column=2, rowspan=5, padx=10)
        
        self.scroll_bar_orizontal=tk.Scrollbar(self.root, orient="horizontal", command=self.listbox.xview )
        self.scroll_bar_orizontal.grid(row=5, column=2, sticky="ew" )
    
        self.listbox_baza_de_date = tk.Listbox(self.root, height=9, width=40)
        self.listbox_baza_de_date.grid(row=0, column=5, rowspan=5, padx=10)
        
        scrollbar_verticala = tk.Scrollbar(self.root, orient="vertical", command=self.listbox_baza_de_date.yview)
        scrollbar_verticala.grid(row=0, column=6, rowspan=5, sticky="ns")
        
        self.scroll_bar_orizontal=tk.Scrollbar(self.root, orient="horizontal", command=self.listbox_baza_de_date.xview )
        self.scroll_bar_orizontal.grid(row=5, column=5, sticky="ew" )
        
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_clienti")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for row in rezultat:
            text=f"COD_CLIENT: -{row[0]} - Nume: -{row[1]} - Adresa: -{row[2]} -  Mail: -{row[3]}" 
            self.listbox_baza_de_date.insert(tk.END, text)
            
        self.listbox_3 = tk.Listbox(self.frame, height=15, width=90)
        self.listbox_3.grid(row=0, column=0, sticky=tk.NSEW)

        # Scrollbar verticală
        scrollbar_verticala = tk.Scrollbar(self.frame, orient="vertical", command=self.listbox_3.yview)
        scrollbar_verticala.grid(row=0, column=1, sticky=tk.NS)
        self.listbox_3.config(yscrollcommand=scrollbar_verticala.set)

        # Scrollbar orizontală
        scrollbar_orizontala = tk.Scrollbar(self.frame, orient="horizontal", command=self.listbox_3.xview)
        scrollbar_orizontala.grid(row=1, column=0, sticky=tk.EW)
        self.listbox_3.config(xscrollcommand=scrollbar_orizontala.set)
    

        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_stocuri")
        rezultat_2=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for row in rezultat_2:
            text_2=f"ID: {row[0]} - Denumire: {row[1]} - Furnizor: {row[2]} - UM: {row[3]} - Stoc: {row[4]} - Pret: {row[5]} - Total lei: {row[6]}"
            self.listbox_3.insert(tk.END, text_2)
        
    
        

    def adauga(self):
        ID_IESIRI=int(self.entry_ID_IESIRI.get())
        ID_STOC = int(self.entry_ID_STOC.get())
        COD_CLIENT = self.entry_COD_CLIENT.get()
        um= self.entry_um.get()
        cantitate = int(self.entry_cantitate.get())
        
        self.listbox.delete(0, tk.END)

        self.optiune_iesiri.adauga_iesiri(ID_IESIRI=ID_IESIRI, ID=ID_STOC, COD_CLIENT=COD_CLIENT, unitate_de_masura=um, iesiri=cantitate)
        text_element = f"{ID_IESIRI}:{ID_STOC}-{COD_CLIENT} - {um} - {cantitate}"
        self.listbox.insert(tk.END, text_element)
        
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "NIR adăugat cu succes!")
        


        

    def sterge(self):
        ID_IESIRI = int(self.entry_ID_IESIRI.get())
        ID_STOC=int(self.entry_ID_STOC.get())
        
        self.optiune_iesiri.sterge_iesiri(ID_IESIRI=ID_IESIRI, ID=ID_STOC)
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            
        messagebox.showinfo("Succes", "Comanda stearsa cu succes!")

    def afiseaza_vanzari(self):
        self.listbox.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_clienti.Nume, tabel_iesiri.* FROM tabel_clienti INNER JOIN tabel_iesiri ON tabel_clienti.COD_CLIENT = tabel_iesiri.Client")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text=f"Nume : {row[0]} - ID: {row[1]} - ID STOC : {row[2]} -  COD CLIENT: {row[3]} -  UM/Unitate de masura : {row[4]} - Cantitate: {row[5]} - Total vanzare: {row[6]}"
            self.listbox.insert(tk.END, text)
        self.sterge_text_casute()
        self.optiune_iesiri.afiseaza_iesiri()
    
    def inapoi(self):
        self.listbox.delete(0, tk.END)
            
    def sterge_text_casute(self):
        self.entry_ID_STOC.delete(0, tk.END)
        self.entry_ID_IESIRI.delete(0, tk.END)
        self.entry_COD_CLIENT.delete(0, tk.END)
        self.entry_um.delete(0, tk.END)
        self.entry_cantitate.delete(0, tk.END)
        
        
    def run(self):
        self.root.mainloop()
        conexiune_cu_baza_de_date.disconnect_baza_de_date()




if __name__ == "__main__":
    conexiune_bd_iesiri = Conexiune_cu_baza_de_date("test_baza_de_date.db")
    app = IesiriGUI()
    app.run()

conexiune_bd_iesiri = Conexiune_cu_baza_de_date("test_baza_de_date.db")





