import os
from colors import bcolors

def header():

        print('\n\t')
        pgn2sql = "pgn2sql: "
        pgn2sql = pgn2sql.center(100,' ')
        print (f'\n{bcolors.OkCyan}{bcolors.Bold}{pgn2sql,}{bcolors.EndC}')
        Descripcion = "Programa de Generacion de fichero SQL desde un Archivo pgn"
        Descripcion = Descripcion.center(100,' ')
        print (f'{Descripcion}')
        print ('\t\t___________________________________________________________________________')
        print ('                                                                          ')

def cleanScreen():
    os.system('cls()' if os.name=='nt' else 'clear')

def pause():
    Pausar = input("\n\n\t\tPulsa la tecla <ENTER>  para ir al Menu...")

def develop():
    print("\n\t\t\tEsta Funcion todavia no esta implementada")
