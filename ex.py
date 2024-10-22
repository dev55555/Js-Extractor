import os

# Define the file containing the URLs
file = "js.txt"

# Specify the directory where you want to save the files
download_directory = "js"

# Create the directory if it doesn't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Open the file and read each line
with open(file, "r") as f:
    for link in f:
        # Strip any leading/trailing whitespace characters (like newlines)
        link = link.strip()
        # Define the command to download the file into the specified directory
        os.system(f"wget -P {download_directory} {link}")
