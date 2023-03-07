

import sys
import argparse

from files_list import get_files_list, get_files_list_except_pch
from includes_analyzer import get_external_includes
from pch_creator import create_pch_file
from pch_includes_refactorer import clean_includes

default_extensions = "h;hpp;c;cpp"
default_pch_filename = 'pch.h'


def parse_extensions(extensions_str: str):
    extensions = extensions_str.split(";")
    return ['\\\\.' + ext for ext in extensions]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, nargs='+', default=[])
    parser.add_argument("-ext", "--extensions", type=str, default=default_extensions,
                        help="echo included extensions separated by semicolon ;")
    parser.add_argument("--pch", type=str, default=default_pch_filename,
                        help="echo pch filename")
    parser.add_argument("--clean_includes", nargs='+', type=str, default=[],
                        help="echo includes you want to clear if it's necessary")
    args = parser.parse_args()

    walk_dirs = args.dir
    ext_filters = parse_extensions(args.extensions)
    pch_filename = args.pch
    includes_to_clean = args.clean_includes

    if len(walk_dirs) == 0:
        print("There is nothing to do")
        return

    print(f"starting processing with args extensions={ext_filters}\n",
          f"pch filename={pch_filename}\n",
          f"includes to clean{includes_to_clean}")

    for walk_dir in walk_dirs:
        print(f"processing: dir {walk_dir}")

        files_list = get_files_list(walk_dir, ext_filters)
        print("files list count=", len(files_list))

        external_includes = get_external_includes(
            get_files_list_except_pch(files_list, pch_filename))
        print("external includes count=", len(external_includes))

        create_pch_file(external_includes, walk_dir, pch_filename)
        print("pch file created")

        if len(includes_to_clean) > 0:
            clean_includes(files_list, set(includes_to_clean), ext_filters)
            print("headers cleared from global and pch files")


if __name__ == '__main__':
    main()
