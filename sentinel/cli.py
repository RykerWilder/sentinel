import click
import subprocess
import os
import sys

@click.group()
def cli():
    """Sentinel CLI Tool"""
    pass

@cli.command()
def start():
    """Avvia l'applicazione Sentinel"""
    # Trova il percorso assoluto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    venv_python = os.path.join(base_dir, "sentinel-venv", "bin", "python")
    main_script = os.path.join(base_dir, "main.py")
    
    if not os.path.exists(venv_python):
        click.echo("ERRORE: Virtual environment non trovato!")
        sys.exit(1)
    
    click.echo("Starting Sentinel...")
    try:
        subprocess.run(["sudo", "-E", venv_python, main_script], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Errore durante l'avvio: {e}")
        sys.exit(1)
    except FileNotFoundError:
        click.echo("sudo non trovato o permessi insufficienti")
        sys.exit(1)

if __name__ == "__main__":
    cli()