import re
import json


def process_file(file_path):
    result = []

    # Open the file and process each line
    with open(file_path, "r") as file:
        for line in file:
            # Strip leading/trailing spaces and newlines
            original = line.strip()

            if original:  # Only process non-empty lines
                # Use regex to keep Unicode letters and spaces
                processed = (
                    re.sub(r"[^\w\s]", "", original, flags=re.UNICODE)
                    .lower()
                    .replace(" ", "")
                )

                # Append the pair to the result list
                result.append([original, processed])

    return result


# Specify the path to your text file
file_path = "at.txt"

# Process the file and print the result
output = process_file(file_path)
print(json.dumps(output, ensure_ascii=False))
