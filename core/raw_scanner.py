import os

SUPPORTED_EXTENSIONS = {'.CR2', '.CR3', '.NEF', '.ARW', '.RAF', '.DNG'}

def scan_directory(path):
    """
    Scans a directory for supported RAW files.
    Returns a list of absolute file paths.
    """
    raw_files = []
    if not os.path.isdir(path):
        return []

    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1].upper()
            if ext in SUPPORTED_EXTENSIONS:
                raw_files.append(os.path.join(root, file))
    
    return raw_files

def is_raw_file(file_path):
    """Check if a specific file is a supported RAW format."""
    ext = os.path.splitext(file_path)[1].upper()
    return ext in SUPPORTED_EXTENSIONS
