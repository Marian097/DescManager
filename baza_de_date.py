import sqlite3

class Conexiune_cu_baza_de_date:
    def __init__(self, baza_de_date) -> None:
        self.baza_de_date=baza_de_date
        self.conexiune=None
        self.cursor=None
        
        
    def connect_baza_de_date(self) :
        self.conexiune=sqlite3.connect(self.baza_de_date)
        self.cursor=self.conexiune.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_angajati (ID int, Angajat string, Calificare string, Adresa string, CNP string, Contract string)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_combustibil(ID, IDAngajat int, Data str, combustibil string, pret float, cantitate int, cost int, FOREIGN KEY (IDAngajat) REFERENCES tabel_angajati(ID))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_piese_de_schimb(ID int, IDAngajat int, Data str,  piesa string, pret float, bucati int, cost int, FOREIGN KEY (IDAngajat) REFERENCES tabel_angajati(ID))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_stocuri(ID int, Denumire str, Furnizor str, Unitate_de_masura, stoc int, pret float, total float)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_iesiri (ID_IESIRI int, ID int, Client string, UM str, iesiri int, total float,  FOREIGN KEY (ID) REFERENCES tabel_stocuri(ID))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_clienti (COD_CLIENT int, Nume, Email string, Adresa string, FOREIGN KEY (COD_CLIENT) REFERENCES tabel_iesiri (Client))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_adresa_livrare (ID_ADRESA int, ID_CLIENT int, Adresa_de_livrare, FOREIGN KEY (ID_CLIENT) REFERENCES tabel_clienti (COD_CLIENT))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_consumuri_combustibil (ID_COMBUSTIBIL int, ID_ANGAJAT int, Data str, Combustibil str, Pret int, Cantitate int, Valoare_totala_lei int, Nume str, Calificare str)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_consum_total_piese (ID_PIESA str, ID_ANGAJAT str, Data str, Denumire str, Pret int, Cantitate int, Valoare_totala_lei int, Nume str, Calificare str )")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_clienti_adresa_livrare (ID_ADRESA int, ID_Client int, Adresa_de_livrare str, Nume_client str)")
        self.conexiune.commit()
      
        
        
    def disconnect_baza_de_date(self):
        if self.conexiune:
            self.conexiune.close()
            
            

conexiune_cu_baza_de_date=Conexiune_cu_baza_de_date("test_baza_de_date.db")

conexiune_cu_baza_de_date.connect_baza_de_date()


