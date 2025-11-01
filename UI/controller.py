import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def btn_handler_mostra(self, e):
        lista_auto= self._model.get_automobili()
        self._view.lista_auto.controls.clear()
        if lista_auto:
            for auto in lista_auto:
                self._view.lista_auto.controls.append(ft.Text(str(auto)))
            self._view.show_alert(f'Trovate {len(lista_auto)} automobili')
        else:
            self._view.lista_auto.controls.append(ft.Text('Nessuna automobile trovata'))
            self._view.show_alert(f'Errore nel recupero delle automobili')

        self._view.update()

    def btn_handler_cerca(self, e):
        modello_cercato = self._view.input_modello_auto.value
        self._view.lista_auto.controls.clear()

        if not modello_cercato:
            self._view.show_alert('Inserisci modello')
            self._view.update()
            return
        lista_auto_ricerca= self._model.cerca_automobili_per_modello(modello_cercato)

        if lista_auto_cercata:
            for auto in lista_auto_cercata:
                self._view.lista_auto_ricerca.controls.append(ft.Text(str(auto)))
            self._view.show_alert(f'Trovate {len(lista_auto_cercata)} automobili')
        else:
            self._view.lista_auto_ricerca.controls.append(ft.Text('Nessuna automobile trovata'))
            self._view.show_alert(f'Nessuna automobile trovata')
    # TODO
