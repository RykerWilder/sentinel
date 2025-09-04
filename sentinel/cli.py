import click
import subprocess
import os
import sys
from colorama import Fore, Style

@click.group()
def cli():
    pass

@cli.command()
def start():
    """start sentinel"""
    # Trova il percorso assoluto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    venv_python = os.path.join(base_dir, "sentinel-venv", "bin", "python")
    main_script = os.path.join(base_dir, "main.py")
    
    if not os.path.exists(venv_python):
        click.echo(f"{Fore.RED}[X] error: Virtual environment non trovato!{Style.RESET_ALL}")
        sys.exit(1)
    
    click.echo("Starting sentinel...")
    try:
        subprocess.run(["sudo", "-E", venv_python, main_script], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"{Fore.RED}[X] Error during startup: {e}{Style.RESET_ALL}")
        sys.exit(1)
    except FileNotFoundError:
        click.echo(f"{Fore.RED}[X] sudo not found or insufficient permissions.{Style.RESET_ALL}")
        sys.exit(1)