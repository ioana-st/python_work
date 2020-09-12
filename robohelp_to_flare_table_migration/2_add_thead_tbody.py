import os
from bs4 import BeautifulSoup

path = "C:\\python\\files"

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".htm")):
            file_path = os.path.join(root,file)
            with open (file_path, encoding="utf-8") as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                tables = soup.find_all('table')
                if tables: 
                    tables_with_header = soup.find_all('table', class_='MyTableWithHeaders') # Selects all tables with the class MyTableWithHeaders in the current file.
                    if tables_with_header: 
                        for table in tables_with_header:
                            rows = table.find_all('tr') # Select all the rows in the current table.
                            header_row = rows[0] # The header row is always the first row.
                            body_rows = rows[1:] # The body rows are always all the rows except the first one.
                            for child in header_row.find_all('td'):
                                child.name = 'th' # All the td tags in the header row are transformed into th tags.
                            thead = soup.new_tag('thead')
                            header_row.wrap(thead) # The header row is wrapped in <thead> </thead>
                            tbody = soup.new_tag('tbody')
                            for body_row in body_rows:
                                body_row.wrap(tbody) # Each body row is wrapped in <tbody> </tbody>...
                                tbody_row = table.find('tbody') # ...then the entire tbody is selected...
                                table.append(tbody_row.extract()) # ...then extracted from its previous position and added after the thead row.
                    tables_without_header = soup.find_all('table', class_='MyTableWithoutHeaders') # Select all tables with the class MyTableWithoutHeaders in the current file.
                    if tables_without_header:
                        for table in tables_without_header:
                            body_rows = table.find_all('tr') # Same steps, except without creating a thead.
                            tbody = soup.new_tag('tbody')
                            for body_row in body_rows:
                                body_row.wrap(tbody)
                                tbody_row = table.find('tbody')
                                table.append(tbody_row.extract())
                    with open(file_path, 'w') as output_file:
                        output_file.write(str(soup))