import shutil
import os
import sys
import subprocess

def print_logo():
    print(""" 
      ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░        
     ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
     ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
      ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░        
            ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
            ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
     ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░
    """)

def print_dynamic_dots(key, value):
  # Ottieni la larghezza corrente del terminale
  cols = shutil.get_terminal_size().columns
        
  #Calcola la lunghezza disponibile per i puntini
  available_space = cols - len(key) - len(str(value)) - 3  
        
  # Stampa la chiave, i puntini e il valore
  print(f"{key}: {'.' * available_space} {value}")

def sentinel_initializer():
  # Nome della cartella dell'ambiente virtuale
  venv_name = "venv"

  # Crea l'ambiente virtuale
  print(f"Creating a virtual environment '{venv_name}'...")
  subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)

  # Percorsi dei comandi pip/python nell'ambiente virtuale
  pip_path = os.path.join(venv_name, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_name, "bin", "pip")
  python_path = os.path.join(venv_name, "Scripts", "python") if os.name == "nt" else os.path.join(venv_name, "bin", "python")

  # Installa le dipendenze
  print("Installing dependencies from requirements.txt...")
  subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)

  print(f"Virtual environment successfully configured! Activate it with:")
  print(f"- Windows: `{venv_name}\\Scripts\\activate`")
  print(f"- Linux/macOS: `source {venv_name}/bin/activate`")