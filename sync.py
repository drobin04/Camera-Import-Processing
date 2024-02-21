import tkinter as tk
import os
import json
import shutil
from tkinter import filedialog

# Function to save and load directory paths
def save_directories():
    directories = {
        'input_directory': input_directory.get(),
        'output_directory': output_directory.get()
    }
    with open('directories.json', 'w') as file:
        json.dump(directories, file)

def load_directories():
    if os.path.exists('directories.json'):
        with open('directories.json', 'r') as file:
            directories = json.load(file)
            input_directory.set(directories['input_directory'])
            output_directory.set(directories['output_directory'])

# Function to select directory and update the corresponding entry widget
def select_directory(directory_entry):
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)

# Function to perform the main task
def run_script():
    input_dir = input_directory.get()
    output_dir = output_directory.get()
    new_folder_name = new_folder.get()

    # Search for files in the input directory and delete files with extensions THM or SEC
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.THM') or file_name.endswith('.SEC'):
            file_path = os.path.join(input_dir, file_name)
            os.remove(file_path)

    # Create a new folder in the output directory
    new_folder_path = os.path.join(output_dir, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Move remaining files from the input directory to the new folder
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if os.path.isfile(file_path):
            new_file_path = os.path.join(new_folder_path, file_name)
            shutil.move(file_path, new_file_path)

    # Save the directories for future use
    save_directories()

# Create the main window
window = tk.Tk()
window.title("File Management Script")

# Create and pack the input directory widgets
input_directory_label = tk.Label(window, text="Input Directory:")
input_directory_label.pack()
input_directory = tk.StringVar()
input_directory_entry = tk.Entry(window, textvariable=input_directory)
input_directory_entry.pack()

input_directory_button = tk.Button(window, text="Select", command=lambda: select_directory(input_directory_entry))
input_directory_button.pack()

# Create and pack the output directory widgets
output_directory_label = tk.Label(window, text="Output Directory:")
output_directory_label.pack()
output_directory = tk.StringVar()
output_directory_entry = tk.Entry(window, textvariable=output_directory)
output_directory_entry.pack()

output_directory_button = tk.Button(window, text="Select", command=lambda: select_directory(output_directory_entry))
output_directory_button.pack()

# Create and pack the new folder name widgets
new_folder_label = tk.Label(window, text="New Folder Name:")
new_folder_label.pack()
new_folder = tk.StringVar()
new_folder_entry = tk.Entry(window, textvariable=new_folder)
new_folder_entry.pack()

# Load the directories from the previous run
load_directories()

# Create and pack the run button
run_button = tk.Button(window, text="Run", command=run_script)
run_button.pack()

# Start the main event loop
window.mainloop()

