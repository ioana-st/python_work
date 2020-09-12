import os

path = "C:\\python\\files"

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".htm")):
            file_path = os.path.join(root,file)
            with open (file_path, encoding="utf-8") as html_file:
                html_content=html_file.read()
                opening = html_content.count("<tbody>") # The number of <tbody> tags in the file.
                closing = html_content.count("</tbody>") # The number of </tbody> tags in the file.
                if opening != closing: # If the number of opening tags is different from the number of closing tags, there is a malformed table in the file.
                    print(file_path)