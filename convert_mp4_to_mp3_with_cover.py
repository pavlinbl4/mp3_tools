from converter.mp3_converter import convert_mp4_to_mp3
from tools.files_work import find_files
from tools.tk_tools import select_folder_via_gui


def main():

    #  select folder with files
    folder_with_files = select_folder_via_gui('/Movies/Youtube')

    # find files to convert
    mp4_files_list = find_files(folder_with_files, extension='mp4')

    # cycle to work with files
    for mp4_file in mp4_files_list:

        # create path to file


        # convert file to mp3
        convert_mp4_to_mp3(mp4_file_path, mp3_file_path)








if __name__ == '__main__':
    print(main())