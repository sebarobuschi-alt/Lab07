from UI.alert import AlertManager
from database.DB_connect import DBConnect
from model.libro_DTO import Libro


"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_libri_biblioteca(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = "SELECT * FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)
            libri = []
            for row in cursor:
                libro = Libro(*row)
                libri.append(libro)
            cursor.close()
        else:
            AlertManager.show_alert("Errore nel database!")

        cnx.close()
        return libri

