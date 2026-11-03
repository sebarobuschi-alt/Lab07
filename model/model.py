from database import libro_DAO
from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        b_s = biblioteca.strip()
        g_s = genere.strip()
        result = []
        for libro in self._libro_dao:
            if b_s and g_s in libro:
                result.append(libro)

            elif b_s in libro:
                result.append(libro)

            elif g_s in libro:
                result.append(libro)
        return result
    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        generi = []
        for libro in self._libro_dao:
            genere = libro[3]
            if genere not in generi:
                generi.append(genere)
        return generi


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        biblioteche = []
        for biblioteca in self._biblioteca_dao:
            if biblioteca not in biblioteche:
                biblioteche.append(biblioteca)

        return biblioteche