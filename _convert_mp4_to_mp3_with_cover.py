from tools.mp3_converter import convert_mp4_to_mp3
from tools.add_cover_to_mp3 import add_mp3_cover
from tools.extract_mp4_cover import get_mp4_cover
from tools.filename_or_extension import cut_off_extension_from_filename
from tools.files_work import find_files
from tools.tk_tools import select_folder_via_gui


def main():
    #  select folder with files
    folder_with_files = select_folder_via_gui('/Users/evgeniy/Movies/Youtube')

    # find files to convert
    mp4_files_list = find_files(folder_with_files, extension='mp4')

    # cycle to work with files
    for mp4_file in mp4_files_list:
        filenane_no_extension = cut_off_extension_from_filename(mp4_file)

        # create path to files
        mp4_file_path = f"{folder_with_files}/{mp4_file}"
        mp3_file_path = f"{folder_with_files}/{filenane_no_extension}.mp3"
        jpg_file_path = f"{folder_with_files}/{filenane_no_extension}_cover.jpg"

        # convert file to mp3
        convert_mp4_to_mp3(mp4_file_path, mp3_file_path)

        # get cover from file
        get_mp4_cover(mp4_file_path)

        # add cover to mp3
        add_mp3_cover(jpg_file_path, mp3_file_path)

    return "work completed"


if __name__ == '__main__':
    print(main())
