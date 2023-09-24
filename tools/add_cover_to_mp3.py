from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

from tools.image_resize import resize_image


def load_image(path_to_image):
    # resize image
    # path_to_resized_image = resize_image(path_to_image)

    # Load the resized image

    with open(path_to_image, 'rb') as r_img_in:
        r_img_data = r_img_in.read()

    return r_img_data


def add_mp3_cover(path_to_image, path_to_media_file):
    mp3file = MP3(path_to_media_file, ID3=ID3)

    img_data = load_image(path_to_image)

    # Add the image as album art
    mp3file.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime='image/jpeg',  # image/jpeg or image/png
            type=3,  # 3 is for the cover image
            desc='Cover',
            data=img_data
        )
    )
    # Save the changes
    mp3file.save()


if __name__ == '__main__':
    add_mp3_cover('/Users/evgeniy/Movies/Youtube/Mamedov Reads/Усталый путник, отдохни  Джон Уиндэм_cover.jpg',
                  '/Users/evgeniy/Movies/Youtube/Mamedov Reads/Усталый путник, отдохни  Джон Уиндэм.mp3')
