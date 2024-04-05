import subprocess
import os

def run_python_scripts(start=1, end=19):
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
