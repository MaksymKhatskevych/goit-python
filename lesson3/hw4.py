import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

music = []
images = []
video = []
documents = []
other_files =[]



audio_file_format = {".mp3", ".ogg", ".wav", ".amr"}
image_file_format = {".jpeg",".png", ".jpg"}
video_file_format = {".avi", ".mp4", ".mov"}
documents_file_format = {".doc", ".docx",".txt"}



for file in files:
    if 'jpeg' in file or 'png' in file or 'jpg' in file:
        images.append(file)

    elif 'avi' in file or 'mp4' in file or 'mov' in file:
        video.append(file)

    elif 'doc' in file or 'docx' in file or 'txt' in file:
        documents.append(file)

    elif 'mp3' in file or 'ogg' in file or 'wav' in file or 'amr' in file :
        music.append(file)

    else:
        other_files.append(file)

   
    
print(f"Base directory {files}")
print("_____________________________________")
print(f"music: {music}")
print(f"images: {images}")
print(f"video: {video}")
print(f"documents: {documents}")	          
