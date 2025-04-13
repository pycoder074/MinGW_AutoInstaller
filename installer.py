import requests
import zipfile
import os
from pathlib import Path
import subprocess
import winreg as reg

# URL of the file you want to download
url = 'https://github.com/brechtsanders/winlibs_mingw/releases/download/14.2.0posix-19.1.7-12.0.0-msvcrt-r3/winlibs-x86_64-posix-seh-gcc-14.2.0-mingw-w64msvcrt-12.0.0-r3.zip'

# Define the default Downloads directory dynamically
downloads_folder = str(Path.home() / "Downloads")
zip_path = os.path.join(downloads_folder, 'winlibs.zip')

# Sending GET request
print('Sending get request...')
r = requests.get(url, verify=False)

# Check if the request was successful
if r.status_code == 200:
    print('Request success')
    # Save the content as winlibs.zip
    with open(zip_path, 'wb') as f:
        f.write(r.content)
    print("File downloaded and saved as winlibs.zip")
else:
    print(f"Failed to download file, status code: {r.status_code}")

# Extracting the ZIP file
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(downloads_folder)  # Extract to default Downloads folder
    print(f'Extracted to {downloads_folder}')
except zipfile.BadZipFile:
    print("Error: The file is not a valid ZIP file.")
except Exception as e:
    print(f"Error during extraction: {e}")


