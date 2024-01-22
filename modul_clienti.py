from baza_de_date import Conexiune_cu_baza_de_date, conexiune_cu_baza_de_date

class Client:
    def __init__(self, conexiune_cu_baza_de_date:Conexiune_cu_baza_de_date) -> None:
        self.conexiune_cu_baza_de_date=conexiune_cu_baza_de_date
        return
    
    def adauga_clienti(self, COD_CLIENT:int, nume:str, email:str, adresa:str):
        """Adaugarea clientului in baza de date

        Args:
            COD_CLIENT (_type_): Clientului se atribuie un cod de client
            nume (_type_): Numele
            email (_type_): adresa de mail
            adresa (_type_): adresa de locuinta
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute(f"INSERT INTO tabel_clienti ('COD_CLIENT', 'Nume', 'Email', 'Adresa') VALUES {COD_CLIENT, nume, email, adresa, }")
        self.conexiune_cu_baza_de_date.conexiune.commit()
        print("Adaugare cu succes.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
    
    def actualizeaza_nume(self, COD_CLIENT:int, nume:str):
        """Actualizarea numelui

        Args:
            COD_CLIENT (_type_): Selectam codul clientului caruia dorim sa ii actualizam numele
            nume (_type_): adaugam noul nume
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT COD_CLIENT FROM tabel_clienti")
        lista_cod_client=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_cod_client:
            if element[0] == COD_CLIENT:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_clienti SET Nume=? WHERE COD_CLIENT=?", (nume, COD_CLIENT, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un COD_CLIENT valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
            
    def actualizeaza_email(self, COD_CLIENT:int, email:str):
        """Actualizare email

        Args:
            COD_CLIENT (_type_): Selectam clientul
            email (_type_): Actualizam adresa de mail
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT COD_CLIENT FROM tabel_clienti")
        lista_cod_client=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_cod_client:
            if element[0] == COD_CLIENT:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_clienti SET Email=? WHERE COD_CLIENT=?", (email, COD_CLIENT, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un COD_CLIENT valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
    def actualizeaza_adresa(self, COD_CLIENT:int, adresa:str):
        """Actualizarea adreselor de locuinta

        Args:
            COD_CLIENT (_type_): Selectam clientul caruia dorim sa ii actualizam adresa
            adresa (_type_): Actualizarea adresei
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT COD_CLIENT FROM tabel_clienti")
        lista_cod_client=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_cod_client:
            if element[0] == COD_CLIENT:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("UPDATE tabel_clienti SET Adresa=? WHERE COD_CLIENT=?", (adresa, COD_CLIENT, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un COD_CLIENT valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
        
        
    def sterge_client(self, COD_CLIENT:int):
        """stergerea clientului

        Args:
            COD_CLIENT (_type_): Stergerea clientului se v-a face pe baza coodului de client
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("SELECT COD_CLIENT FROM tabel_clienti")
        lista_cod_client=self.conexiune_cu_baza_de_date.cursor.fetchall()
        id_valid=False
        for element in lista_cod_client:
            if element[0] == COD_CLIENT:
                id_valid=True
                break
        
        if id_valid:
            self.conexiune_cu_baza_de_date.cursor.execute("DELETE FROM tabel_clienti WHERE COD_CLIENT=?", (COD_CLIENT, ))
            self.conexiune_cu_baza_de_date.conexiune.commit()
            print("Actualizare reusita.")
        else:
            print("Introduce-ti un COD_CLIENT valid.")
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
            
    def afiseaza(self, COD_CLIENT:int):
        """afisarea clientului

        Args:
            COD_CLIENT (_type_): Cu ajutorul codului vom putea selecta clientul caruia dorim sa vedem datele 
        """
        self.conexiune_cu_baza_de_date.connect_baza_de_date()
        self.conexiune_cu_baza_de_date.cursor.execute("Select * FROM tabel_clienti WHERE COD_CLIENT=(?)", (COD_CLIENT,  ))
        lista_clienti=self.conexiune_cu_baza_de_date.cursor.fetchall()
        for client in lista_clienti:
            print(client)
        self.conexiune_cu_baza_de_date.disconnect_baza_de_date()
            
            
client=Client(conexiune_cu_baza_de_date)
