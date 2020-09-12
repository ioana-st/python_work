import os
from bs4 import BeautifulSoup

path = "C:\\python\\files"

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".htm")):
            file_path = os.path.join(root,file)
            print("Last read file was:", file_path)
            with open (file_path, encoding="utf-8") as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                tables = soup.find_all('table')
                if tables:
                    for table in tables:
                        if table.find_all('tr', bgcolor='#694ED6') or table.find_all('tr', bgcolor='#694ed6') or table.find_all('td', bgcolor='#694ED6') or table.find_all('td', bgcolor='#694ed6') or table.find_all('tr', bgcolor='#6A4FD6') or table.find_all('tr', bgcolor='#6a4fd6') or table.find_all('td', bgcolor='#6A4FD6') or table.find_all('td', bgcolor='#6a4fd6') or soup.find_all('tr', class_=lambda value: value and value.startswith('t1st')):
                            table['class']='MyTableWithHeaders'
                        else:
                            if (table.find_all('tr', bgcolor='#F2F2F2') or table.find_all('td', bgcolor='#F2F2F2')) and len(table.find_all('tr')) == 1:
                                table['class']='MyInputTable'
                            else:
                                if table.find_all('tr', bgcolor='#F2F2F2') and len(table.find_all('tr')) > 1:
                                    table['class']='MyTableWithoutHeaders'
                                else:
                                    if table.find_all('caption'):
                                        table['class'] ='MyCaptionTable'
                                    else:
                                        if (table.find_all('tr', attrs={'bgcolor': None}) and table.find_all('td', attrs={'bgcolor': None})) or table.find_all('p', attrs={'class': 'FM_StepNo1'}) or table.find_all('p', attrs={'class': 'FM_StepNumber'}) or table.find_all('p', attrs={'class': 'FM_SubStep'}):
                                            table['class']='MyProcedureTable'
                                        else:
                                            print("There is an undentified table type in: ", file_path)
                    with open(file_path, 'w') as output_file:
                        try:
                            output_file.write(str(soup))
                            print("Change in:", file_path)
                        except:
                            print("Encoding error in ", file_path)