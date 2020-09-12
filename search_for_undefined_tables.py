import os
from bs4 import BeautifulSoup

path = "C:\\python\\files"


total_non_class_tables = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".htm")):
            file_path = os.path.join(root,file)
            with open (file_path, encoding="utf-8") as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                non_class_tables_in_file = soup.find_all('table', class_=lambda value: value and value.startswith('MyClass'))
            total_non_class_tables = total_non_class_tables + len(non_class_tables_in_file)
print(total_non_class_tables)