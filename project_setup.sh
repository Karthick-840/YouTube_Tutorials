#!/bin/bash

#######################################################
# Script Name: project_setup.sh
# Description: This script sets up a Python project by 
#              being called by .devcontainer/devcontainer.json, 
#              creating a virtual environment, 
#              installing dependencies, and performing 
#              other project-specific actions.
# Author: Karthick Jayaraman
# Date: 24-01-2023
# Last Modified: 10-12-2023
# Contact: karthick840@yahoo.in
#######################################################

# Function to create virtual environment
create_virtual_environment() {
    if [ ! -d ".venv" ]; then
        echo 
        echo "---------------------------------------------"
        echo "🚀 Creating virtual environment...🚀"
        echo "---------------------------------------------"
        echo 
        python3 -m venv .venv || { echo "❌ Failed to create virtual environment .venv"; return 1; }
    else
        echo
        echo "👉 Virtual environment .venv already present. Skipping this action"
        echo
    fi

}

# Function to activate virtual environment
activate_virtual_environment() {

    echo 
    if [ -f ".venv/bin/activate" ]; then
        echo
        echo "---------------------------------------------"
        echo "🚀 Activating virtual environment...🚀"
        echo "---------------------------------------------"
        echo
        source .venv/bin/activate || { echo "❌ Failed to activate virtual environment .venv"; return 1; }
        echo "Virtual environment activated."
    else
        echo "Failed to find the virtual environment activation script."
        return 1
    fi
}

# Function to upgrade pip
upgrade_pip() {
    echo "Upgrading pip..."
    pip install --upgrade pip
}

# Function to install requirements
install_requirements() {

    echo 
    echo "---------------------------------------------"
    echo "✅ 🔉  Installing Dependencies 🔧"
    echo "---------------------------------------------"
    echo 
    if [ -f "requirements.txt" ]; then
        echo "Installing packages from requirements.txt..."
        pip install -r requirements.txt
    else
        echo "requirements.txt not found, skipping package installation."
    fi
}

# Function to clone and install My_Toolbox repository
install_my_toolbox() {
    local repo_url="https://github.com/Karthick-840/My_Toolbox.git"
    local repo_dir="My_Toolbox"

    echo 
    echo "---------------------------------------------"
    echo "🔧 Installing My_Toolbox Repository 🔧"
    echo "---------------------------------------------"
    echo 

    if [ -d "$repo_dir" ]; then
        echo "Directory $repo_dir already exists. Deleting it..."
        rm -rf "$repo_dir"
    fi

    echo "Cloning repository from $repo_url into $repo_dir..."
    if git clone "$repo_url" "$repo_dir"; then
        echo "Repository cloned successfully."
        echo "Installing the cloned repository from $repo_dir..."
        if cd "$repo_dir"; then
            if pip install .; then
                echo "Repository installed successfully."
            else
                echo "❌ Failed to install the cloned repository"
                return 1
            fi
        else
            echo "❌ Failed to navigate to $repo_dir"
            return 1
        fi
    else
        echo "❌ Failed to clone repository"
        return 1
    fi
}

# Function to check for the presence of the credentials file
check_credentials_file() {
    echo "Checking for credentials file..."
    if [ ! -f "client_secrets.json" ]; then
        echo "Error: client_secrets.json file not found. Please upload your credentials."
        exit 1
    else
        echo "Credentials file found."
    fi
}

# Function to display creation log
display_creation_log() {
    echo 
    echo "Displaying creation log:"
    cat /workspaces/.codespaces/.persistedshare/creation.log
    echo 
}

main() {
    echo 
    echo "---------------------------------------------"
    echo "🐍 Setting up Python Virtual Environment 🌐"
    echo "----------------------------------------------"
    echo 

    if create_virtual_environment; then
        echo "✅ Virtual environment created successfully."
    else
        echo "❌ Failed to create virtual environment."
        exit 1
    fi

    if activate_virtual_environment; then
        echo "✅ Virtual environment activated successfully."
    else
        echo "❌ Failed to activate virtual environment."
        exit 1
    fi

    if upgrade_pip; then
        echo "✅ Pip upgraded successfully."
    else
        echo "❌ Failed to upgrade pip."
        exit 1
    fi

    if install_my_toolbox; then
        echo "✅ Toolbox installed successfully."
    else
        echo "❌ Failed to install toolbox."
        exit 1
    fi

    if install_requirements; then
        echo "✅ Requirements installed successfully."
    else
        echo "❌ Failed to install requirements."
        exit 1
    fi

    if check_credentials_file; then
        echo "✅ Credentials file checked successfully."
    else
        echo "❌ Failed to check credentials file."
        exit 1
    fi

    echo -e "✅ Virtual environment setup complete."

}

# Execute main function
main