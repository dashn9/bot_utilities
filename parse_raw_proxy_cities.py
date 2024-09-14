import re
import json
import unicodedata


def normalize_string(s):
    """Normalize a string to pure English a-z characters."""
    if not isinstance(s, str):
        return s

    # Convert to lowercase
    s = s.lower()

    # Remove non-word characters except for space
    s = re.sub(r"\W+", "", s)

    # Normalize Unicode characters to ASCII
    s = unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode("ASCII")

    return s


def process_file(file_path):
    result = []

    # Open the file and process each line
    with open(file_path, "r") as file:
        for line in file:
            # Strip leading/trailing spaces and newlines
            original = line.strip()

            if original:  # Only process non-empty lines
                # Use regex to keep Unicode letters and spaces
                processed = normalize_string(original)

                # Append the pair to the result list
                result.append([original, processed])

    return result


# Specify the path to your text file
file_path = "at.txt"

# Process the file and print the result
output = process_file(file_path)
print(json.dumps(output, ensure_ascii=False))
