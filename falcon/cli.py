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
    """falcon start"""
    # Trova il percorso assoluto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    venv_python = os.path.join(base_dir, "falcon-venv", "bin", "python")
    main_script = os.path.join(base_dir, "main.py")
    
    if not os.path.exists(venv_python):
        click.echo(f"{Fore.RED}[X] Error: Virtual environment not found{Style.RESET_ALL}")
        sys.exit(1)
    
    try:
        subprocess.run([venv_python, main_script], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"{Fore.RED}[X] Error during startup: {e}{Style.RESET_ALL}")
        sys.exit(1)
    except FileNotFoundError:
        click.echo(f"{Fore.RED}[X] Python interpreter not found.{Style.RESET_ALL}")
        sys.exit(1)