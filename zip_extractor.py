import zipfile

def extract_file(filepath, dest_dir):
    #dest dir is short for destination directory
    with zipfile.ZipFile(filepath, 'r') as file:
        file.extractall(dest_dir)

    
