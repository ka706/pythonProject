#Importación de bibliotecas
import cv2
from pyzbar.pyzbar import decode #decodifica los códigos QR
import mysql.connector #impletementa MySQL
import numpy as np #Manipylacion de matrices
import pyautogui, webbrowser #pyautogui para la automatización de la interfaz de usuario,
# y webbrowser para abrir una ventana del navegador.
from time import sleep
def leerqr():
    # Inicia la cámara
    cap = cv2.VideoCapture(0)

    while True: #Entra en un bucle infinito para leer continuamente los frames de la cámara.
        ret, frame = cap.read()

        # Decodifica los códigos QR en la imagen
        codigos_qr = decode(frame)

        for codigo_qr in codigos_qr:
            # Extrae el ID del código QR

            id_qr = codigo_qr.data.decode('utf-8')
            print(f"ID del código QR: {id_qr}") #Imprime el ID del código QR.

            # Busca el ID en la base de datos
            buscar(id_qr)

            # Dibuja un rectángulo alrededor del código QR
            puntos = codigo_qr.polygon
            if len(puntos) == 4:
                pts = np.array(puntos, dtype=int)
                cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        # Muestra la imagen con el rectángulo alrededor del código QR
        cv2.imshow("Lector de QR", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra la ventana
    cap.release()
    cv2.destroyAllWindows()


def buscar(id_qr):
    # Establece la conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="Leslie",
        password="t7O60CM3L8b",
        database="proyectoqr"
    )

    # Crea un cursor
    cursor = conn.cursor()

    # Ejecuta una consulta para buscar el ID en la base de datos
    query = f"SELECT Telefono FROM usuarios WHERE id = {id_qr}"
    cursor.execute(query)
    # Recupera los resultados
    resultados = cursor.fetchall()

    if resultados:
        # Extrae el telefono de la tupla de resultados
        telefono = int(resultados[0][0])

        # Imprime el telefono como entero
        print(telefono)
    else:
        print(f"No se encontraron datos para {id_qr}.")

    webbrowser.open(f'https://web.whatsapp.com/send?phone=+52 1 5 {telefono}')
    #Interacción con WhatsApp Web:
    sleep(20)

    for i in range(1): #Envío de Mensaje con PyAutoGUI:
        pyautogui.typewrite('Ha sido resgistrado en el Centro Universitario UAEM Texcoco, numero de cuenta: ' + id_qr)
        pyautogui.press('enter')

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()


# Llama a la función para leer el código QR
leerqr()