# basics/os_module_basics.py

"""
OS Module Basics Example
------------------------
This script demonstrates how to use the `os` module to interact with the operating system.
"""

import os

def show_current_directory():
    """Displays the current working directory."""
    cwd = os.getcwd()
    print(f"📂 Current directory: {cwd}")

def list_directory_contents(path="."):
    """Lists files and folders in the given path (defaults to current directory)."""
    print(f"📁 Listing contents of '{path}':")
    for item in os.listdir(path):
        print(f" - {item}")

def create_and_remove_directory(dirname):
    """Creates a directory and then removes it."""
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print(f"✅ Directory '{dirname}' created.")
    else:
        print(f"⚠️ Directory '{dirname}' already exists.")

    os.rmdir(dirname)
    print(f"❌ Directory '{dirname}' removed.")

if __name__ == "__main__":
    show_current_directory()
    list_directory_contents()
    create_and_remove_directory("test_folder")
