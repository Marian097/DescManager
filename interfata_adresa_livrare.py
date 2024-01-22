import tkinter as tk
from tkinter import messagebox
from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date
from modul_adrese_livrari import Adresa_livrare




class AdresaLivrareGUI:
    def __init__(self):
        conexiune_cu_baza_de_date.connect_baza_de_date()
        self.optiune_adresa = Adresa_livrare(conexiune_bd_iesiri)
        self.root = tk.Tk()
        self.frame=tk.Tk()
        self.frame.title("DescManager")
        self.frame.geometry("600x300")
        self.root.title("DescManager")
        self.root.geometry("900x350")
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date


        self.creare_interfata()


    def creare_interfata(self):
        tk.Label(self.root, text="ID ADRESA: ").grid(row=0, column=0)
        self.entry_ID_ADRESA = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID_ADRESA.grid(row=0, column=1)

        tk.Label(self.root, text="COD CLIENT: ").grid(row=1, column=0)
        self.entry_COD_CLIENT = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_COD_CLIENT.grid(row=1, column=1)

        tk.Label(self.root, text="Adresa: ").grid(row=2, column=0)
        self.entry_adresa = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_adresa.grid(row=2, column=1)

        self.buton_adauga = tk.Button(self.root, text="Adauga adresa de livrare", command=self.adauga)
        self.buton_adauga.grid(row=3, column=0, columnspan=2)

        self.buton_sterge = tk.Button(self.root, text="Sterge adresa de livrare", command=self.sterge)
        self.buton_sterge.grid(row=4, column=0, columnspan=2)

        self.buton_afiseaza = tk.Button(self.root, text="Afiseaza adresa livrare", command=self.afiseaza_adresa)
        self.buton_afiseaza.grid(row=5, column=0, columnspan=2)
        
        self.buton_inapoi=tk.Button(self.root, text="Save", command=self.Save)
        self.buton_inapoi.grid(row=6, column=0, columnspan=2)
        
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
    

        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_clienti_adresa_livrare")
        rezultat_2=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for row in rezultat_2:
            text_2=f"ID_ADRESA: {row[0]} - ID_CLIENT: {row[1]} - Adresa de livrare: {row[2]} - Nume client: {row[3]}"
            self.listbox_3.insert(tk.END, text_2)
        
    
        

    def adauga(self):
        # ID_ADRESA, ID_CLIENT, adresa
        ID_ADRESA=int(self.entry_ID_ADRESA.get())
        ID_CLIENT = int(self.entry_COD_CLIENT.get())
        Adresa = self.entry_adresa.get()
        
        self.listbox.delete(0, tk.END)

        self.optiune_adresa.adauga_adresa(ID_ADRESA=ID_ADRESA, ID_CLIENT=ID_CLIENT, adresa=Adresa)
        text_element = f"ID_ADRESA: {ID_ADRESA}: ID CLIENT: -{ID_CLIENT}- Adresa de livrare: -{Adresa}"
        self.listbox.insert(tk.END, text_element)
        
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Adresa adaugata cu succes!")
        


        

    def sterge(self):
        ID_ADRESA = int(self.entry_ID_ADRESA.get())
        
        self.optiune_adresa.sterge_adresa(ID_ADRESA=ID_ADRESA)
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            
        messagebox.showinfo("Succes", "Stergere reusita!")

    def afiseaza_adresa(self):
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_adresa_livrare.*, tabel_clienti.Nume FROM tabel_adresa_livrare INNER JOIN tabel_clienti ON tabel_adresa_livrare.ID_CLIENT=tabel_clienti.COD_CLIENT;")
        livrare=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in livrare:
            text=f"ID_ADRESA : {row[0]} - ID_CLIENT: {row[1]} - Adresa de livrare : {row[2]} -  Nume client: {row[3]}"
            self.listbox.insert(tk.END, text)
        self.sterge_text_casute()
        self.optiune_adresa.afiseaza_livrare()
        
    def Save(self):
        ID_Adresa=int(self.entry_ID_ADRESA.get())
        self.optiune_adresa.salvare_client_adresa_livrare_bd(ID_ADRESA=ID_Adresa)
        messagebox.showinfo("Adresa salvata.")
                                                            
    def inapoi(self):
        self.listbox.delete(0, tk.END)
            
    def sterge_text_casute(self):
        self.entry_ID_ADRESA.delete(0, tk.END)
        self.entry_adresa.delete(0, tk.END)
        self.entry_COD_CLIENT.delete(0, tk.END)
        
    def run(self):
        self.root.mainloop()
        conexiune_cu_baza_de_date.disconnect_baza_de_date()




if __name__ == "__main__":
    conexiune_bd_iesiri = Conexiune_cu_baza_de_date("test_baza_de_date.db")
    app = AdresaLivrareGUI()
    app.run()

conexiune_bd_iesiri = Conexiune_cu_baza_de_date("test_baza_de_date.db")