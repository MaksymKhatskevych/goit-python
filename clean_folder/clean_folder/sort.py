import os
from pathlib import Path
import re
import sys
import shutil


def normalize(string):

    map = {ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G', ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', ord('ё'): 'jo', ord('Ё'): 'Jo', ord('ж'): 'zh', ord('Ж'): 'Zh', ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I', ord('й'): 'y', ord('Й'): 'Y', ord('к'): 'k', ord('К'): 'K', ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M', ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O', ord('п'): 'p', ord(
        'П'): 'P', ord('р'): 'r', ord('Р'): 'R', ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T', ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F', ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'Ts', ord('ч'): 'ch', ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh', ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ы'): 'y', ord('Ы'): 'Y', ord('ь'): '', ord('Ь'): '', ord('ъ'): '', ord('Ъ'): '', ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'ju', ord('Ю'): 'Ju', ord('я'): 'Ja', ord('Я'): 'Ja', }
    lat_str = string.translate(map)
    fixed_str = re.sub(r'\W', "_", lat_str)
    return fixed_str


def sort(p):

    os.chdir(directory)
    music_formats = ('.mp3', '.ogg', '.waw', '.amr')
    image_formats = ('.jpeg', '.png', '.jpg', '.pdf')
    document_formats = ('.doc', '.docx', '.txt',
                          '.pdf', '.xls', '.pptx', '.xlsx')
    archieve_formats = ('.zip', '.gz', '.tar')
    video_formats = ('.avi', '.mp4', '.mov')
    if p.is_dir():
        for item in p.iterdir():
            sort(item)
        try:
            print('Удаленно:', p.name)
            os.removedirs(p)
        except PermissionError:
            pass
        except FileNotFoundError:
            pass


    else:
        file_name = p.stem
        formats = os.path.splitext(p)[1]
        if formats in music_formats:
            os.makedirs(directory + "\\music", exist_ok=True)
            move(p, directory + "\\music" + normalize(file_name) + formats)
        elif formats in image_formats:
            os.makedirs(directory + "\\image", exist_ok=True)
            move(p, directory + "\\image\\" +
                 normalize(file_name) + formats)
        elif formats in document_formats:
            os.makedirs(directory + "\\document", exist_ok=True)
            move(p, directory + "\\document\\" +
                 normalize(file_name) + formats)
        elif formats in video_formats:
            os.makedirs(directory + "\\video", exist_ok=True)
            move(p, directory + "\\video\\" +
                 normalize(file_name) + formats)
        elif formats in archieve_formats:
            os.makedirs(directory + "\\archieve", exist_ok=True)
            unpack_archive(p, directory + "\\archieve\\")




def main():

    global directory
    directory = sys.argv[1]
    path = Path(sys.argv[1])
    sort(path)



if __name__ == '__main__':
    main()
