import re
import os


ip_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# Get directories from the environment variable
directories_to_check = os.getenv("DIRECTORIES", ".").split(",")

# File extensions to check
extensions_to_check = [".cs", ".py", ".js", ".json"]

files_with_ips = []

def search_file_for_ips(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Find all IP addresses
        matches = ip_regex.findall(content)
        if matches:
            return True
    return False

def check_directories():
    for directory in directories_to_check:
        directory = directory.strip()
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in extensions_to_check):
                    file_path = os.path.join(root, file)
                    if search_file_for_ips(file_path):
                        files_with_ips.append(file_path)

if __name__ == "__main__":
    check_directories()

    if files_with_ips:
        print(f"Hardcoded IPs found in the following files: {files_with_ips}")
        exit(1)
    else:
        print("No hardcoded IPs found.")
        exit(0)
