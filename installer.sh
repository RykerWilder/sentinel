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

# clone repository
clone() {
    echo -e "${YELLOW}Cloning repository...${NC}"
    if [ -d "sentinel" ]; then
        echo -e "${YELLOW}Directory 'sentinel' already exists. Removing it...${NC}"
        rm -rf sentinel
    fi
    git clone "https://github.com/RykerWilder/sentinel" || error_exit "Repository cloning failed."
    cd sentinel || error_exit "Failed to enter sentinel directory."
}

# python3 dependencies
install_python_deps() {
    echo -e "${YELLOW}Installing python3 dependencies...${NC}"
    python3 -m venv sentinel-venv || error_exit "Virtual environment creation failed."
    source sentinel-venv/bin/activate || error_exit "Virtual environment activation failed."
    pip install --upgrade pip || error_exit "Pip upgrade failed."
    
    # Check if requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        error_exit "requirements.txt not found in the repository."
    fi
    
    pip install -r requirements.txt || error_exit "Requirements installation failed."
    pip install -e . || error_exit "Editable installation failed."
}

# MAIN
main() {
    echo -e "${GREEN}Starting Sentinel installation...${NC}"
    check_dependencies
    clone
    install_python_deps
    echo -e "${GREEN}Sentinel installed successfully!"
    echo -e "cd sentinel"
    echo -e "source sentinel-venv/bin/activate"
    echo -e "sentinel"
}

# Run main function only if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi