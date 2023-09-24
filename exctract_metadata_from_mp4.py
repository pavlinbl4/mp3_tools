

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser



def extract_mp4_cover(path_to_media_file):
    # Open video file with hachoir
    parser = createParser(path_to_media_file)
    metadata = extractMetadata(parser)

    print(metadata)

    # # Get the cover art
    # cover = metadata.get('thumbnail')
    # if cover is not None:
    #     with open("cover.jpg", "wb") as f:
    #         f.write(cover)
    #
    # print("Cover image extracted and saved as cover.jpg")

if __name__ == '__main__':
    extract_mp4_cover('/Volumes/big4photo/Movies/Youtube/Роман "Тайна булавки". Эдгар Уоллес./Эдгар Уоллес. Тайна булавки. Главы 1-3..mp4')