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
            :return: una lista con tutte le automobili presenti oppure None
        """
        try:
            conn=get_connection()
            if conn is None:
                print('Errore: connessione al database non riuscita')
                return None
            #else
            cursor=conn.cursor(dictionary=True)
            query="SELECT * FROM automobile"
            cursor.execute(query)
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
        except Exception as e:
            print(f'Errore: {e}')
            return None
        # TODO

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        if not modello:
            return None

        try:
            conn=get_connection()
            if conn in None:
                print('Errore: connessione al database non riuscita')
                return None
            #else
            cursor=conn.cursor(dictionary=True)
            query="SELECT * FROM automobile WHERE LOWER(modello) LIKE %s"
            modello_cerca="%" + modello.lower() + "%"
            cursor.execute(query,modello_cerca)

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
        except Exception as e:
            print(f'Errore: {e}')
            return None
        # TODO
