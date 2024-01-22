from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date


        
class Angajat:
    
    def __init__(self, conexiune_cu_baza_de_date:Conexiune_cu_baza_de_date):
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date
        return
    
    def adauga_angajat(self, nume:str , ID:int, calificare:str, adresa:str, cnp:str, contract:str):
        """Adaugarea angjatului

        Args:
            nume (str): Adaugarea numelui
            ID (int): Adaugarea ID-ului 
            calificare (str): Adaugarea calificarii
            adresa (str): Adaugarea adresei de locuinta
            cnp (str): Adaugarea cnp-ului
            contract (str): Adaugarea numarului de contract
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        if len(cnp) == 13:
            self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_angajati ('ID', 'Angajat', 'Calificare', 'Adresa', 'CNP', 'Contract') VALUES {ID, nume, calificare, adresa, cnp, contract, }")
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Adaugare cu succes.")
        else:
            print("Adaugare esuata. CNP invalid!")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    

            
    def actualizeaza_nume(self, ID:int, nume_nou:str):
        """Actualizarea numelui

        Args:
            ID (int): Vom folosi ID-ul pentru a selecta numele dorit (toate actualizarile se vor face pe baza ID-ului)
            nume_nou (str): Adaugarea noului nume
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_angajati WHERE ID=?", (ID, ))
        lista_id_angajat=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_id_angajat:
            if element[0] == ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute(f"UPDATE tabel_angajati SET angajat = ? WHERE  ID = ?", (nume_nou, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
                
            
    def actualizeaza_calificare(self, ID:int, calificare:str):
        """Actualizam calificarea

        Args:
            ID (int): Selectam un ID
            calificare (str): Adaugam noua calificare
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_angajati WHERE ID=(?)", (ID, ))
        lista_de_calificari=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_de_calificari:
            if element[0] == ID:
                id_valid=True
                break
            
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute(f"UPDATE tabel_angajati SET calificare = (?) WHERE ID = (?)", (calificare, ID,))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    
    
    def actualizeaza_adresa(self, ID:int, adresa:str):
        """Actualizarea adresei

        Args:
            ID (int): Selectam ID-ul dorit
            adresa (str): Adaugam noua adresa
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_angajati WHERE ID=?", (ID, ))
        lista_de_adrese=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_de_adrese:
            if element[0]==ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_angajati SET Adresa=(?) WHERE ID=(?)", (adresa, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def actualizeaza_cnp(self, ID:int, cnp:str):
        """Actualizam CNP-ul

        Args:
            ID (int): Selectam ID-ul dorit
            cnp (str): Adaugam noul CNP
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_angajati WHERE ID=?", (ID, ))
        lista_cnp=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_cnp:
            if element[0] == ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_angajati SET Cnp=(?) WHERE ID=(?)", (cnp, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def actualizeaza_contract(self, ID:int, contract:str):
        """Actualizam numarul de contract

        Args:
            ID (int): Selectam ID-ul
            contract (str): Adaugam nou numar de contract
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_angajati WHERE ID=(?)", (ID, ))
        lista_contracte=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_contracte:
            if element[0] == ID:
                id_valid=True
                break
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_angajati SET Contract=(?) WHERE ID=(?)", (contract, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    
    
   
    def sterge_angajat(self, ID:int):
        """Stergem angajatul

        Args:
            ID (int): Introducem ID-ul angajatului pe care dorim sa il stergem
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_angajati WHERE ID=(?)", (ID, ))
        lista_angajat=conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_angajat:
            if element[0]==ID :
                id_valid=True
                break
        if id_valid:
            conexiune_cu_baza_de_date.cursor.execute(f"DELETE FROM tabel_angajati WHERE ID=(?)", (ID, ))
            conexiune_cu_baza_de_date.conexiune.commit()
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
                
    def afiseaza_angajat(self, ID:int):
        """Afisarea datelor angajatului selectat  

        Args:
            ID (int): ID-ul anagajtului
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("Select * FROM tabel_angajati WHERE ID=(?)", (ID, ))
        angajati=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for elemente in angajati:
            print(elemente)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
                    


      
angajat=Angajat(conexiune_cu_baza_de_date)
