import re


default_external_include_regex = r'#include\s+<.*>'


def get_external_includes(files_list: list, external_include_regex=default_external_include_regex):
    external_includes = set()
    for file_path in files_list:
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                for line in f:
                    if line in external_includes:
                        continue
                    result = re.match(external_include_regex, str(line))
                    if result != None:
                        # print("found new external include: " + line, "in file: " + file_path)
                        external_includes.add(line)
        except UnicodeDecodeError:
            print(f"Error in get external includes: file {file_path} cannot be decoded by utf-8!")
    return external_includes
