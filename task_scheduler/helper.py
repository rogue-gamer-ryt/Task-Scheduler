#   Purpose: Helper files to write common functions

import os
import shutil
from os import listdir
from os.path import isfile, join


class FileTypes:
    def __init__(self) -> None:
        self.Documents = [".doc", ".docx", ".pdf"]
        self.Installers = [".exe", ".msi"]
        self.Images = [".png", ".jpg", ".jpeg"]


def shift_files(path: str) -> None:
    """
    This is a sample script to clean up a folder based on the file extensions

    Args:
        path (str): path of the folder

    Returns:
        None
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    filetypes = FileTypes()
    file_type_variation_list = []
    for key, value in filetypes.__dict__.items():
        new_folder = path + '\\' + str(key)

        for file in files:
            filename, file_extension = os.path.splitext(file)
            src_path = path + "/" + file
            if file_extension in value:
                src_path = path + "/" + file
                dest_path = new_folder + "/" + file
                if os.path.isdir(new_folder):  # folder exists
                    pass
                else:
                    os.mkdir(new_folder)
                shutil.move(src_path, dest_path)

            else:
                file_type_variation_list.append(file_extension)
                new_folder_name = path + '/' + file_extension + '_folder'
                if os.path.isdir(new_folder_name):  # folder exist
                    pass
                else:
                    os.mkdir(new_folder_name)
                shutil.move(src_path, new_folder_name)
