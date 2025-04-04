import shutil
import os
import sys
import subprocess
from pathlib import Path

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

def create_venv_and_install_deps():
    # Nome della cartella dell'ambiente virtuale
    venv_dir = "venv"
    venv_path = Path(venv_dir)

    # Controlla se il venv esiste già
    if venv_path.exists():
        print(f"⚠️ La cartella '{venv_dir}' esiste già. Eliminala prima di riprovare.")
        sys.exit(1)

    # 1. Crea l'ambiente virtuale
    print(f"\n🐍 Creazione ambiente virtuale in '{venv_dir}'...")
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante la creazione del venv: {e}")
        sys.exit(1)

    # 2. Percorsi dei comandi pip/python (cross-OS)
    if os.name == "nt":  # Windows
        pip_path = str(venv_path / "Scripts" / "pip.exe")
        python_path = str(venv_path / "Scripts" / "python.exe")
    else:  # Linux/macOS
        pip_path = str(venv_path / "bin" / "pip")
        python_path = str(venv_path / "bin" / "python")

    # 3. Installa le dipendenze
    print("\n📦 Installazione delle dipendenze da requirements.txt...")
    try:
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante l'installazione delle dipendenze: {e}")
        sys.exit(1)

    # Messaggio di completamento
    print("\n✅ Ambiente virtuale configurato con successo!")
    print("\nPer attivarlo, esegui:")
    if os.name == "nt":
        print(f"  {venv_dir}\\Scripts\\activate")
    else:
        print(f"  source {venv_dir}/bin/activate")