import os
from bs4 import BeautifulSoup

path = "C:\\python\\files"

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".htm")):
            file_path = os.path.join(root,file)
            relpath = os.path.relpath('path = "C:\\work\\tablestyles"', root) # Calculates the relative path between the current file and the folder where the CSS file is stored.
            with open (file_path, encoding="utf-8") as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                tables = soup.find_all('table')
                if tables:
                    my_tables = soup.find_all('table', class_=lambda value: value and value.startswith('MyTable')) # Selects all tables with a class that starts with MyTable (i.e. both MyTableWithHeaders and MyTableWithoutHeaders).
                    if my_tables:
                        if relpath == '.':
                            css_url = 'MyNewStyle.css' # If the HTML file is in the same folder as the CSS file, the URL is just the name of the CSS.
                        else:
                            css_url=os.path.join(relpath,'MyNewStyle.css').replace("\\","/") # If the HTML is in a different folder than the CSS file, the URL is the relative path to the CSS file (using \ because that's what Flare expects). 
                        table_style = 'mc-table-style: url(\''+ css_url +'\');' # Creates a style in Flare format.           
                        for table in misys_tables: # Adds the class and style to the table.
                            table['class'] = 'TableStyle-MyNewStyle'
                            table['style'] = table_style
                    with open(file_path, 'w') as output_file:
                            output_file.write(str(soup))
