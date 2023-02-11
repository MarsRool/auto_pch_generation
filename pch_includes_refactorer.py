

import re
from files_list import file_matches_filter


def clean_includes(files_list: list, includes_to_clean_regex: set, ext_filters: list):
    def is_acceptable(line: str):
        for include_to_clean_regex in includes_to_clean_regex:
            if re.match(include_to_clean_regex, line) != None:
                return False
        return True

    for file_path in files_list:
        if not file_matches_filter(file_path, ext_filters):
            return
        with open(file_path, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()

            for line in lines:
                if is_acceptable(line):
                    f.write(line)
