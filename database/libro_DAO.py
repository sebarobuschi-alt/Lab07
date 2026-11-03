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
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is not None:
            query = "SELECT * FROM libri"
            cursor = cnx.cursor()
            cursor.excute(query)
            libri = []
            for row in cursor:
                libro = Libro(*row)
                libri.append(libro)

            else:
                AlertManager.show_alert("Errore nel database!")
            cursor.close()
            cnx.close()
            return libri

