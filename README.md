# Welcome to Auto Pch Generation!

This is project for auto generation precompiled header `pch.h`.
The script `main.py` collects all external includes from all files with specific extensions (ex. .h, .hpp, .c, .cpp) in the source directory and creates the `pch.h` file.
Also, the script can clean unnecessary includes.

# Usage
usage: python main.py [-h] [-d DIR [DIR ...]] [-ext EXTENSIONS] [--pch PCH]
                      [--clean_includes CLEAN_INCLUDES [CLEAN_INCLUDES ...]]

options:
  -h, --help            show this help message and exit
  -d DIR [DIR ...], --dir DIR [DIR ...]
                        echo directory absolute path or pathes where to perform script
  -ext EXTENSIONS, --extensions EXTENSIONS
                        echo included extensions separated by semicolon, default are 'h;hpp;c;cpp'
  --pch PCH             echo pch filename, default is 'pch.h'
  --clean_includes CLEAN_INCLUDES [CLEAN_INCLUDES ...]
                        echo includes you want to clear if it's necessary

# Use Examples
The script use example with single argument - absolute path to source directory.
`python main.py --dir "C:\Path\To\Project\src\"`

The script use example with several source directories
`python main.py --dir "C:\Path\To\Some\Project\src\" "C:\Path\To\Another\Project\src\"`

The script use example with custom extensions to perform - with `.h` and `.cpp` only
`python main.py --dir "C:\Path\To\Project\src\" -ext "h;cpp"`

The script use example with cleaning `global.h` and `pch.h` includes
`python main.py --dir "C:\Path\To\Project\src\" --clean_includes '#include \"global.h\"' '#include \"pch.h\"'`
