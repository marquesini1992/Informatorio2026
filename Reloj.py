#Tiene un pequeño Easter Egg
#Pueden 

import tkinter as tk
import time
import random

ventana = tk.Tk()
ventana.title('Reloj Anomalo')
ventana.geometry('400x200')

frame = tk.Frame(ventana)
frame.pack(expand=True)

frame_inferior = tk.Frame(ventana)
frame_inferior.pack(pady=10)

hormin = tk.Label(frame, font=('fixedsys', 60), bg='black', fg='white')
seg = tk.Label(frame, font=('fixedsys', 60), bg='white', fg='black')

#Variables
modo = None                     # "hora", "Cronómetro", "countdown"
after_id = None                 # almacena la función after que esté activa
random_countdown = tk.IntVar()  # modo random activado/desactivado
h = m = s = 0                   # tiempo general


#Control de modos: RELOJ / CRONÓMETRO / COUNTDOWN
def detener_todo():
    """Detiene cualquier modo activo."""
    global after_id, modo
    modo = None
    if after_id is not None:
        ventana.after_cancel(after_id)

#Reloj
def hora():
    global h, m, s, after_id

    if modo != "hora":
        return  # evita que siga si se cambió de modo

    tiempo_actual = time.strftime('%H:%M:%S')
    h, m, s = map(int, tiempo_actual.split(':'))

    hormin.config(text=f"{h:02d}{m:02d} ")
    seg.config(text=f"{s:02d}")

    after_id = ventana.after(1000, hora)

def iniciar_hora():
    detener_todo()
    global modo
    modo = "hora"
    hora()


#Cronómetro
def cronometro():
    global h, m, s, after_id

    if modo != "Cronómetro":
        return

    total = h * 3600 + m * 60 + s + 1
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60

    hormin.config(text=f"{h:02d}{m:02d} ")
    seg.config(text=f"{s:02d}")

    after_id = ventana.after(1000, cronometro)

def iniciar_cronometro():
    detener_todo()
    global modo, h, m, s
    h = m = s = 0
    modo = "Cronómetro"
    cronometro()

#Countdown
def countdown():
    global h, m, s, after_id
    
    if modo != "countdown":
        return

    total = h * 3600 + m * 60 + s - 1

    if total < 0: #Easter Egg
        hormin.config(text="✈DHAR")
        seg.config(text="MA")
        print("Los números son 4 8 15 16 23 42.")
        return

    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60

    hormin.config(text=f"{h:02d}{m:02d} ")
    seg.config(text=f"{s:02d}")

    after_id = ventana.after(1000, countdown)

def iniciar_countdown():
    detener_todo()
    global modo, h, m, s, random_countdown
    modo = "countdown"
    # print("Estado del checkbox:", random_countdown.get())
    # Se define si usara o no valores aleatorios
    if random_countdown.get() == 1:     
     h = random.randint(0, 23)
     m = random.randint(0, 59)
     s = random.randint(0, 59)

    # Mostrar inmediatamente los valores aleatorios
    hormin.config(text=f"{h:02d}{m:02d} ")
    seg.config(text=f"{s:02d}")

    countdown()

#Botones
boton1 = tk.Button(ventana, text='Hora', font=('Arial', 20), command=iniciar_hora)
boton1.pack(side='left')

boton2 = tk.Button(ventana, text='Cronómetro', font=('Arial', 20), command=iniciar_cronometro)
boton2.pack(side='left')

boton3 = tk.Button(ventana, text='Countdown', font=('Arial', 20), command=iniciar_countdown)
boton3.pack(side='left')

checkbox = tk.Checkbutton(
    frame_inferior,
    text="Activar Countdown aleatorio",
    variable=random_countdown
)

#Interfaz
hormin.pack(side='left')
seg.pack(side='left')
checkbox.pack(anchor = 'center')

ventana.mainloop()
