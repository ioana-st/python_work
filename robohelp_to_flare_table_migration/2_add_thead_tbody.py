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
                    tables_with_header = soup.find_all('table', class_='MyTableWithHeaders')
                    if tables_with_header:
                        for table in tables_with_header:
                            rows = table.find_all('tr')
                            header_row = rows[0]
                            body_rows = rows[1:]
                            for child in header_row.find_all('td'):
                                child.name = 'th'
                            thead = soup.new_tag('thead')
                            header_row.wrap(thead)
                            tbody = soup.new_tag('tbody')
                            for body_row in body_rows:
                                body_row.wrap(tbody)
                                tbody_row = table.find('tbody')
                                table.append(tbody_row.extract())
                    tables_without_header = soup.find_all('table', class_='MyTableWithoutHeaders')
                    if tables_without_header:
                        for table in tables_without_header:
                            body_rows = table.find_all('tr')
                            tbody = soup.new_tag('tbody')
                            for body_row in body_rows:
                                body_row.wrap(tbody)
                                tbody_row = table.find('tbody')
                                table.append(tbody_row.extract())
                    with open(file_path, 'w') as output_file:
                        output_file.write(str(soup))
                        print("Change in:", file_path)