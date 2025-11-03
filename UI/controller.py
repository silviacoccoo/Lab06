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
        lista_auto= self._model.get_automobili() # Recupero la lista di automobili
        self._view.lista_auto.controls.clear() # Pulisce dai risultati vecchi

        if lista_auto: # Se la lista d'auto esiste
            for auto in lista_auto:
                self._view.lista_auto.controls.append(ft.Text(str(auto)))
            self._view.show_alert(f'Trovate {len(lista_auto)} automobili')
        else: # Se la lista d'auto non esiste
            self._view.lista_auto.controls.append(ft.Text('Nessuna automobile trovata'))
            self._view.show_alert(f'Errore nel recupero delle automobili')

        self._view.update()

    def btn_handler_cerca(self, e):
        modello_cercato = self._view.input_modello_auto.value # Il modello cercato è quello preso in input
        self._view.lista_auto_ricerca.controls.clear()

        if not modello_cercato or modello_cercato.strip() == "":
            self._view.show_alert('Inserisci un modello valido per la ricerca')
            self._view.update()
            return

        # Cerco le automobili per il modello inserito come input
        lista_auto_ricerca= self._model.cerca_automobili_per_modello(modello_cercato)

        if lista_auto_ricerca and len(lista_auto_ricerca) > 0: # Se questa lista di auto esiste
            for auto in lista_auto_ricerca:
                self._view.lista_auto_ricerca.controls.append(ft.Text(str(auto)))
            self._view.show_alert(f'Trovate {len(lista_auto_ricerca)} automobili')
        else: # Se è vuota
            self._view.lista_auto_ricerca.controls.append(ft.Text('Nessuna automobile trovata'))
            self._view.show_alert(f'Nessuna automobile trovata per il modello: {modello_cercato} o errore di connessione')

        self._view.update() # Aggiorno l'interfaccia
    # TODO
