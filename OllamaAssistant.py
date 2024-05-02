#!/usr/bin/python3

import tkinter as tk
import requests
import json
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
import subprocess
import os
import datetime as dt


def kill_previous_and_run():
    # Ottieni il PID dell'istanza corrente
    current_pid = os.getpid()

    # Cerca processi in esecuzione con il nome 'GnomeOllama.py'
    result = subprocess.run(["pgrep", "-f", "OllamaAssistant.py"], stdout=subprocess.PIPE)
    pids = result.stdout.decode().split()

    # Se esistono tali processi, uccidi quelli con PID inferiore a quello corrente
    for pid in pids:
        if int(pid) < current_pid:
            subprocess.run(["kill", "-9", pid])

    # Esegui il tuo script
    subprocess.run(["python3", "GnomeOllama.py"])


# Utilizza la funzione
kill_previous_and_run()

headers = {"Content-Type": "application/json"}


def send_to_LLM(prompt, from_clipboard=False):

    # Ottieni il testo copiato
    if from_clipboard:
        copied_text = root.clipboard_get()
    else:
        copied_text = ""

    data = {"model": "phi3:3.8b", "prompt": prompt + copied_text}

    # Inserisci il prompt nella zona di testo
    text_area.insert(
        tk.END, "-------" + dt.datetime.now().strftime("%H:%M:%S") + "-------\n"
    )
    text_area.insert(tk.END, prompt + "\n")

    # p.stop()
    for i in range(1):
        p.step()
        root.update()
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers=headers,
            data=json.dumps(data),
        )

        for line in response.iter_lines():
            if line:
                json_line = json.loads(line)
                text_area.insert(tk.END, json_line["response"])
        text_area.insert(tk.END, "\n\n")

        p.step()
        root.update()


def send_text(option):

    p.pack()

    # Invia il testo all'API selezionando l'opzione corrispondente
    if option == "Riassumi il testo":
        send_to_LLM("Sum up the text, riassumi il testo: \n", from_clipboard=True)
        # Codice per inviare il testo all'API per il riassunto
        pass
    elif option == "Spiega":
        # Codice per inviare il testo all'API per la spiegazione
        send_to_LLM("Explain this text, spiega questo testo: ", from_clipboard=True)
        pass
    elif option == "Rifromula":
        # Codice per inviare il testo all'API per la rifromulazione
        send_to_LLM("Rephrase this text, rifromula questo testo: ", from_clipboard=True)
        pass
    elif option == "Controlla la grammatica":
        # Codice per inviare il testo all'API per la rifromulazione
        send_to_LLM("Check the spelling, controlla la grammatica: ", from_clipboard=True)
        pass
    else:
        # Codice per inviare il testo all'API per la generazione di testo
        send_to_LLM(option)
        pass


def clear_text():
    text_area.delete("1.0", tk.END)


# Crea la finestra
root = tk.Tk()
root.title("LLM Desktop Integration")

# Crea i pulsanti

p = Progressbar(root, length=200, mode="determinate", takefocus=True, maximum=2)

# Crea un frame per i pulsanti
button_frame = tk.Frame(root)
button_frame.pack()

button1 = tk.Button(
    button_frame,
    text="Riassumi il testo",
    command=lambda: send_text("Riassumi il testo"),
)
button1.pack(side=tk.LEFT)

button2 = tk.Button(button_frame, text="Spiega", command=lambda: send_text("Spiega"))
button2.pack(side=tk.LEFT)

button3 = tk.Button(
    button_frame, text="Rifromula", command=lambda: send_text("Rifromula")
)
button3.pack(side=tk.LEFT)

button4 = tk.Button(
    button_frame, text="Controlla", command=lambda: send_text("Controlla la grammatica")
)
button4.pack(side=tk.LEFT)

# Crea il pulsante per pulire il testo
clear_button = tk.Button(button_frame, text="Pulisci", command=clear_text)
clear_button.pack(side=tk.LEFT)

# Crea la zona di testo
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

# Crea un frame per l'input e il pulsante di invio
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X)

# Crea la casella di testo in input
input_text = tk.Entry(input_frame)
input_text.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Crea il pulsante di invio
send_button = tk.Button(
    input_frame, text="Invia", command=lambda: send_text(input_text.get())
)
send_button.pack(side=tk.RIGHT)

# Associa l'evento di pressione del tasto Invio alla funzione send_text
input_text.bind("<Return>", lambda event: send_text(input_text.get()))

# Avvia la finestra
root.mainloop()
