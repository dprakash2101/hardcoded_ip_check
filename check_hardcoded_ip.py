import re
import os


ip_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')


directories_to_check = os.getenv("DIRECTORIES", ".").split(",")

print(f"Directories to check: {directories_to_check}")

user_extensions = os.getenv("EXTENSIONS", "").split(",")
print(f"User-provided extensions: {user_extensions}") 

default_extensions = [".cs", ".py", ".js", ".json", ".java", ".ts"]

combine_with_default = os.getenv("COMBINE_EXTENSIONS", "false").lower() == "true"
print(f"Combine with default: {combine_with_default}")

"""
If user mention false extension types will not be combined other wise they will be combine
"""
if combine_with_default == "true":
    combine_with_default = True
elif combine_with_default == "false":
    combine_with_default = False
else:
    combine_with_default = True 

# Determine the final list of extensions to check
if user_extensions == [""]:  # If no user-provided extensions
    extensions_to_check = default_extensions  # Use default extensions
else:
    if combine_with_default:
        extensions_to_check = default_extensions + user_extensions  # Combine defaults + user extensions
    else:
        extensions_to_check = user_extensions  # Use only user-provided extensions

# Remove any duplicates in extensions_to_check and strip any extra whitespace
extensions_to_check = list(set(ext.strip() for ext in extensions_to_check if ext))
print(f"Final list of extensions to check: {extensions_to_check}")

files_with_ips = []

def search_file_for_ips(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = ip_regex.findall(content)
        if matches:
            return True
    return False

def check_directories():
    for directory in directories_to_check:
        directory = directory.strip()
        print(f"Checking directory: {directory}")
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in extensions_to_check):
                    file_path = os.path.join(root, file)
                    print(f"Checking file: {file_path}")
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
