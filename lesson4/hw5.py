import os
import sys
import pathlib


print("___________________________________________________________________________")
"""Sorted file lists"""
music = []
images = []
video = []
documents = []
other_files = []


def recursyve(path):
    if path.is_dir():
        print(f"Name folders: {path}---> {os.listdir(path)}")
        for i in os.listdir(path):
            if i == files:
                sort(files)
    
        for fold in path.iterdir():      
            recursyve(fold)
            


            
def sort():
   
    audio_file_format = ('MP3', 'OGG', 'WAV', 'AMR')
    image_file_format = ('JPEG', 'PNG', 'JPG')
    video_file_format = ('AVI', 'MP4', 'MOV')
    documents_file_format = ('DOC', 'DOCX', 'TXT')

    audio_file_format = [(el.lower()) for el in audio_file_format]
    image_file_format = [(el.lower()) for el in image_file_format]
    video_file_format = [(el.lower()) for el in video_file_format]
    documents_file_format = [(el.lower()) for el in documents_file_format]
    my_files = files.copy()
    my_files = [(z.lower()) for z in my_files]

    for i in range(len(my_files)):
        if my_files[i].split('.')[-1] in audio_file_format:
            music.append(files[i])
        elif my_files[i].split('.')[-1] in image_file_format:
            images.append(files[i])
        elif my_files[i].split('.')[-1] in video_file_format:
            video.append(files[i])
        elif my_files[i].split('.')[-1] in documents_file_format:
            documents.append(files[i])
        else:
            other_files.append(files[i])
    
    print(f"music: {music}")
    print(f"images: {images}")
    print(f"video: {video}")
    print(f"documents: {documents}") 
    print(f"other_files: {other_files}")




def main():
    """main function"""
    global files
    path = sys.argv[1]
    path = pathlib.Path(path)
    files = os.listdir(path)
    recursyve(path)
    sort()
    print(f"Base directory {path}")
    print("_____________________________________")

if __name__ in "__main__":
    main()    



    
 