import os
import re


def file_matches_filter(filename: str, ext_filters: list) -> bool:
    if len(ext_filters) == 0:
        return True

    ext = os.path.splitext(filename)[1]
    for ext_filter in ext_filters:
        if re.search(ext_filter, ext) != None:
            return True
    return False


def get_files_list(walk_dir: str, ext_filters: list):
    files_list = []
    for root, _, files in os.walk(walk_dir):

        for filename in files:
            if file_matches_filter(filename, ext_filters):
                # print('filename: ' + filename)
                files_list.append(os.path.join(root, filename))
            else:
                print('--!-- filename doesn\'t match: ' + filename)
    return files_list


def get_files_list_except_pch(files_list: list, pch_filename: str):
    result = []
    for file_path in files_list:
        if re.search(pch_filename, file_path) == None:
            result.append(file_path)
    return result
