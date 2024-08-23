[![Downloads](https://img.shields.io/github/downloads/ImPot8o/structure-block-generator/total.svg)](https://github.com/ImPot8o/structure-block-generator/releases)
# Minecraft Structure Block Size Limit Workaround

This Python script is a workaround for the 32x32x32 block size limit of Minecraft structure blocks by automatically generating multiple structure files and corresponding functions. It allows users to create larger structures by specifying the desired dimensions, name, namespace, and directories through a user-friendly GUI.

- This script generates a bunch of structures, and 2 mcfunctions. 
- The structures form a grid of structure blocks pre-configured to copy as large of an area as you want. You need to go through each one and all you have to do is click copy and then break the block. 
- The first mcfunction places and configures all the blocks.
- After you copy you're area, if you don't change the names in the structure blocks, you can use the second function to place the entire structure. Stand one block above where you placed the grid of structure blocks and run the place command and it will place it.



## Features

- Generates multiple structure files (NBT) to overcome the 32x32x32 block size limit
- Creates corresponding functions to place and configure the structure blocks in the Minecraft world
- Provides a user-friendly graphical interface for inputting parameters
- Allows users to specify custom dimensions, name, namespace, and directories for the generated files

## Requirements

- Python 3.10 (only one I've tested in)
- `nbtlib` library
- `tkinter` library

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:
```python
pip install nbtlib
```

## Usage

1. Run the script using the following command:
```python
python main.py
```
2. The graphical user interface (GUI) will open.
3. Enter the desired dimensions (width, height, depth) for your structure.
4. Provide a name for your structure.
5. (Optional) Enter a namespace for the structure blocks.
6. (Optional) Enter a suffix for the generated structure files.
7. Select the directory where you want to save the generated structure files.
8. Select the directory where you want to save the generated function files.
9. Click the "Generate" button to generate the structure files and functions.
10. The script will generate the necessary files and display a success message.

## Generated Files

- Structure Files: The script generates multiple NBT files containing structure_void blocks based on the specified dimensions. The files are saved in the selected structure directory.
- Function Files:
  - `place_structures.mcfunction`: This function file contains commands to place and configure the structure blocks in the Minecraft world. This automatically turns the structure blocks to save mode, creates the areas they need to save, and names them. all you need to do it hit save and break the block.
  - `place-<structure_name>.mcfunction`: This function file contains commands to place the structures using the `/place` command. It places the structures that are created with the first mcfunction.

## Limitations

- The script generates structure files containing only structure_void blocks for copying larger areas than structure block allow. It doesn't copy entities by default.
- The generated functions assume a specific relative position for placing the structures. You may need to adjust the coordinates in the functions based on your desired placement location.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Acknowledgments

- The script utilizes the `nbtlib` library for working with NBT files.
- The graphical user interface is created using the `tkinter` library.

Feel free to contribute, report issues, or suggest improvements!
