import tkinter as tk
from tkinter import messagebox
from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date
from modul_clienti import Client
conexiune_db_client= Conexiune_cu_baza_de_date("test_baza_de_date.db")

class ClientGUI:
    def __init__(self):
        conexiune_cu_baza_de_date.connect_baza_de_date()
        self.optiune_client = Client (conexiune_db_client)
        self.root = tk.Tk()
        self.root.title("DescManager")
        self.root.geometry("950x430")
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date


        self.creare_interfata()



    def creare_interfata(self):
        tk.Label(self.root, text="Cod de client: ").grid(row=0, column=0)
        self.entry_COD_CLIENT = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_COD_CLIENT.grid(row=0, column=1)

        tk.Label(self.root, text="Nume: ").grid(row=1, column=0)
        self.entry_nume = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_nume.grid(row=1, column=1)
        
        tk.Label(self.root, text="E-mail:").grid(row=2, column=0)
        self.entry_email=tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_email.grid(row=2, column=1)

        tk.Label(self.root, text="Adresa:").grid(row=3, column=0)
        self.entry_adresa = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_adresa.grid(row=3, column=1)

        self.buton_adauga = tk.Button(self.root, text="Adauga", command=self.adauga)
        self.buton_adauga.grid(row=4, column=0, columnspan=2)
        
        self.buton_actualizeaza_nume = tk.Button(self.root, text="Actualizeaza nume", command=self.actualizeaza_nume_client)
        self.buton_actualizeaza_nume.grid(row=5, column=0, columnspan=2)
        
        self.buton_actualizeaza_mail = tk.Button(self.root, text="Actualizeaza e-mail", command=self.actualizeaza_mail_client)
        self.buton_actualizeaza_mail.grid(row=6, column=0, columnspan=2)
               
        self.buton_actualizeaza_adresa = tk.Button(self.root, text="Actualizeaza adresa", command=self.actualizeaza_adresa_client)
        self.buton_actualizeaza_adresa.grid(row=7, column=0, columnspan=2)
        
        self.buton_sterge_client = tk.Button(self.root, text="Sterge client", command=self.sterge_client)
        self.buton_sterge_client.grid(row=8, column=0, columnspan=2)
        
        self.buton_afiseaza_client = tk.Button(self.root, text="Afiseaza client", command=self.afiseaza_client)
        self.buton_afiseaza_client.grid(row=9, column=0, columnspan=2)
        
        self.buton_inapoi=tk.Button(self.root, text="Inapoi", command=self.inapoi)
        self.buton_inapoi.grid(row=10, column=0, columnspan=2 )
        
        self.buton_refresh=tk.Button(self.root, text="Refresh", command=self.refresh_listbox)
        self.buton_refresh.grid(row=11, column=0, columnspan=2)
        
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
        
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_clienti")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
            
        for row in rezultat:
            text=f"COD_CLIENT: {row[0]} - Nume: {row[1]} - Mail : {row[2]} -  Adresa: {row[3]}" 
            self.listbox_baza_de_date.insert(tk.END, text)
       

    def adauga(self):
        COD_CLIENT=int(self.entry_COD_CLIENT.get())
        nume=self.entry_nume.get()
        mail=self.entry_email.get()
        adresa=self.entry_adresa.get()
        
        self.listbox.delete(0, tk.END)
        
        self.optiune_client.adauga_clienti(COD_CLIENT=COD_CLIENT, nume=nume, email=mail, adresa=adresa)
        text_element = f"{COD_CLIENT}: {nume} - {mail} - {adresa}"
        self.listbox.insert(tk.END, text_element)
        
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Adaugare reusita!")
        
        
    def sterge_client(self):
        COD_CLIENT=int(self.entry_COD_CLIENT.get())
        self.optiune_client.sterge_client(COD_CLIENT=COD_CLIENT)
        
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
        messagebox.showinfo("Succes", "Stergere reusita!")

    def actualizeaza_nume_client(self):
        self.listbox.delete(0, tk.END)
        COD_CLIENT = int(self.entry_COD_CLIENT.get())
        nume = self.entry_nume.get()

        self.optiune_client.actualizeaza_nume(COD_CLIENT=COD_CLIENT, nume=nume)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{COD_CLIENT}: {nume}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_mail_client(self):
        self.listbox.delete(0, tk.END)
        COD_CLIENT= int(self.entry_COD_CLIENT.get())
        mail = self.entry_email.get()

        self.optiune_client.actualizeaza_email(COD_CLIENT=COD_CLIENT, email=mail)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{COD_CLIENT}: {mail}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_adresa_client(self):
        self.listbox.delete(0, tk.END)
        COD_CLIENT= int(self.entry_COD_CLIENT.get())
        adresa=self.entry_adresa.get()
        self.optiune_client.actualizeaza_adresa(COD_CLIENT=COD_CLIENT, adresa=adresa)
        selected_index = self.listbox.curselection()
        if selected_index:
            text_element = f" {COD_CLIENT}: {adresa}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        

    def afiseaza_client(self):
        self.listbox.delete(0, tk.END)
        COD_CLIENT=int(self.entry_COD_CLIENT.get())
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_clienti WHERE COD_CLIENT=?", (COD_CLIENT, ))
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
             text=f"COD_CLIENT: {row[0]} - Nume: {row[1]} - Adresa : {row[2]} -  Mail: {row[3]}" 
             self.listbox.insert(tk.END, text)
        self.sterge_text_casute()
        self.optiune_client.afiseaza(COD_CLIENT)
        
    def refresh_listbox(self):    
        self.listbox_baza_de_date.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_clienti")
        rezultat = self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text=f"COD_CLIENT: {row[0]} - Nume: {row[1]} - Email : {row[2]} -  Adresa: {row[3]}"
            self.listbox_baza_de_date.insert(tk.END, text)
        
    def sterge_text_casute(self):
        self.entry_COD_CLIENT.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_nume.delete(0, tk.END)
        self.entry_adresa.delete(0, tk.END)
        
    def inapoi(self):
        self.listbox.delete(0, tk.END)
        
    def run(self):
        self.root.mainloop()
        conexiune_cu_baza_de_date.disconnect_baza_de_date()




if __name__ == "__main__":
    conexiune_db_client= Conexiune_cu_baza_de_date("test_baza_de_date.db")
    app = ClientGUI()
    app.run()