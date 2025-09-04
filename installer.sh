#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# error handler
error_exit() {
    echo -e "${RED}Error: $1${NC}" >&2
    exit 1
}

# check dependencies
check_dependencies() {
    echo -e "${YELLOW}Checking dependencies...${NC}"
    
    if ! command -v git &> /dev/null; then
        error_exit "Git is not installed. Please install it before proceeding."
    fi
    
    if ! command -v python3 &> /dev/null; then
        error_exit "Python3 is not installed. Please install it before proceeding."
    fi
}

# clone project (aggiunto questa funzione mancante)
clone_project() {
    echo -e "${YELLOW}Setting up project...${NC}"
    # Qui va la logica per clonare o preparare il progetto
    # Se il progetto è già scaricato, potresti saltare questa parte
}

# python3 dependencies
install_python_deps() {
    cd sentinel
    echo -e "${YELLOW}Installing python3 dependencies...${NC}"
    
    python3 -m venv sentinel-venv || error_exit "Virtual environment creation failed."
    
    source sentinel-venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt || error_exit "Requirements installation failed."
    pip install -e . || error_exit "Editable installation failed."
}

# MAIN
main() {
    check_dependencies
    clone_project
    install_python_deps

    echo -e "${GREEN}Sentinel installed. Please run on terminal 'sentinel start'.${NC}"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi