import os
import nbtlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def generate_structure(width, height, depth, name, namespace, structure_dir, function_dir, suffix, place_function_name):
    # Calculate the number of structure blocks needed
    x_blocks = (width + 31) // 32
    y_blocks = (height + 31) // 32
    z_blocks = (depth + 31) // 32

    # Create the structure directory if it doesn't exist
    if not os.path.exists(structure_dir):
        os.makedirs(structure_dir)

    # Generate the structure files
    for x in range(x_blocks):
        for y in range(y_blocks):
            for z in range(z_blocks):
                structure_name = f"{name}_{x}_{y}_{z}{suffix}"
                structure_file = os.path.join(structure_dir, f"{structure_name}.nbt")

                # Calculate the size of the current structure block
                block_width = min(32, width - x * 32)
                block_height = min(32, height - y * 32)
                block_depth = min(32, depth - z * 32)

                # Create an NBT structure with only structure_void blocks
                structure_data = nbtlib.File({
                    'DataVersion': nbtlib.Int(2865),  # Data version for 1.19.4
                    'size': nbtlib.List([
                        nbtlib.Int(block_width),
                        nbtlib.Int(block_height),
                        nbtlib.Int(block_depth)
                    ]),
                    'palette': nbtlib.List([
                        nbtlib.Compound({
                            'Name': nbtlib.String('minecraft:structure_void')
                        })
                    ]),
                    'blocks': nbtlib.List([
                        nbtlib.Compound({
                            'pos': nbtlib.List([nbtlib.Int(i), nbtlib.Int(j), nbtlib.Int(k)]),
                            'state': nbtlib.Int(0)
                        })
                        for i in range(block_width)
                        for j in range(block_height)
                        for k in range(block_depth)
                    ])
                })

                # Save the NBT data to a file
                structure_data.save(structure_file)

                print(f"Generated structure file: {structure_file}")

    # Generate a function to place and configure the structure blocks
    function_content = ""
    for x in range(x_blocks):
        for y in range(y_blocks):
            for z in range(z_blocks):
                structure_name = f"{name}_{x}_{y}_{z}{suffix}"
                structure_name_func = f"{namespace}:{name}_{x}_{y}_{z}{suffix}"
                block_width = min(32, width - x * 32)
                block_height = min(32, height - y * 32)
                block_depth = min(32, depth - z * 32)
                function_content += f"""
# Place and configure the structure block for {structure_name}
setblock ~{x * 32} ~{y * 32} ~{z * 32} minecraft:structure_block
data modify block ~{x * 32} ~{y * 32} ~{z * 32} mode set value SAVE
data modify block ~{x * 32} ~{y * 32} ~{z * 32} name set value "{structure_name_func}"
data modify block ~{x * 32} ~{y * 32} ~{z * 32} sizeX set value {block_width}
data modify block ~{x * 32} ~{y * 32} ~{z * 32} sizeY set value {block_height}
data modify block ~{x * 32} ~{y * 32} ~{z * 32} sizeZ set value {block_depth}
data modify block ~{x * 32} ~{y * 32} ~{z * 32} Position set value [{x * 32}, {y * 32}, {z * 32}]
"""

    # Save the function content to a file
    structure_name = f"{name}{suffix}"
    create_function_name = f"create-{structure_name}"
    function_file = os.path.join(function_dir, f"{create_function_name}.mcfunction")
    with open(function_file, 'w') as f:
        f.write(function_content)

    print(f"Generated function file: {function_file}")

    # Generate the second function to place the structures using /place command
    place_function_content = ""
    for x in range(x_blocks):
        for y in range(y_blocks):
            for z in range(z_blocks):
                structure_name = f"{name}_{x}_{y}_{z}{suffix}"
                structure_name_func = f"{namespace}:{name}_{x}_{y}_{z}{suffix}"
                place_function_content += f"""
# Place the structure for {structure_name}
place template {structure_name_func} ~{x * 32} ~{y * 32} ~{z * 32}
"""

    # Save the second function content to a file
    structure_name = f"{name}{suffix}"
    place_function_name = f"place-{structure_name}"
    place_function_file = os.path.join(function_dir, f"{place_function_name}.mcfunction")
    with open(place_function_file, 'w') as f:
        f.write(place_function_content)

    print(f"Generated second function file: {place_function_file}")


def browse_structure_directory():
    directory = filedialog.askdirectory()
    if directory:
        structure_dir_entry.delete(0, tk.END)
        structure_dir_entry.insert(0, directory)


def browse_function_directory():
    directory = filedialog.askdirectory()
    if directory:
        function_dir_entry.delete(0, tk.END)
        function_dir_entry.insert(0, directory)


def on_generate():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        depth = int(depth_entry.get())
        name = name_entry.get()
        namespace = namespace_entry.get()
        structure_dir = structure_dir_entry.get()
        function_dir = function_dir_entry.get()
        suffix = suffix_entry.get()
        place_function_name = ''

        if not name:
            messagebox.showerror("Error", "Name cannot be empty")
            return

        if not namespace:
            messagebox.showerror("Warning", "Namespace is empty. Will default to 'minecraft:'")

        if not structure_dir:
            messagebox.showerror("Error", "Structure directory cannot be empty")
            return

        if not function_dir:
            messagebox.showerror("Error", "Function directory cannot be empty")
            return

        generate_structure(width, height, depth, name, namespace, structure_dir, function_dir, suffix,
                           place_function_name)
        messagebox.showinfo("Success", "Structure files generated successfully")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid dimensions")


# Create the main window
root = tk.Tk()
root.title("Structure Generator")
root.geometry("600x350")

# Apply a style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TFrame", padding=10)
style.configure("TNotebook", font=("Helvetica", 12))
style.configure("TNotebook.Tab", font=("Helvetica", 12))

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create and place the widgets
ttk.Label(frame, text="Structure Width: (x)").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
width_entry = ttk.Entry(frame)
width_entry.grid(row=0, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Structure Height: (y)").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
height_entry = ttk.Entry(frame)
height_entry.grid(row=1, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Structure Depth: (z)").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
depth_entry = ttk.Entry(frame)
depth_entry.grid(row=2, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Structure Name:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = ttk.Entry(frame)
name_entry.grid(row=3, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Namespace: (optional, in structure block)").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
namespace_entry = ttk.Entry(frame)
namespace_entry.grid(row=4, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Suffix: (optional)").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
suffix_entry = ttk.Entry(frame)
suffix_entry.grid(row=5, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Structure Directory:").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
structure_dir_entry = ttk.Entry(frame)
structure_dir_entry.grid(row=7, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

browse_structure_button = ttk.Button(frame, text="Browse...", command=browse_structure_directory)
browse_structure_button.grid(row=7, column=2, padx=10, pady=5)

ttk.Label(frame, text="Function Directory:").grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
function_dir_entry = ttk.Entry(frame)
function_dir_entry.grid(row=8, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

browse_function_button = ttk.Button(frame, text="Browse...", command=browse_function_directory)
browse_function_button.grid(row=8, column=2, padx=10, pady=5)

generate_button = ttk.Button(frame, text="Generate", command=on_generate)
generate_button.grid(row=9, column=0, columnspan=3, pady=10)

# Start the main event loop
root.mainloop()
