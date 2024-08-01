# Minecraft Structure Block Size Limit Bypass

This Python script bypasses the 32x32x32 block size limit of Minecraft structure blocks by automatically generating multiple structure files and corresponding functions. It allows users to create larger structures by specifying the desired dimensions, name, namespace, and directories through a user-friendly GUI.

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

- The script generates structure files containing only structure_void blocks. You need to manually add your desired blocks and entities to the generated structures using a structure block editor or NBT editor.
- The generated functions assume a specific relative position for placing the structures. You may need to adjust the coordinates in the functions based on your desired placement location.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Acknowledgments

- The script utilizes the `nbtlib` library for working with NBT files.
- The graphical user interface is created using the `tkinter` library.

Feel free to contribute, report issues, or suggest improvements!
