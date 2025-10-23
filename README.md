# folder-organiser
Folder-Sort: The Auto-Organizer 

Is your  folder looking more chaotic than Manchester United's defense on the counter-attack? This is a simple, "work smart" Python script that brings order to the chaos.

It's a lightweight, command-line tool that scans any folder you tell it to and automatically organizes your files into clean subdirectories based on their file type.

What It Does 

Scans Any Directory: Point it at Downloads, Desktop, or any other messy folder.

Smart Sorting: Uses a simple "tactical map" (a Python dictionary) to sort files by their extension (e.g., .png, .pdf, .zip).

Auto-Creates Folders: Automatically creates new destination folders (like Images, PDFs, Archives) if they don't already exist.

Safe & Clean: It only moves files, leaving other folders alone. It also gives you a full "post-match report" of how many files were moved.

How to Use

You can run this script from any terminal.

Make sure you have Python 3 installed.

Save folder_sort.py to your computer

Open your terminal and cd into the folder where you saved the script.

Run the script by passing the full path to the messy folder you want to clean.

Example Usage:

On Windows (in cmd or PowerShell):

# Don't forget the quotes ("") if your path has spaces!
python folder_sort.py "C:\Users\Sanchez\Downloads"



On Mac / Linux (in Terminal):

python folder_sort.py "/home/sanchez/Desktop"



How to Customize 

Want to sort more file types? Just edit the type_of_file dictionary in the folder_sort.py script.

For example, to add mp3 files to a new Music folder, just add this line:

type_of_file = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".pdf": "PDFs",
    # ... all the other rules
    ".mp3": "Music"  # <-- Your new rule!
}



Dependencies

Python 3

That's it. All libraries (os, shutil, argparse) are part of the standard Python library. No pip install needed.
