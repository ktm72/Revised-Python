from os import path

def list_files_in_directory(directory_path):
    """List all files in a directory."""
    if path.isdir(directory_path):
        return [f for f in path.listdir(directory_path) if path.isfile(path.join(directory_path, f))]
    else:
        raise NotADirectoryError(f"The path {directory_path} is not a directory.")
def copy_file(source_path, destination_path):
    """Copy a file from source to destination."""
    if path.isfile(source_path):
        with open(source_path, 'rb') as src_file:
            with open(destination_path, 'wb') as dest_file:
                dest_file.write(src_file.read())
    else:
        raise FileNotFoundError(f"The source file {source_path} does not exist.")
def move_file(source_path, destination_path):
    """Move a file from source to destination."""
    if path.isfile(source_path):
        copy_file(source_path, destination_path)
        delete_file(source_path)
    else:
        raise FileNotFoundError(f"The source file {source_path} does not exist.")
def rename_file(old_name, new_name):
    """Rename a file."""
    if path.isfile(old_name):
        if not path.isfile(new_name):
            move_file(old_name, new_name)
        else:
            raise FileExistsError(f"The file {new_name} already exists.")
    else:
        raise FileNotFoundError(f"The file {old_name} does not exist.")
def create_directory(directory_path):
    """Create a new directory."""
    if not path.exists(directory_path):
        path.makedirs(directory_path)
    else:
        raise FileExistsError(f"The directory {directory_path} already exists.")
def delete_directory(directory_path):
    """Delete a directory if it exists and is empty."""
    if path.isdir(directory_path):
        if not path.listdir(directory_path):
            path.rmdir(directory_path)
        else:
            raise OSError(f"The directory {directory_path} is not empty.")
    else:
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")
