from baza_de_date import  Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date

class Intrari:
    def __init__(self, conexiune_cu_baza_de_date : Conexiune_cu_baza_de_date):
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date
        return
        
    def adauga_intrari(self, ID:int, denumire:str, furnizor:str, unitate_de_masura:str, stoc:int, pret:float):
        """Adaugam produsele care intra in stoc

        Args:
            ID (_type_): Adaugam ID-ul specific intrari
            denumire (_type_): denumirea    
            furnizor (_type_): furnizorul
            unitate_de_masura (_type_): unitate de masura
            stoc (_type_): stocul
            pret (_type_): pretul
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        total=pret*stoc
        self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_stocuri('ID', 'Denumire', 'Furnizor', 'Unitate_de_masura', 'stoc', 'pret', 'total') VALUES {ID, denumire, furnizor, unitate_de_masura, stoc, pret, total}")
        self.conexiune_cu_baza_de_date.conexiune.commit()
        print("Adaugare cu succes.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def actualizeaza_denumire(self, ID:int, denumire:str):
        """Actualizam denumirea

        Args:
            ID (int): Id-ul specific
            denumire (str): noua denumire
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False 
        for id in lista_id:
            if id[0] == ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET Denumire=? WHERE ID=?", (denumire, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
       
    
    def actualizeaza_furnizor(self, ID:int, furnizor:str):
        """Actualizam furnizorul

        Args:
            ID (int): Id-ul specific
            furnizor (str): actualizam furnizorul
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri")
        lista_id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False 
        for id in lista_id:
            if id[0] == ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET Furnizor=? WHERE ID=?", (furnizor, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
    def actualizeaza_um(self, ID:int, unitate_de_masura: str):
        """Actualizam unitatea de masura

        Args:
            ID (int): ID-ul specific
            unitate_de_masura (str): Unitate de masura
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False 
        for id in lista_id:
            if id[0] == ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET Unitate_de_masura=? WHERE ID=?", (unitate_de_masura, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
    def actualizeaza_stoc(self, ID:int, stoc:int):
        """Actualizarea stocului

        Args:
            ID (int): ID-ul specific
            stoc (int): noul stoc
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT pret FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_pret=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False 
        for id in lista_id:
            if id[0] == ID:
                id_valid=True
                break
        
        for element in lista_pret:
            pret=element[0]
            total_nou=pret*stoc
            break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET stoc=?, total=? WHERE ID=?", (stoc, total_nou, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def actualizeaza_pret(self, ID:int, pret_nou:float):
        """Actualizarea pretului

        Args:
            ID (int): Id-ul produsului
            pret_nou (float): Introducem noul pret
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT pret FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_pret=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT stoc FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_stocuri=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False 
        for id in lista_id:
            if id[0] == ID:
                id_valid=True
                break
        
        for element in lista_stocuri:
            stoc=element[0]
            break
        
        for pret_vechi in lista_pret:
            if pret_vechi[0] != pret_nou:
                total_nou=pret_nou * stoc
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET pret=?, total=? WHERE ID=?", (pret_nou, total_nou, ID, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
            
    def sterge_intrare(self, ID:int):
        """Stergem intrare

        Args:
            ID (int): Id-ul specific produsului pe care vrem sa il stergem
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_intrari=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for element in lista_intrari:
            if element[0] == ID:
                self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_stocuri WHERE ID=?", (ID, ))
                self.conexiune_cu_baza_de_date.conexiune.commit()
                break
        if element[0] != ID:
            print("Introduceti un ID valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
                
    def afisare_intrari(self):
        """afisare lista de intrari
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT * FROM tabel_stocuri")
        lista_intrari=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for elemente in lista_intrari:
            print(elemente)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
            
    
        
        
intrari=Intrari(conexiune_cu_baza_de_date)

