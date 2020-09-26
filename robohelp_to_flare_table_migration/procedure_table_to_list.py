import os
from bs4 import BeautifulSoup

path = 'C:\\work\\test_files'

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith('.htm')):
            file_path = os.path.join(root,file)
            with open (file_path, encoding='utf-8') as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                proc_tables = soup.find_all('table', class_='Procedure')
                for table in proc_tables:
                    tds = table.find_all('td')
                    i = 0
                    useful_tds = []
                    ol = soup.new_tag('ol')
                    for td in tds:
                        if i % 2 != 0:
                           useful_tds.append(td) # Get the second cell of every row
                        i = i + 1
                    if useful_tds:
                        table.insert_after(ol) # Make a new ordered list
                        for useful_td in useful_tds:
                            li = soup.new_tag('li')
                            paras = useful_td.find_all('p') 
                            for p in paras:
                                p.wrap(li) # Wrap all the paragraphs found inside the cell in a single <li> 
                            ol.append(li) # Add the <li> to the ordered list
                        table.extract()
            with open(file_path, 'w') as output_file:
                output_file.write(str(soup))