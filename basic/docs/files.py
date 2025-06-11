# r = Read
# a = Append
# w = Write
# x = Create

from os import path, remove, getcwd

# get directory
current_directory = getcwd()
print(f"Current Directory: {current_directory}")

# f = open(current_directory + '/basic/docs/names.txt', 'r')
# print(f.read(40)) # Read the first 40 characters from the file
# print("___________________")
# print(f.readline()) # Read the first line from the file
# print("___________________")
# for line in f:
#     print(line.strip())  # Read the file line by line and strip whitespace
# f.close() # Close the file after reading
# print("___________________")

# Error handling example
# Attempt to open a file that does not exist
# try:
#     f = open("names.txt", 'r')  # Attempt to open a file that does not exist
# except:
#     print(f"Error: File not found.")
# finally:
#     f.close()  # Ensure the file is closed if it was opened
# print("___________________")
class FileHandler:
  """A class to handle basic file operations."""
  
  def __init__(self, file_path):
    self.file_path = file_path
    self.file = None

  def open_file(self, mode='r'):
    """Open a file with the specified mode."""
    self.file = open(self.file_path, mode)
    return self.file

  def read(self):
    """Read the content of the file."""
    if self.file:
      return self.file.read()
    else:
      raise ValueError("File is not opened.")

  def write(self, content):
    """Write content to the file."""
    if self.file:
      self.file.write(content)
    else:
      raise ValueError("File is not opened.")

  def close(self):
    """Close the file."""
    if self.file:
      self.file.close()
      self.file = None
    else:
      raise ValueError("File is not opened.")

  def file_exists(self):
    """Check if a file exists."""
    return path.isfile(self.file_path)
  
  def delete_file(self):
    """Delete a file if it exists."""
    if path.isfile(self.file_path):
      remove(self.file_path)
    else:
      raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        

def get_file_size(file_path):
    """Get the size of a file in bytes."""
    if path.isfile(file_path):
        return path.getsize(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
def get_file_name(file_path):
    """Get the name of the file from its path."""
    return path.basename(file_path)
def get_file_extension(file_path):
    """Get the file extension from its path."""
    return path.splitext(file_path)[1]
def get_file_directory(file_path):
    """Get the directory of the file from its path."""
    return path.dirname(file_path)
def get_file_info(file_path):
    """Get basic information about a file."""
    if path.isfile(file_path):
        return {
            'size': f"{get_file_size(file_path)} bytes",
            'name': get_file_name(file_path),
            'extension': get_file_extension(file_path),
            'directory': get_file_directory(file_path)
        }
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

# FILE_DIR = current_directory + '/basic/docs/names.txt'

# file = FileHandler(FILE_DIR)
# file.open_file()
# readfile = file.read()
# print(readfile)
# file.close()
# print("___________________")

# append_file = FileHandler(FILE_DIR)
# append_file.open_file('a')
# append_file.write(f"\nNew line added to the {get_file_name(FILE_DIR)}.")
# append_file.close()
# # Reopen the file to read the updated content
# file = FileHandler(FILE_DIR)
# file.open_file()
# readfile = file.read()
# print(readfile)
# file.close()
# print(get_file_info(FILE_DIR))
# print("___________________")

# write(overwrite) file
# ANOTHER_FILE_DIR = current_directory + '/basic/docs/context.txt'
# file = FileHandler(ANOTHER_FILE_DIR)
# file.open_file('w')
# file.write("Overwritten content in the file.\n")
# file.close()
# # Reopen the file to read the updated content
# file.open_file()
# readfile = file.read()
# print(readfile)
# file.close()
# print("file exists:", file.file_exists())
# print("___________________")

CREATE_FILE_DIR = current_directory + '/basic/docs/tanvir.txt'
createFileHandler = FileHandler(CREATE_FILE_DIR)
createFileHandler.open_file('x')  # 'x' mode to create a new file
createFileHandler.write("This is a new file created with 'x' mode.\n")
createFileHandler.close()
# Reopen the file to read the content
createFileHandler.open_file()
readfile = createFileHandler.read()
print(readfile)
createFileHandler.close()
print(f"{get_file_name(CREATE_FILE_DIR)} file exists:", createFileHandler.file_exists())
print("___________________")
# delete file
try:
  deleteFileHandler = FileHandler(CREATE_FILE_DIR)
  deleteFileHandler.delete_file()
  print(f"File {get_file_name(CREATE_FILE_DIR)} deleted successfully.")
except FileNotFoundError as e:
  print(e)
finally:
  if deleteFileHandler.file_exists():
    deleteFileHandler.close()
print(f"{get_file_name(CREATE_FILE_DIR)} file exists:", deleteFileHandler.file_exists())
print("___________________")