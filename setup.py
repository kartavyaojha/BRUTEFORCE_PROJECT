import subprocess
import sys

def install_packages():
    packages = [
        'requests',
        'pyfiglet',
        'termcolor',
        'Flask'
    ]
    
    for package in packages:
        try:
            # Check if the package is already installed
            subprocess.check_call([sys.executable, '-m', 'pip', 'show', package])
            print(f"{package} is already installed.")
        except subprocess.CalledProcessError:
            # Install the package if not already installed
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

if __name__ == "__main__":
    install_packages()
    print("All dependencies have been installed.")
