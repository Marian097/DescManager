from baza_de_date import  Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date


class Combustibil:
    def __init__(self, conexiune_cu_baza_de_date : Conexiune_cu_baza_de_date):
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date
        return
    
    def adauga_combustibil(self, ID:int, ID_ANGAJAT:int, Data:str, combustibil:str, pret:int, cantitate:int):
        """Adaugarea consumului

        Args:
            ID (int): ID-ul pentru consum
            ID_ANGAJAT (int): ID-ul specific anagajtului caruia se atribuie un consum
            combustibil (str): Adaugam combustibil
            pret (int):  Adaugam pretul
            cantitate (int): Adaugam cantitatea cantitatea
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        cost=pret*cantitate
        self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_combustibil ('ID', 'IDAngajat', 'Data','combustibil', 'pret', 'cantitate', 'cost') VALUES {ID, ID_ANGAJAT, Data, combustibil, pret, cantitate, cost, }")
        self.conexiune_cu_baza_de_date.conexiune.commit()
        print("Adaugare cu succes.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
           
    def actualizeaza_combustibil(self, ID_COMBUSTIBIL:int, combustibil:str, Data:str, pret:int, cantitate:int):
        """Actualizarea combustibilului

        Args:
            ID_COMBUSTIBIL (int):  Adaugam un ID specific combustibilului -> Actualizarea combustibilului se v-a realiza cu ajutorul ID-ului
            combustibil (str): Adaugam o noua caloare pentru combustibil
            pret (int): Adaugam o noua valoare pentru pret
            cantitate (int): Adaugam o noua cantitate
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_combustibil")
        lista_de_combustibil=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for ID in lista_de_combustibil:
            if ID[0] == ID_COMBUSTIBIL:
                id_valid=True
                cost=pret*cantitate
                break
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_combustibil SET combustibil=(?), Data=(?), pret=(?), cantitate=(?), cost=(?) WHERE ID=(?)", (combustibil, Data, pret, cantitate, cost, ID_COMBUSTIBIL, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
          
    def sterge_combustibil(self, ID_COMBUSTIBIL:int):
        """Stergem combustibilul

        Args:
            ID_COMBUSTIBIL (int): Stergerea se v-a realiza cu ajutorul Id-ului specific combustibilului dorit sters
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_combustibil")
        lista_combustibil=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_combustibil:
            if element[0]==ID_COMBUSTIBIL:
                id_valid=True
                break
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute(f"DELETE FROM tabel_combustibil WHERE ID=(?)", (ID_COMBUSTIBIL, ))
            self.conexiune_cu_baza_de_date.cursor.execute(f"DELETE FROM tabel_consumuri_combustibil WHERE ID_COMBUSTIBIL=(?)", (ID_COMBUSTIBIL, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
    def afiseaza_combustibil(self):
        """Afisarea combustibilului
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_combustibil.*, tabel_angajati.angajat, tabel_angajati.calificare FROM tabel_combustibil INNER JOIN tabel_angajati ON tabel_combustibil.IDAngajat = tabel_angajati.ID;")
        afiseaza_date=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for element in afiseaza_date:
             print(element)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def Adauga_combustibil_total_in_baza_de_date(self, ID):
        """Afisarea combustibilului
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_combustibil.*, tabel_angajati.angajat, tabel_angajati.calificare FROM tabel_combustibil INNER JOIN tabel_angajati ON tabel_combustibil.IDAngajat = tabel_angajati.ID WHERE tabel_combustibil.ID=?", (ID, ))
        afiseaza_date=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for element in afiseaza_date:
             self.conexiune_cu_baza_de_date.cursor.execute("INSERT INTO tabel_consumuri_combustibil ('ID_COMBUSTIBIL', 'ID_ANGAJAT', 'Data', 'Combustibil', 'Pret', 'Cantitate', 'Valoare_totala_lei', 'Nume', 'Calificare') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8]))
             self.conexiune_cu_baza_de_date.conexiune.commit()
             print("Operatiune cu succes.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    
    
    
combustibil=Combustibil(conexiune_cu_baza_de_date)
