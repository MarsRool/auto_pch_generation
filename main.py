

import sys

from files_list import get_files_list, get_files_list_except_pch
from includes_analyzer import get_external_includes
from pch_creator import create_pch_file
from pch_includes_refactorer import clean_includes

default_extensions = [r'\.h', r'\.hpp', r'\.c', r'\.cpp']
default_pch_filename = 'pch.h'


def input():
    if len(sys.argv) == 1:
        print("invalid script use")
        return
    walk_dir = sys.argv[1]
    # ext_filters = sys.argv[2] if len(sys.argv) > 2 else []
    ext_filters = default_extensions
    return (walk_dir, ext_filters)


def main():
    walk_dir, ext_filters = input()
    files_list = get_files_list(walk_dir, ext_filters)
    print("files list count=", len(files_list))

    external_includes = get_external_includes(
        get_files_list_except_pch(files_list, default_pch_filename))
    print("external includes count=", len(external_includes))

    create_pch_file(external_includes, walk_dir, default_pch_filename)
    print("pch file created")

    # uncomment to clean unnecessary global and pch includes
    # clean_includes(files_list, {r'#include "global.h"', r'#include "pch.h"'}, default_extensions)
    # print("headers cleared from global and pch files")


if __name__ == '__main__':
    main()
