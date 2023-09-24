import customtkinter
from tkinter import filedialog
import os
from pathlib import Path

from tools.main_modul import work_with_file


def gui_window():
    root_tk = customtkinter.CTk()  # tkinter.Tk()  # create the Tk window like you normally do

    window_width = 600
    window_height = 340
    screen_width = root_tk.winfo_screenwidth()
    screen_height = root_tk.winfo_screenheight()
    x = int(screen_width / 4)
    y = int(screen_height / 2 - window_height / 2)
    root_tk.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root_tk.title("Convert video mp4 files to mp3 audio")

    customtkinter.set_appearance_mode("Dark")
    home_folder = Path().home()

    folders_paths = {1: f'{home_folder}/Downloads', 2: f'{home_folder}/Music'}

    def choose_folder_1():

        folder_path = filedialog.askdirectory(initialdir=f'{home_folder}/Downloads')
        if folder_path != '':
            folders_paths[1] = folder_path
        text1 = customtkinter.CTkTextbox(root_tk, fg_color='transparent', width=500, height=10)
        text1.place(relx=0.1, rely=0.2)
        text1.insert(customtkinter.END, f'Source path - {folders_paths[1]}')
        return

    def choose_folder_2():
        folder_path = filedialog.askdirectory(initialdir=f'{home_folder}/Music')
        if len(folder_path) > 1:
            folders_paths[2] = folder_path
        text2 = customtkinter.CTkTextbox(root_tk, fg_color='transparent', width=500, height=10)
        text2.place(relx=0.1, rely=0.5)
        text2.insert(customtkinter.END, f'Destination path - {os.path.abspath(folders_paths[2])}')
        return

    def choose_folder_3():
        work_with_file(folders_paths, 'mp4', 'mp3')
        root_tk.destroy()

    button1 = customtkinter.CTkButton(master=root_tk,
                                      height=40,
                                      width=300,
                                      corner_radius=10,
                                      fg_color=("black", "gray"),  # <- tuple color for light and dark theme
                                      text="Select folder with files to convert",
                                      command=choose_folder_1)
    button1.place(relx=0.5, rely=0.1, anchor='center')

    text1 = customtkinter.CTkTextbox(root_tk, fg_color='transparent')
    text1.place(relx=0.2, rely=0.2)
    text1.insert(customtkinter.END, f'Default path - {folders_paths[1]}')

    button2 = customtkinter.CTkButton(master=root_tk,
                                      height=40,
                                      width=300,
                                      corner_radius=10,
                                      fg_color=("black", "gray"),  # <- tuple color for light and dark theme
                                      text="Select destination folder",
                                      command=choose_folder_2)
    button2.place(relx=0.5, rely=0.4, anchor='center')

    text2 = customtkinter.CTkTextbox(root_tk, fg_color='transparent')
    text2.place(relx=0.2, rely=0.5)
    text2.insert(customtkinter.END, f'Default path - {folders_paths[2]}')

    button3 = customtkinter.CTkButton(master=root_tk,
                                      height=40,
                                      width=500,
                                      corner_radius=10,
                                      fg_color=("red", "gray"),  # <- tuple color for light and dark theme
                                      text="Convert it",
                                      command=choose_folder_3)
    button3.place(relx=0.5, rely=0.8, anchor='center')

    root_tk.mainloop()
    return folders_paths


if __name__ == '__main__':
    gui_window()
