import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def run(script_name):
    script_path = BASE_DIR / "scripts" / script_name
    print(f"\nRunning {script_name}...")

    result = subprocess.run([sys.executable, str(script_path)])

    if result.returncode != 0:
        print(f"{script_name} failed.")
        sys.exit(1)

    print(f"{script_name} completed successfully.")

def main():
    print("Starting Healthcare API Data Pipeline...")

    run("extract.py")
    run("transform.py")
    run("validate.py")
    run("load.py")

    print("\nHealthcare API pipeline completed successfully.")

if __name__ == "__main__":
    main()