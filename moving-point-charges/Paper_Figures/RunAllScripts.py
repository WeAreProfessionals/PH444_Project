"""
The Script below has been created by us (PH444 Project Group 8) to make it easier for anyone to 
execute the Code Completely without having to run each file individually. This Script is basically
used to sequentially run the the python files that generate Figures1 till Figure20 (Images plus 
Animations) used in the Presentation. It takes 8+ Hours to run on an AMD Ryzen 7 5800HS 3.201GHz 
8 core CPU.

To run on you device locally, you need to install the following dependencies on your system:
1. ffmpeg: It is a free and open source software project that offers many tools for video and audio 
processing. This is required to process the animations on matplotlib.
2. BibTeX: BibTeX is both a bibliographic flat-file database file format and a software program for 
processing these files to produce lists of references. This is used to process the latex fonts in the
python scripts.
3. Install any python libraries such as numpy, math, matplotlib, scipy that are imported in any of the 
python files.
"""


import subprocess
import os

def run_python_scripts(start=1, end=20):
    for i in range(start, end + 1):
        script_name = f"{os.path.dirname(os.path.realpath(__file__))}\Figure{i}.py"
        print(f"Running {script_name}...")

        # Check if the script file exists
        if not os.path.exists(script_name):
            print(os.getcwd())
            print(f"File {script_name} not found. Skipping.")
            continue

        # Run the script
        try:
            subprocess.run(["python", script_name], check=True)
            print(f"{script_name} completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running {script_name}: {e}")

if __name__ == "__main__":
    run_python_scripts()
 