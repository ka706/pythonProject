# Importamos las librerias
import pyqrcode
con = 1
while con <= 2:

    roster = con
    id = '65' + str(con)
    qr = pyqrcode.create(65 and id, error= 'L')
    qr.png('A' + str(roster) + '.png', scale = 6)
    con = con + 1

con = 1
while con <= 2:

    roster = con
    id = '80' + str(con)
    qr = pyqrcode.create(80 and id, error= 'L')
    qr.png('P' + str(roster) + '.png', scale = 6)
    con = con + 1

