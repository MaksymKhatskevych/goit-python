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

print(f"Base directory {files}")
print("_____________________________________") 


audio_file_format = [(el.lower()) for el in audio_file_format]
image_file_format = [(el.lower()) for el in image_file_format]
video_file_format = [(el.lower()) for el in video_file_format]
documents_file_format = [(el.lower()) for el in documents_file_format]


    
for file in files:
    
    if file.rsplit('.')[-1] in audio_file_format:
        music.append(file)
        
    elif file.rsplit('.')[-1] in image_file_format:
        images.append(file)
        
    elif file.rsplit('.')[-1] in video_file_format:
        video.append(file)
        
    elif file.rsplit('.')[-1] in documents_file_format:
        documents.append(file)
        
    else:
        other_files.append(file)        

print(f"music: {music}")
print(f"images: {images}")
print(f"video: {video}")
print(f"documents: {documents}") 
print(f"other_files: {other_files}")             
  
