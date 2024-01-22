from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date

class Adresa_livrare: 
    
    def __init__(self, conexiune_cu_baza_de_date : Conexiune_cu_baza_de_date):
        self.conexiune_cu_baza_de_date = conexiune_cu_baza_de_date
        return
    
    def adauga_adresa(self, ID_ADRESA, ID_CLIENT, adresa ):
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_adresa_livrare ('ID_ADRESA', 'ID_CLIENT', 'Adresa_de_livrare') VALUES {ID_ADRESA, ID_CLIENT, adresa}")
        self.conexiune_cu_baza_de_date.conexiune.commit()
        print("Adaugare reusita.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
        
    def actualizeaza_adresa(self, ID_ADRESA, adresa_actualizata):
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID_ADRESA FROM tabel_adresa_livrare WHERE ID_ADRESA=?", (ID_ADRESA, ))
        lista_id_adresa=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_id_adresa:
            if element[0] == ID_ADRESA:
                id_valid=True
                break
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_adresa_livrare SET Adresa_de_livrare=? WHERE ID_ADRESA=?", (adresa_actualizata, ID_ADRESA, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def sterge_adresa(self, ID_ADRESA):
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID_ADRESA FROM tabel_adresa_livrare WHERE ID_ADRESA=?", (ID_ADRESA, ))
        id_adresa=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in id_adresa:
            if element[0] == ID_ADRESA:
                id_valid=True
                break
            
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_adresa_livrare WHERE ID_ADRESA=?", (ID_ADRESA, ))
            self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_clienti_adresa_livrare WHERE ID_ADRESA=?", (ID_ADRESA, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Adresa a fost stearsa.")
        else:
            print("ID invalid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
        
    def afiseaza_livrare(self):
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_adresa_livrare.*, tabel_clienti.Nume FROM tabel_adresa_livrare INNER JOIN tabel_clienti ON tabel_adresa_livrare.ID_CLIENT=tabel_clienti.COD_CLIENT;")
        livrare=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for informatii in livrare:
            print(informatii)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def salvare_client_adresa_livrare_bd(self, ID_ADRESA):
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_adresa_livrare.*, tabel_clienti.Nume FROM tabel_adresa_livrare INNER JOIN tabel_clienti ON tabel_adresa_livrare.ID_CLIENT=tabel_clienti.COD_CLIENT WHERE tabel_adresa_livrare.ID_ADRESA=?;", (ID_ADRESA, ))
        livrare=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for informatii in livrare:
            self.conexiune_cu_baza_de_date.cursor.execute("INSERT INTO tabel_clienti_adresa_livrare ('ID_ADRESA', 'ID_CLIENT', 'Adresa_de_livrare', 'Nume_client') VALUES (?, ?, ?, ?)",(informatii[0], informatii[1], informatii[2], informatii[3]))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
            
            
        
        
    
        
        
        
adresa_livrare=Adresa_livrare(conexiune_cu_baza_de_date)


       
        