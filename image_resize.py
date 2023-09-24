from PIL import Image
from pathlib import Path


def der_path(path_to_image):
    # Using pathlib.Path.parent
    file_name = Path(path_to_image).name
    dir_path = Path(path_to_image).parent
    return file_name, dir_path


def resize_image(path_to_image, max_size=200):
    img = Image.open(path_to_image)

    # Get the width and height of the image
    width, height = img.size

    # Calculate the new height and width to maintain aspect ratio
    if width > height:
        ratio = height / width
        new_width = max_size
        new_height = int(new_width * ratio)
    else:
        ratio = width / height
        new_height = max_size
        new_width = int(new_height * ratio)

    # Resize with thumbnail
    img.thumbnail((new_width, new_height))

    file_name, dir_path = der_path(path_to_image)

    # Save resized image
    img.save(f"{dir_path}/{file_name}_resized.jpg")

    return f"{dir_path}/{file_name}_resized.jpg"


if __name__ == '__main__':
    resize_image('/Volumes/big4photo/Movies/Youtube/Роман "Тайна булавки". Эдгар Уоллес./thumb.jpg', )
