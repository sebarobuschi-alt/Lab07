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
        try:
            for biblioteca in self._model.get_biblioteche():
                opzione = ft.dropdown.Option(key=biblioteca.id, text=biblioteca.nome)
                self._view._dd_biblioteche.options.append(opzione)
            self._view.update()
        except Exception as e:
            raise self._view.show_alert("Errore nel popolamento della dropdown")


    def popola_dd_genere(self,e):
        self._view._dd_genere.options.clear()
        self._view._dd_genere.options.append(ft.dropdown.Option(key="", text=""))
        try:
            for genere in self._model.get_generi():
                opzione = ft.dropdown.Option(key=genere, text=genere)
                self._view._dd_genere.options.append(opzione)
            self._view.update()
        except Exception as e:
            raise self._view.show_alert("Errore nel popolamento della dropdown")


    # CALLBACKS DROPDOWN
    def on_select(self,e):
        self.biblioteca_selezionata = self._view._dd_biblioteche.value
        self.genere_selezionato = self._view._dd_genere.value




    # AZIONE: MOSTRA LIBRI
    def handler_mostra_libri(self,e):
        self._view._list_view.controls.clear()
        # Svuota i risultati precedenti
        try:
            libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
            for libro in libri:
                self._view._list_view.controls.append(ft.Text(str(libro)))
            self._view.update()
        except Exception as e:
            raise self._view.show_alert("Errore nell'utilizzo dell'handler 'mostra_libri'")