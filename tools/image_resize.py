from PIL import Image

from tools.path_and_name import der_path


def resize_image(path_to_image, max_size=500):
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
    img.save(f"{dir_path}/{file_name.split('.')[0]}_resized.jpg", format="jpeg", quality=50)

    return f"{dir_path}/{file_name.split('.')[0]}_resized.jpg"


if __name__ == '__main__':
    resize_image('/Volumes/big4photo/Downloads/KSP_017975_00031_0h.JPG', )
