import tkinter as tk
from PIL import Image, ImageTk 
from interfata_client import ClientGUI
from interfata_grafica_modul_stocuri import IntrariGUI
from interfata_grafica_optiune_angajat import AngajatGUI
from interfata_grafica_tabel_iesiri import IesiriGUI
from interfata_piese_de_schimb import PieseGUI
from interfata_grafica_combustibil import OptiuneCombustibilGUI
from interfata_adresa_livrare import AdresaLivrareGUI


class DescManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DescManager")
        self.root.geometry("800x600")
        
        logo_path = "C:\\Users\\Marian-PC\\OneDrive\\Desktop\\Logo.png"
        original_image = Image.open(logo_path)
        resized_image = original_image.resize((800, 600), Image.BILINEAR)
        self.logo = ImageTk.PhotoImage(resized_image)
        
        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.place(x=0, y=0, anchor='nw')
        

    def creare_interfata(self):
        butoane = [
            ("Baza de date clienti", self.baza_de_date_clienti),
            ("Stoc", self.menu_intrari),
            ("Angajati", self.menu_angajat),
            ("Vanzari", self.menu_vanzari),
            ("Piese de Uzura", self.menu_piese_uzura),
            ("Consumuri", self.menu_consum),
            ("Baza de date adrese + clienti", self.menu_clienti_adrese)
        ]

        for i, (text, command) in enumerate(butoane, start=4):
            buton_optiune_clienti = tk.Button(self.root, text=text, command=command, width=25, height=1)
            buton_optiune_clienti.place(x=15, y=i * 30)

    def baza_de_date_clienti(self):
        self.client_gui = ClientGUI()

    def menu_intrari(self):
        self.intrari_gui = IntrariGUI()

    def menu_angajat(self):
        self.angajat_gui = AngajatGUI()

    def menu_vanzari(self):
        self.iesiri_gui = IesiriGUI()

    def menu_piese_uzura(self):
        self.piese_gui = PieseGUI()

    def menu_consum(self):
        self.combustibil_gui = OptiuneCombustibilGUI()
        
    def menu_clienti_adrese(self):
        self.adrese_clienti=AdresaLivrareGUI()

    def run(self):
        self.root.mainloop()


desc_manager = DescManager()
desc_manager.creare_interfata()
desc_manager.run()
