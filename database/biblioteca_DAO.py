from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca
from UI.alert import AlertManager
"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def read_biblioteche(self):
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is not None:
            query = "SELECT * FROM biblioteca"
            cursor = cnx.cursor()
            cursor.excute(query)
            biblioteche = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                biblioteche.append(biblioteca)

            else:
                AlertManager.show_alert("Errore nel database!")

            cursor.close()
            cnx.close()
            return biblioteche


