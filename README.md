# Welcome to Auto Pch Generation!

This is project for auto generation precompiled header `pch.h`.
The script `main.py` collect all external includes from all files with specific extensions (ex. .h, .hpp, .c, .cpp) in the source folder and creates the `pch.h` file.

# Use Example
The script accepts single arcument - absolute path to source folder.
`python main.py "C:\Path\To\ProjectFolder\src\"`

# Notes
In the `main.py` there is commented lines, which clear all `pch.h` and `global.h` includes.
This is special feature for projects where such includes are everywhere.