import os
import re

def fix_unicode_escapes(directory):
    """Fix Unicode escape sequences in all files"""
    replacements = {
        'u00e7': 'ç',  # c with cedilla
        'u00f6': 'ö',  # o with diaeresis
        'u00fc': 'ü',  # u with diaeresis
        'u011f': 'ğ',  # g with breve
        'u0131': 'ı',  # dotless i
        'u015f': 'ş',  # s with cedilla
        'u00c7': 'Ç',  # C with cedilla
        'u00d6': 'Ö',  # O with diaeresis
        'u00dc': 'Ü',  # U with diaeresis
        'u011e': 'Ğ',  # G with breve
        'u0130': 'İ',  # I with dot above
        'u015e': 'Ş',  # S with cedilla
    }
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.md', '.ini')):
                file_path = os.path.join(root, file)
                try:
                    # Read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Replace all occurrences of Unicode escape sequences
                    for escape_seq, char in replacements.items():
                        content = content.replace(escape_seq, char)
                    
                    # Write the fixed content
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"Fixed: {file_path}")
                except Exception as e:
                    print(f"Error: {file_path} - {e}")

if __name__ == "__main__":
    # Fix all files in the current directory
    fix_unicode_escapes('.')