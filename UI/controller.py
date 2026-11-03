import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dd_biblioteche(self,e):
        self._view._dd_biblioteche.options.clear()
        self._view._dd_biblioteche.options.append(ft.dropdown.Option(key="", text=""))
        for biblioteca in self._model.get_biblioteche():
            opzione = ft.dropdown.Option(key=biblioteca, text=biblioteca)
            self._view._dd_biblioteche.options.append(opzione)
        self._view.update()

    def popola_dd_genere(self,e):
        self._view._dd_genere.options.clear()
        self._view._dd_genere.options.append(ft.dropdown.Option(key="", text=""))
        for genere in self._model.get_genere():
            opzione = ft.dropdown.Option(key=genere, text=genere)
            self._view._dd_genere.options.append(opzione)
        self._view.update()


    # CALLBACKS DROPDOWN
    def on_biblioteca_change(self,e):
        self.biblioteca_selezionata = self._view._dd_biblioteche.value

    def on_genere_change(self,e):
        self.genere_selezionato = self._view._dd_genere.value



    # AZIONE: MOSTRA LIBRI
    def handler_mostra_libri(self,e):
        risultato = []
        for libro in self._model.get_libri_filtrati(self.biblioteca_selezionata,self.genere_selezionato):
            risultato.append(libro)
            self._view._list_view.controls.append(risultato)
