import tkinter as tk
from tkinter import messagebox
from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date
from refactoring_angajati import Angajat


class AngajatGUI:
    def __init__(self):
        conexiune_cu_baza_de_date.connect_baza_de_date()
        self.optiune_angajat = Angajat (conexiune_db_angajat)
        self.root = tk.Tk()
        self.root.title("DescManager")
        self.root.geometry("950x430")
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date


        self.creare_interfata()



    def creare_interfata(self):
        tk.Label(self.root, text="ID: ").grid(row=0, column=0)
        self.entry_ID = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_ID.grid(row=0, column=1)

        tk.Label(self.root, text="Nume: ").grid(row=1, column=0)
        self.entry_nume = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_nume.grid(row=1, column=1)
        
        tk.Label(self.root, text="Calificare: ").grid(row=2, column=0)
        self.entry_calificare=tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_calificare.grid(row=2, column=1)

        tk.Label(self.root, text="Adresa: ").grid(row=3, column=0)
        self.entry_adresa = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_adresa.grid(row=3, column=1)
        
        tk.Label(self.root, text="CNP: ").grid(row=4, column=0)
        self.entry_cnp = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_cnp.grid(row=4, column=1)
        
        tk.Label(self.root, text="Contract: ").grid(row=5, column=0)
        self.entry_contract = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry_contract.grid(row=5, column=1)


        self.buton_adauga = tk.Button(self.root, text="Adauga angajat", command=self.adauga)
        self.buton_adauga.grid(row=6, column=0, columnspan=2)
        
        self.buton_actualizeaza_nume = tk.Button(self.root, text="Actualizeaza nume", command=self.actualizeaza_nume_angajat)
        self.buton_actualizeaza_nume.grid(row=7, column=0, columnspan=2)
        
        self.buton_actualizeaza_cnp=tk.Button(self.root, text="Actualizeaza CNP", command=self.actualizeaza_cnp_angajat)
        self.buton_actualizeaza_cnp.grid(row=8, column=0, columnspan=2)
        
        self.buton_actualizeaza_calificare = tk.Button(self.root, text="Actualizeaza calificare", command=self.actualizeaza_calificare_angajat)
        self.buton_actualizeaza_calificare.grid(row=8, column=0, columnspan=2)
               
        self.buton_actualizeaza_adresa = tk.Button(self.root, text="Actualizeaza adresa", command=self.actualizeaza_adresa_angajat)
        self.buton_actualizeaza_adresa.grid(row=9, column=0, columnspan=2)
        
        self.buton_actualizeaza_adresa = tk.Button(self.root, text="Actualizeaza Contract", command=self.actualizeaza_contract_angajat)
        self.buton_actualizeaza_adresa.grid(row=10, column=0, columnspan=2)
        
        self.buton_sterge_angajat = tk.Button(self.root, text="Sterge angajat", command=self.sterge)
        self.buton_sterge_angajat.grid(row=11, column=0, columnspan=2)
        
        self.buton_afiseaza_angajat = tk.Button(self.root, text="Afiseaza angajat dupa ID", command=self.afiseaza_angajat_dupa_id)
        self.buton_afiseaza_angajat.grid(row=12, column=0, columnspan=2)
        
        self.buton_refresh = tk.Button(self.root, text="Refresh", command=self.refresh_listbox)
        self.buton_refresh.grid(row=13, column=0, columnspan=2)
        
        self.buton_inapoi=tk.Button(self.root, text="Inapoi", command=self.inapoi)
        self.buton_inapoi.grid(row=14, column=0, columnspan=2 )
        
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
        
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_angajati")
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
            
        for row in rezultat:
            text=f"ID: {row[0]} - Nume: {row[1]} -Calificare: {row[2]} - Adresa : {row[3]} -  CNP: {row[4]} - Contract: {row[5]}" 
            self.listbox_baza_de_date.insert(tk.END, text)
       

    def adauga(self):
        ID=int(self.entry_ID.get())
        nume=self.entry_nume.get()
        contract=self.entry_contract.get()
        adresa=self.entry_adresa.get()
        cnp=self.entry_cnp.get()
        calificare=self.entry_calificare.get()
        
        self.listbox.delete(0, tk.END)
        
        self.optiune_angajat.adauga_angajat(nume=nume, ID=ID, calificare=calificare, adresa=adresa, cnp=cnp, contract=contract)
        text_element = f"{ID}: {nume} - {cnp} - {calificare} - {adresa} - {contract}"
        self.listbox.insert(tk.END, text_element)
        
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Angajat adaugat!")
        
        
    def sterge(self):
        ID=int(self.entry_ID.get())
        self.optiune_angajat.sterge_angajat(ID=ID)
        
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Angajat sters!")

    def actualizeaza_nume_angajat(self):
        self.listbox.delete(0, tk.END)
        ID = int(self.entry_ID.get())
        nume = self.entry_nume.get()

        self.optiune_angajat.actualizeaza_nume(ID=ID, nume_nou=nume)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID}: {nume}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_contract_angajat(self):
        self.listbox.delete(0, tk.END)
        ID= int(self.entry_ID.get())
        contract = self.entry_contract.get()

        self.optiune_angajat.actualizeaza_contract(ID=ID, contract=contract)
        selected_index = self.listbox.curselection()
        
        if selected_index:
            text_element = f"{ID}: {contract}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_adresa_angajat(self):
        self.listbox.delete(0, tk.END)
        ID= int(self.entry_ID.get())
        adresa=self.entry_adresa.get()
        self.optiune_angajat.actualizeaza_adresa(ID=ID, adresa=adresa)
        selected_index = self.listbox.curselection()
        if selected_index:
            text_element = f" {ID}: {adresa}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_cnp_angajat(self):
        self.listbox.delete(0, tk.END)
        ID= int(self.entry_ID.get())
        cnp=self.entry_cnp.get()
        self.optiune_angajat.actualizeaza_cnp(ID=ID, cnp=cnp)
        selected_index = self.listbox.curselection()
        if selected_index:
            text_element = f" {ID}: {cnp}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        
    def actualizeaza_calificare_angajat(self):
        self.listbox.delete(0, tk.END)
        ID= int(self.entry_ID.get())
        calificare=self.entry_calificare.get()
        self.optiune_angajat.actualizeaza_calificare(ID=ID, calificare=calificare)
        selected_index = self.listbox.curselection()
        if selected_index:
            text_element = f" {ID}: {calificare}"
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, text_element)
        self.sterge_text_casute()
        messagebox.showinfo("Succes", "Actualizare reusita!")
        

    def afiseaza_angajat_dupa_id(self):
        self.listbox.delete(0, tk.END)
        ID=int(self.entry_ID.get())
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_angajati WHERE ID=?", (ID, ))
        rezultat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text=f"ID: {row[0]} - Nume: {row[1]} - Calificare: {row[2]} - Adresa : {row[3]} -  CNP: {row[4]} - Contract: {row[5]}" 
            self.listbox.insert(tk.END, text)
        self.sterge_text_casute()
        self.optiune_angajat.afiseaza_angajat(ID=ID)
        

    def inapoi(self):
        self.listbox.delete(0, tk.END)
     
    def refresh_listbox(self):    
        self.listbox_baza_de_date.delete(0, tk.END)
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_angajati")
        rezultat = self.conexiune_cu_baza_de_date.cursor.fetchall()
        for row in rezultat:
            text = f"ID: {row[0]} - Nume: {row[1]} - Calificare: {row[2]} - Adresa : {row[3]} -  CNP: {row[4]} - Contract: {row[5]}"
            self.listbox_baza_de_date.insert(tk.END, text)

        
    def sterge_text_casute(self):
        self.entry_ID.delete(0, tk.END)
        self.entry_nume.delete(0, tk.END)
        self.entry_cnp.delete(0, tk.END)
        self.entry_adresa.delete(0, tk.END)
        self.entry_contract.delete(0, tk.END)
        self.entry_calificare.delete(0, tk.END)
        
        
    def run(self):
        self.root.mainloop()
        conexiune_cu_baza_de_date.disconnect_baza_de_date()




if __name__ == "__main__":
    conexiune_db_angajat= Conexiune_cu_baza_de_date("test_baza_de_date.db")
    app = AngajatGUI()
    app.run()
    
    
conexiune_db_angajat= Conexiune_cu_baza_de_date("test_baza_de_date.db")