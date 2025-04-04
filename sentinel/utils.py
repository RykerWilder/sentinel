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
    venv_dir = "venv"
    venv_path = Path(venv_dir)

    # 1. Controlla se il venv esiste già
    if venv_path.exists():
        print(f"⚠️ La cartella '{venv_dir}' esiste già. Eliminala prima di riprovare.")
        sys.exit(1)

    # 2. Crea il venv
    print(f"\n🐍 Creazione ambiente virtuale in '{venv_dir}'...")
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante la creazione del venv: {e}")
        sys.exit(1)

    # 3. Percorsi dei comandi (cross-OS)
    pip_path = str(venv_path / "Scripts" / "pip") if os.name == "nt" else str(venv_path / "bin" / "pip")

    # 4. Installa le dipendenze + pacchetto in editable mode
    print("\n📦 Installazione delle dipendenze...")
    try:
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        subprocess.run([pip_path, "install", "-e", "."], check=True)  # Aggiunto questo!
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante l'installazione: {e}")
        sys.exit(1)

    # 5. Messaggio di completamento
    print("\n✅ Configurazione completata!")
    print("\nPer attivare il venv:")
    print(f"  {'venv\\Scripts\\activate' if os.name == 'nt' else 'source venv/bin/activate'}")

if __name__ == "__main__":
    create_venv_and_install_deps()