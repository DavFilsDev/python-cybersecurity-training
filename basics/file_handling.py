# basics/file_handling.py

"""
Simple File Handling Example
----------------------------
This script shows how to create, write, and read a text file in Python.
"""

def write_file(filename, content):
    """Writes the given content to a file."""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"✅ File '{filename}' created and written.")

def read_file(filename):
    """Reads and displays the content of a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"📂 Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")

if __name__ == "__main__":
    filename = "example.txt"
    content = "Hello from Python file handling exercise! second"

    write_file(filename, content)
    read_file(filename)
