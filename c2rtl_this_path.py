import os
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor

# Base path to search for .c files
base_path = "./"

# Function to convert a file path to a legal project name
def convert_to_legal_name(file_path):
    return re.sub(r'[^a-zA-Z0-9_]', '_', file_path)

# Function to generate TCL script content
def generate_tcl_script(project_name, c_file):
    tcl_content = f"""
open_project -reset {project_name}
set_top fn1
add_files {c_file}
open_solution -reset solution1
set_part {{xcvu9p-flga2104-2-i}}
create_clock -period 10
csynth_design
export_design
close_solution
close_project
exit
"""
    return tcl_content

# Function to execute TCL script
def run_tcl_script(tcl_script_path):
    command = f"vitis_hls -f {tcl_script_path}"
    print(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Output for {tcl_script_path}:\n{result.stdout}")
        print(f"Errors for {tcl_script_path}:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {tcl_script_path}:\n{e.stderr}")

# Function to process each .c file
def process_c_file(c_file_path):
    project_name = convert_to_legal_name(c_file_path)
    tcl_script_path = os.path.join(os.path.dirname(c_file_path), f"run_hls_{project_name}.tcl")

    # Generate and save the TCL script
    tcl_content = generate_tcl_script(project_name, c_file_path)
    with open(tcl_script_path, "w") as tcl_file:
        tcl_file.write(tcl_content)

    # Print the file being processed and the TCL script content
    print(f"Processing file: {c_file_path}")
    print(f"TCL script content for {c_file_path}:\n{tcl_content}")

    # Run the TCL script
    run_tcl_script(tcl_script_path)

# Main script
if __name__ == "__main__":
    c_files = []

    # Collect all .c files
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".c"):
                c_files.append(os.path.join(root, file))
            if file.endswith(".cpp"):
                c_files.append(os.path.join(root, file))

    # Check if any .c files were found
    if not c_files:
        print("No .c files found in the specified path.")
    else:
        print(f"Found {len(c_files)} .c files.")

    # Process .c files in parallel
    with ThreadPoolExecutor() as executor:
        executor.map(process_c_file, c_files)
