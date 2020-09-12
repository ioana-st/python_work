import os
from bs4 import BeautifulSoup

path = "C:\\python\\files"

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".htm")):
            file_path = os.path.join(root,file)
            relpath = os.path.relpath('path = "C:\\work\\tablestyles"', root)
            with open (file_path, encoding="utf-8") as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                tables = soup.find_all('table')
                if tables:
                    my_tables = soup.find_all('table', class_=lambda value: value and value.startswith('MyTable'))
                    if my_tables:
                        if relpath == '.':
                            css_url = 'MyNewStyle.css'
                        else:
                            css_url=os.path.join(relpath,'MyNewStyle.css').replace("\\","/")
                        table_style = 'mc-table-style: url(\''+ css_url +'\');'                
                        for table in misys_tables:
                            table['class'] = 'TableStyle-MyNewStyle'
                            table['style'] = table_style
                    with open(file_path, 'w') as output_file:
                            output_file.write(str(soup))
                            print("Change in:", file_path)
