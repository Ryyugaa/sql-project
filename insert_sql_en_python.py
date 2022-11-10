
import sqlite3
basededonne = sqlite3.connect('projet_nsi_sql.db')
curseur = basededonne.cursor()
curseur.execute("INSERT INTO CLUB (id_club, 'nom') VALUES (?, ?)", (1, 'Reims'))
basededonne.commit()
curseur.close


