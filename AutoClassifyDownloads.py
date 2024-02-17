import os # function for interacting with the operating system
import shutil # function for file operations
import time

# Specify Downloads Directory
dirDownloads = "C:/Users/jmkd-/Downloads"

# Mapping Files Extensions to Foldes names
extensions = {
    "txt" : "TextFiles",
    "jpg" : "Images",
    "jpeg" : "Images",
    "pdf" : "PDFs",
    "png" : "Images",
    "mp4" : "Videos",
    "mp3" : "Audios",
    "exe" : "Applications(exe)"
}

# function to classify and move files
def classifyAndMove(fileName):
    _, extension = os.path.splitext(fileName) # split the file name into base name and extension
    extension = extension[1:].lower() # remove dots and convert to lower

    if extension in extensions:
        folder = os.path.join(dirDownloads, extensions[extension]) 
        os.makedirs(folder, exist_ok=True) #create destination folder if not exist
        shutil.move(os.path.join(dirDownloads, fileName), os.path.join(folder, fileName))
        
        print(f"Moved {fileName} to {folder}") # print a message for confirmation

# Monitoring Downloads Directory
def monitorDownloadsDir():
    while True:
        for fileName in os.listdir(dirDownloads):
            if os.path.isfile(os.path.join(dirDownloads, fileName)):
                classifyAndMove(fileName)
        time.sleep(1)


# Start Monitoring Downloads Directory
if __name__ == "__main__":
    monitorDownloadsDir()
