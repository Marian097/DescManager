from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date


class Iesiri:
    
    def __init__(self, conexiune_cu_baza_de_date:Conexiune_cu_baza_de_date):
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date
        return
    
    def adauga_iesiri(self, ID_IESIRI:int, ID:int, COD_CLIENT:int, unitate_de_masura:str, iesiri:int):
        """Aceasta functie are rolul de a scadea produsele din stocul existent

        Args:
            ID_IESIRI (int): Adaugam un ID specific comenzi
            ID (int): Adaugam Id-ul specific produsului
            COD_CLIENT (int): Adaugam codul de client caruia se atribuie comanda
            unitate_de_masura (str): unitatea de masura
            iesiri (int): adaugam cantitatea dorita
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID FROM tabel_stocuri")
        id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT COD_CLIENT FROM tabel_clienti")
        lista_id_clienti=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT pret FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_pret=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for element in lista_pret:
            pret=element[0]
            total_iesiri=pret*iesiri
            break
            
        for element in lista_id_clienti:
            if element[0] == COD_CLIENT:
                COD_CLIENT=element[0]
                break
            
        id_valid=False
        for element in id:
            if element[0] == ID:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_iesiri ('ID_IESIRI', 'ID', 'Client', 'UM', 'iesiri', 'total' ) VALUES { ID_IESIRI ,ID, COD_CLIENT, unitate_de_masura, iesiri, total_iesiri}")
            self.conexiune_cu_baza_de_date.conexiune.commit()
            self.conexiune_cu_baza_de_date.cursor.execute("SELECT iesiri FROM tabel_iesiri WHERE ID=?", ( ID,))
            lista_iesiri=self.conexiune_cu_baza_de_date.cursor.fetchall()
            self.conexiune_cu_baza_de_date.cursor.execute("SELECT stoc FROM tabel_stocuri WHERE ID=?", (ID,))
            lista_stoc=self.conexiune_cu_baza_de_date.cursor.fetchall()
            self.conexiune_cu_baza_de_date.cursor.execute("SELECT total FROM tabel_stocuri WHERE ID=?", (ID, ))
            lista_total=self.conexiune_cu_baza_de_date.cursor.fetchall()
            print("Adaugare reusita.")
        else:
            print("Introduceti un ID valid.")
            return
        
        
        for element in lista_total:
            total=element[0]
            break
        
        for element in lista_iesiri:
            iesiri=element[0]
            break
        for element in lista_stoc:
            stoc=element[0]
            break
        
        
        total_final=total-total_iesiri
        stoc_final=stoc-iesiri
        self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET stoc=?, total=? WHERE ID=?", (stoc_final, total_final, ID, ))
        self.conexiune_cu_baza_de_date.conexiune.commit()
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
    
    def sterge_iesiri(self, ID_IESIRI:int, ID:int):
        """Stergem comanda. In cazul in care clientul se razgandeste in privinta produsului trebuie readaugat in stoc

        Args:
            ID_IESIRI (int): Id-ul comenzii specifice
            ID (int): Id-ul produsului.
            Dupa stergerea comenzii, produsul si valoarea vor reintra in stoc
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT ID_IESIRI FROM tabel_iesiri")
        lista_id=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT iesiri FROM tabel_iesiri WHERE ID_IESIRI=?", (ID_IESIRI,))
        lista_iesiri=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT stoc FROM tabel_stocuri WHERE ID=?", (ID, ) )
        lista_stoc=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT total FROM tabel_iesiri WHERE ID_IESIRI=?", (ID_IESIRI, ))
        lista_total_iesiri=self.conexiune_cu_baza_de_date.cursor.fetchall()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT total FROM tabel_stocuri WHERE ID=?", (ID, ))
        lista_total_initial=self.conexiune_cu_baza_de_date.cursor.fetchall()
        
        for element in lista_id:
            if element[0]==ID_IESIRI:
                self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_iesiri WHERE ID_IESIRI=?", (ID_IESIRI, ))
                self.conexiune_cu_baza_de_date.conexiune.commit()
                break
        
        for element in lista_total_initial:
            total_stocuri=element[0]
            break
            
        for element in lista_total_iesiri:
            total_iesiri=element[0]
            break
        
        for element in lista_iesiri:
            iesiri=element[0]
            break
        
        for element in lista_stoc:
            stoc=element[0]
            break
        
        total_initial=total_stocuri+total_iesiri
        stoc_initial=iesiri+stoc
        self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_stocuri SET stoc=?, total=? WHERE ID=?", (stoc_initial, total_initial, ID))
        self.conexiune_cu_baza_de_date.conexiune.commit()
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    def afiseaza_iesiri(self):
        """Afisarea comenzilor
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT tabel_clienti.Nume, tabel_iesiri.* FROM tabel_clienti INNER JOIN tabel_iesiri ON tabel_clienti.COD_CLIENT = tabel_iesiri.Client")
        lista_iesiri=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for informatii in lista_iesiri:
            print(informatii)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()


iesiri=Iesiri(conexiune_cu_baza_de_date)

