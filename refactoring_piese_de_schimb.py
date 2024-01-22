from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date

class Piese_de_schimb:
    
    def __init__(self, conexiune_cu_baza_de_date : Conexiune_cu_baza_de_date):
        """Initiam conexiunea cu baza de date

        Args:
            conexiune_cu_baza_de_date (Conexiune_cu_baza_de_date): Obiectul de conexiune cu baza de date
        """
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date
        return
    
    def adauga_piese(self, ID:int, ID_angajat:int, Data:str, piese:str, pret:int, cantitate:int):
        """Adaugam piesele in baza de date

        Args:
            ID (int): Id-ul piesei                          Pretul si cantitatea sunt Integers pentru ca urmeaza sa calculam costul pieselor
            ID_angajat (int): ID ul
            piese (str): numele
            pret (int): pretul
            cantitate (int): cantitatea
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        cost=pret*cantitate
        self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_piese_de_schimb('ID', 'IDAngajat', 'Data', 'piesa', 'pret', 'bucati', 'cost') VALUES {ID, ID_angajat, Data, piese, pret, cantitate, cost}")
        self.conexiune_cu_baza_de_date.conexiune.commit()
        print("Adaugare cu succes.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    
    def actualizeaza_piese(self, ID_PIESA:int, Data:str, piesa:str, pret:int, cantitate:int):
        """Actualizarea pieselor(Daca piesa este scrisa gresit sau pretul se modifica le vom actualiza.)

        Args:
            ID_PIESA (int): Id ul piesei -> Nu se actualizeaza, ramane unic, ca urmare stergerea pieselor se v-a face cu ajutorul ID-ului.
            piesa (str): Actualizarea numelui
            pret (int): Actualizarea pretului
            cantitate (int): Actualizarea cantitatii
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_piese_de_schimb")
        lista_piese_de_schimb=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for ID in lista_piese_de_schimb:
            if ID[0] == ID_PIESA:
                id_valid=True
                cost=pret*cantitate
                break
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_piese_de_schimb SET piesa=(?), Data=(?), pret=(?), bucati=(?), cost=(?) WHERE ID=(?)", (piesa,Data, pret, cantitate, cost, ID_PIESA ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    
    def sterge_piese(self, ID_PIESA:int, ID_ANGAJAT:int):
        """Stergerea piesei

        Args:
            ID_PIESA (int): Id-ul piesei
            ID_ANGAJAT (int): Id-ul angajatului -> Daca cumva vrem sa stergem o piesa specifica unui angajat vom avea nevoie si de id-ul angajatului
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_piese_de_schimb WHERE IDAngajat=(?)", ( ID_ANGAJAT, ) )
        sterge_piesa=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for id in sterge_piesa:
            if id is not None:
                id_valid=True
                break
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_piese_de_schimb WHERE ID=(?)", (ID_PIESA, ))
            self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_consum_total_piese WHERE ID_PIESA=(?)", (ID_PIESA, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Stergere esuata. ID-ul nu se afla in lista.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
    
    def afiseaza_piese(self):
        """Afisarea listei
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_piese_de_schimb.*, tabel_angajati.angajat, tabel_angajati.calificare FROM tabel_piese_de_schimb INNER JOIN tabel_angajati ON tabel_piese_de_schimb.IDAngajat = tabel_angajati.ID;")
        afiseaza_piese=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for piese in afiseaza_piese:
            print(piese)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def salvare_piese_in_baza_de_date(self, ID):
        """Afisarea listei
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_piese_de_schimb.*, tabel_angajati.angajat, tabel_angajati.calificare FROM tabel_piese_de_schimb INNER JOIN tabel_angajati ON tabel_piese_de_schimb.IDAngajat = tabel_angajati.ID  WHERE tabel_piese_de_schimb.ID=?", (ID, ))
        afiseaza_piese=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for piese in afiseaza_piese:
            self.conexiune_cu_baza_de_date.cursor.execute("INSERT INTO tabel_consum_total_piese ('ID_PIESA', 'ID_ANGAJAT', 'Data', 'Denumire', 'Pret', 'Cantitate', 'Valoare_totala_lei', 'Nume', 'Calificare') VALUES (?, ?, ?, ?, ?, ?, ? , ?, ?)", (piese[0], piese[1], piese[2], piese[3], piese[4], piese[5], piese[6], piese[7], piese[8]))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
                

piesa=Piese_de_schimb(conexiune_cu_baza_de_date)


