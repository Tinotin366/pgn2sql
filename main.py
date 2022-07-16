#!/usr/bin/env python3

from functions import header
import mariadb

# If you have problem install mariadb try:
# pip3 install mariadb==1.0.10 

# Python 3.8.6

import sys
import os
from functions import *
from conf import db
from colors import bcolors


# Limpiar primera la pantalla
cleanScreen()

header()


# Programa para convertir un fichero en formato pgn a un fichero  sql parta poderlo insertar en una base de datos.
# Por el momento abrira el fichero por defecto: games.pgn
pgnFile = open("games.pgn", "r")

# Opening a file

Counter = 0

# Reading from file
pgnContent = pgnFile.read()
# Divide una cadena en una lista donde cada palabra es un elemento de la lista.
# El caracter en la funcion define cada elemento. \n en nuestro caso.

pgnList = pgnContent.split("\n")

for i in pgnList:
	if i:
		Counter += 1
		
# print("This is the number of lines in the file")
print("El numero de lineas del fichero games.pgn es de: {}".format(Counter))
# print(Counter)

# Vamos a contar el numero de partidas que hay en este fichero
# Para ello vemos que hay 2 saltos de linea entre cada partida.
# y un salto de linea entre los campos de la partida y la notacion de la partida.
# Puede darse el caso que no haya dos saltos entre partida y por lo tanto hay que tener un criterio para ver com detectarlo. Tambien hay que detectar el final del pgn

# Los campos del pgn son:

print ('Los campos del pgn son:\n')

print (f'{bcolors.OkCyan}Seven Tag Roster:{bcolors.EndC} ')

print ('[Event " Name of the tournament or match event. "]')
print ('[Site "Location of the event"]')
print ('[Date "Starting date of the game, in YYYY.MM.DD form. "]')
print ('[Round "Playing round ordinal of the game within the event."]')
print ('[White "Player of the white pieces, in Lastname, Firstname format."]')
print ('[Black "Player of the black pieces, in Lastname, Firstname format. "]')
print ('[Result "Result of the game. It is recorded as White score, dash, then Black score, or *"]')

print (f'\n{bcolors.OkCyan}Optional tag pairs{bcolors.EndC} ')


print ('[TimeControl "300+0"]')
print ('[PlyCount "String value denoting the total number of half-moves played. "]')
print ('[Board "Board on competition. In single tournament or position in team competition"]')
print ('[Termination "Normal"]')
print ('[FEN "The initial position of the chessboard, in Forsyth–Edwards Notation. "]')
print ('[Annotator ""]')
print ('[Mode "OTB (over-the-board) ICS (Internet Chess Server) "]')
print ('[Movetext  (without Tag asigned "SAN:  Standard Algebraic Notation"]')

print (f'\n{bcolors.OkCyan}Optional Extra tag pairs{bcolors.EndC} ')

print ('[WhiteTitle "Title of White Player"]')
print ('[BlackTitle "Title of Black Player"]')
print ('[WhiteTeam "White Team"]')
print ('[BlackTeam "Black Team"]')
print ('[WhiteElo "White ELO"]')
print ('[BlackElo "Black ELO"]')
print ('[WhiteRatingDiff "White - Black diference"]')
print ('[BlackRatingDiff "Black - White diference"]')

print ('[UTCDate "UTC (Universal Time Coordinated Date)"]')
print ('[UTCTime "UTC (Universal Time Coordinated Time)"]')
print ('[Variant "Chess Variant: Standard, 960, etc"]')
print ('[EndTime "Final end time of the game"]')
print ('[ECO "ECO Code"]')
print ('[Opening "Game Opening"]\n')

print ('La Salida hacia el fichero generado [games.sql] debe de ser algo parecido a:\n')

# INSERT INTO games (Id_Game, Event, Site, Date, Round, Board, White, WhiteTitle, WhiteTeam,  Black, BlackTitle, BlackTeam, Result, WhiteTeam, BlackTeam, UTCDate, UTCTime, WhiteElo, BlackElo, WhiteRatingDiff, BlackRatingDiff, Variant, EndTime, TimeControl, ECO, Termination, Annotator)
# VALUES (Id_Game, "Event", "Site", "Date", Round, Board, "White", "WhiteTitle", "WhiteTeam", "Black", "Result", "BlackTitle", "BlackTeam", "WhiteTeam", "BlackTeam", "UTCDate", "UTCTime", WhiteElo, BlackElo, WhiteRatingDiff, BlackRatingDiff, "Variant", "EndTime", "TimeControl", "ECO", "Termination", "Annotator")

print ('INSERT INTO games (Id_Game, Event, Site, Date, Round, Board, White, WhiteTitle, WhiteTeam,  Black, BlackTitle, BlackTeam, Result, WhiteTeam, BlackTeam, UTCDate, UTCTime, WhiteElo, BlackElo, WhiteRatingDiff, BlackRatingDiff, Variant, EndTime, TimeControl, ECO, Termination, Annotator)')
print ('VALUES (Id_Game, "Event", "Site", "Date", Round, Board, "White", "WhiteTitle", "WhiteTeam", "Black", "Result", "BlackTitle", "BlackTeam", "WhiteTeam", "BlackTeam", "UTCDate", "UTCTime", WhiteElo, BlackElo, WhiteRatingDiff, BlackRatingDiff, "Variant", "EndTime", "TimeControl", "ECO", "Termination", "Annotator")')

# Creacion de la Database 

# MariaDB [(none)]> create database games;
# MariaDB [(none)> grant all privileges on  games to 'player'@'localhost' identified by "password";
# MariaDB [(none)]> use games;

# Creacion la Tabla Games

# CREATE TABLE games (Id_Game int(8) NOT NULL,  Event varchar(256) DEFAULT NULL, Site varchar(256) DEFAULT NULL, Date date DEFAULT NULL,  Round int(2) DEFAULT NULL, Board int(3) DEFAULT NULL, White varchar(256) DEFAULT NULL,  WhiteTitle varchar(4) DEFAULT NULL, WhiteTeam varchar(256) DEFAULT NULL, WhiteElo varchar(4) DEFAULT NULL, WhiteRatingDiff varchar(4) DEFAULT NULL,  Black varchar(256) DEFAULT NULL, BlackTitle varchar(4) DEFAULT NULL, BlackTeam varchar(256) DEFAULT NULL,  BlackElo varchar(4) DEFAULT NULL, BlackRatingDiff varchar(4) DEFAULT NULL, Result varchar(3) DEFAULT NULL, UTCDate date DEFAULT NULL, UTCTime time DEFAULT NULL,  Variant varchar(256) DEFAULT NULL, EndTime varchar(25) DEFAULT NULL, TimeControl varchar(25) DEFAULT NULL, ECO varchar(3) DEFAULT NULL, Opening varchar(256) DEFAULT NULL, Termination varchar(25) DEFAULT NULL, Annotator varchar(50) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


