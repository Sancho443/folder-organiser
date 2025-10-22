import os
import shutil
import argparse
import time

parser = argparse.ArgumentParser(description='Sort folders')
parser.add_argument('folder_path', type=str, help='Folder path')
args = parser.parse_args()
target_folder = args.folder_path


#this is the dictionary for the ffolder name and type of file that should be stored in it
#you could also add you type of file here and it will automatically create a folder for it
type_of_file = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".pdf": "PDFs",
    ".zip": "Archives",
    ".exe": "Exes",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".m4a": "Videos",
}

print(f"MZEE,acha tusafishe hii folder: {target_folder}")
print("Itabidi umechill kiasi,nipee 5 sec hivi")
time.sleep(5)

try:
    all_files = os.listdir(target_folder)
except FileNotFoundError:
    #
    print(f"[!!!!!!]YOOOH,hakuna directory kama hii,: {target_folder}")
    print("ebu check vizuri kama umecopy path vizuri.Hiyo inaeza kuwa issue")
    # We exit here coz the folder isnt there's so why bother
    exit()
except PermissionError:
    #this shows up if you don't have permission to access the folder
    print(f"hapa most probably nikama hauna permission za ku access folder,{target_folder}.")
    exit()

files_moved = 0

# We loop through every item that was found kwa target folder
for item_name in all_files:
    # Get the FULL path to the item
    item_path = os.path.join(target_folder, item_name)

    # Check if it's a file, NOT a folder.
    if not os.path.isfile(item_path):
        continue

   #here is where all the magic happens,the function below will take for fullname of the item i.e schoolfees.pdf and slit into "schoolfees" and ".pdf"
    file_name, file_extension = os.path.splitext(item_name)
    file_extension = file_extension.lower()  # Make it lowercase

    # Check if this extension is in the dictionary
    if file_extension in type_of_file:

        # Get the name of the new folder, e.g., "PDFs"
        destination_folder_name = type_of_file[file_extension]
        # Create the full path for the new folder, e.g., "C:\Users\Sanchez\Downloads\PDFs"
        destination_folder_path = os.path.join(target_folder, destination_folder_name)


        # Create the folder if it doesn't exist.
        os.makedirs(destination_folder_path, exist_ok=True)

        try:

            shutil.move(item_path, destination_folder_path)
            print(f"✅ wagwan: {item_name}  -->  {destination_folder_name}/")
            files_moved += 1
        except Exception as e:
            print({e})

if files_moved == 0:
    print("Hakuna file nime move,,,i think iko sawa ebu check")

else:
    print(f"Next time organise yourself,nime move {files_moved} files.")


