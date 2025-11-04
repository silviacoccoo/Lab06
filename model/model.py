from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            return: una lista con tutte le automobili presenti oppure None
        """

        conn=get_connection() # Si crea la connessione con il database

        # Se non si stabilisce la connessione la funzione deve restituire None
        if conn is None:
            print('Errore: connessione al database non riuscita')
            return None

        # Altrimenti, se si crea la connessione
        cursor=conn.cursor(dictionary=True)
        query="SELECT * FROM automobile" # Seleziono dal database di nome automobile
        cursor.execute(query) # Eseguo la query

        result=[] # Inizializzo una lista vuota che accoglierà gli oggetti auto
        for row in cursor:
            disponibile=True if row['disponibile']==1 else False
            # Per ogni riga del cursor creiamo un oggetto auto
            auto=Automobile(
                codice=row['codice'],
                marca=row['marca'],
                modello=row['modello'],
                anno=row['anno'],
                posti=row['posti'],
                disponibile=disponibile
            )
            result.append(auto) # Ogni oggetto auto lo aggiungiamo alla lista result

        cursor.close()
        conn.close()

        return result
        # TODO

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            param modello: il modello dell'automobile
            return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        if not modello:
            return []

        conn=None
        cursor=None

        conn=get_connection()

        if conn is None:
            print('Errore: connessione al database non riuscita')
            return None

        # Altrimenti
        cursor=conn.cursor(dictionary=True)
        query="SELECT * FROM automobile WHERE LOWER(modello) = %s"
        modello_cerca=modello.strip().lower()
        cursor.execute(query,(modello_cerca,))

        result=[]
        for row in cursor:
            disponibile=True if row['disponibile']==1 else False
            auto=Automobile(
                codice=row['codice'],
                marca=row['marca'],
                modello=row['modello'],
                anno=row['anno'],
                posti=row['posti'],
                disponibile=disponibile
            )
            result.append(auto)

        cursor.close()
        conn.close()

        return result
        # TODO
