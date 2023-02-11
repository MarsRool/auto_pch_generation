
import os
import re


default_external_include_regex = r'#include\s+<(.*)>'


def create_pch_file(external_includes: set, out_dir: str, pch_filename,
                    external_include_regex=default_external_include_regex):
    file_path = os.path.join(out_dir, pch_filename)
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write('#pragma once\n\n')

        def is_lower(string): return re.search(
            external_include_regex, string).group(1).islower()

        lowercase_letter_includes = [
            i for i in external_includes if is_lower(i)]
        uppercase_letter_includes = [
            i for i in external_includes if not is_lower(i)]
        lowercase_letter_includes.sort()
        uppercase_letter_includes.sort()
        if len(lowercase_letter_includes) > 0:
            lowercase_letter_includes.append('\n')
        f.writelines(lowercase_letter_includes)
        f.writelines(uppercase_letter_includes)
