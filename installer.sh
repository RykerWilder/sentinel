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
    # Check if python3-venv is available
    if ! python3 -c "import venv" &> /dev/null; then
        echo -e "${YELLOW}python3-venv not found. Installing...${NC}"
        sudo apt update && sudo apt install -y python3-venv python3-pip || error_exit "Failed to install python3-venv"
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
    
    # Create virtual environment
    python3 -m venv sentinel-venv || error_exit "Virtual environment creation failed."
    
    # Activate virtual environment
    source sentinel-venv/bin/activate || error_exit "Virtual environment activation failed."
    
    # Upgrade pip within the virtual environment
    python -m pip install --upgrade pip || error_exit "Pip upgrade failed."
    
    # Check if requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        error_exit "requirements.txt not found in the repository."
    fi
    
    # Install requirements
    pip install -r requirements.txt || error_exit "Requirements installation failed."
    
    # Install in editable mode
    pip install -e . || error_exit "Editable installation failed."
}

# MAIN
main() {
    echo -e "${GREEN}Starting Sentinel installation...${NC}"
    check_dependencies
    clone
    install_python_deps
    echo -e "${GREEN}Sentinel installed successfully!${NC}"
    echo -e "${YELLOW}Now to use Sentinel run:${NC}"
    echo -e "1. cd sentinel"
    echo -e "2. source sentinel-venv/bin/activate"
    echo -e "3. sentinel start"
}

# Run main function only if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi