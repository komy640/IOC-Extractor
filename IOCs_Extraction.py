import re
import sys
from tabulate import tabulate

# Define regex patterns
PATTERNS = {
    "IP Addresses": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
    "Email Addresses": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "URLs": r'https?://[^\s"\']+',
    "Executable Files": r'(?:[A-Za-z]:\\|/)?(?:[\w\-\.]+[\\/])*[\w\-\.]+\.(?:exe|bat|bin|sh|ps1|scr|cmd)',
    "Windows Registry Keys": r'HKEY_LOCAL_MACHINE\\[\w\\]+',
    "MD5 Hashes": r'\b[a-fA-F0-9]{32}\b',
    "SHA-1 Hashes": r'\b[a-fA-F0-9]{40}\b',
    "SHA-256 Hashes": r'\b[a-fA-F0-9]{64}\b'
}

def display_banner():
    banner = r"""
############################################################################
  ______   _   _  __
 |  ____| | | | |/ /  ___  _  _   _   _   _           
 | |__    | | | ' /  / _ \| '_ \/\ \ | | | |   
 |  __|   | | |  <  | (_) | | | | | || |_| |        
 | |____  | | | . \  \___/|_| |_| |_| \__, |  
 |______| |_| |_|\_\                  ___| |
                                     |_____|  

This tool efficiently parses large files to identify and extract critical indicators of compromise (IOCs) including IP addresses, email addresses, URLs, executable files, registry keys, and cryptographic hashes  
############################################################################
"""
    print(banner)
    print("==> Extracting Artifacts - By k0my <==")
    print("=" * 50)

def extract_artifacts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Extract artifacts
        extracted_data = {category: set(re.findall(pattern, content, re.IGNORECASE)) for category, pattern in PATTERNS.items()}

        # Save results to a file
        output_file = "extracted_artifacts.txt"
        with open(output_file, 'w', encoding='utf-8') as out:
            for category, items in extracted_data.items():
                if items:
                    out.write(f"\n{category}:\n")
                    for i, item in enumerate(items, 1):
                        out.write(f"{i}. {item}\n")

        # Print extracted data in tabular format
        for category, items in extracted_data.items():
            if items:
                print(f"\n{category}:")
                table_data = [[i+1, item] for i, item in enumerate(items)]
                print(tabulate(table_data, headers=["#", category], tablefmt="grid"))

        print(f"\nExtracted artifacts saved in {output_file}")

    except FileNotFoundError:
        print("\nError: File not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    display_banner()

    # Allow interactive file input if no argument is given
    if len(sys.argv) != 2:
        file_path = input("Enter the path of the file: ").strip()
    else:
        file_path = sys.argv[1]

    extract_artifacts(file_path)
