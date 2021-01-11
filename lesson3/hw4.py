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
other_files = []



audio_file_format = ('MP3', 'OGG', 'WAV', 'AMR')
image_file_format = ('JPEG', 'PNG', 'JPG')
video_file_format = ('AVI', 'MP4', 'MOV')
documents_file_format = ('DOC', 'DOCX', 'TXT')


for file in files:
    if file.endswith('.mp3') or file.endswith('ogg') or file.endswith('.wav') or file.endswith('.amr'):
        music.append(file)          
    elif file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
        images.append(file)
    elif file.endswith('.avi') or file.endswith('.mp4') or file.endswith('.mov'):
        video.append(file)
    elif file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt'):
        documents.append(file)
    else:
        other_files.append(file)              

    


   
    
print(f"Base directory {files}")
print("_____________________________________")
print(f"music: {music}")
print(f"images: {images}")
print(f"video: {video}")
print(f"documents: {documents}") 
print(f"other_files: {other_files}") 	          
