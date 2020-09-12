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
                    for table in tables: # The tables in the input RoboHelp files were defined inconsistently, so the script tries to figure out what class they were supposed to have.
                        if table.find_all('tr', bgcolor='#694ED6') or table.find_all('td', bgcolor='#694ED6') or table.find_all('tr', bgcolor='#6A4FD6') or table.find_all('td', bgcolor='#6A4FD6') or soup.find_all('tr', class_=lambda value: value and value.startswith('t1st')):
                            table['class']='MyTableWithHeaders'
                            # Some tables had a violet header row. The header row was either defined using a class that started with "t1st" (if the RoboHelp style had been applied correctly) or was defined through inline formatting on the td or tr tag, using one of two close-but-not-identical shades of violet.
                        else:
                            if (table.find_all('tr', bgcolor='#F2F2F2') or table.find_all('td', bgcolor='#F2F2F2')) and len(table.find_all('tr')) == 1:
                                table['class']='MyInputTable'
                                # Input tables were used for formulas and had exactly one row and grey background applied on either tr or td. 
                            else:
                                if table.find_all('tr', bgcolor='#F2F2F2') and len(table.find_all('tr')) > 1:
                                    table['class']='MyTableWithoutHeaders'
                                    # Basic tables did not have any violet rows, had more than one row and had at least one row with a grey background.
                                else:
                                    if table.find_all('caption'):
                                        table['class'] ='MyCaptionTable'
                                        # Tables with captions always contained a caption tag.
                                    else:
                                        if (table.find_all('tr', attrs={'bgcolor': None}) and table.find_all('td', attrs={'bgcolor': None})) or table.find_all('p', attrs={'class': 'FM_StepNo1'}) or table.find_all('p', attrs={'class': 'FM_StepNumber'}) or table.find_all('p', attrs={'class': 'FM_SubStep'}):
                                            table['class']='MyProcedureTable'
                                            # Procedure tables either did not have any background, or had a background but also contained paragraphs with specific classes.
                                        else:
                                            print("There is an undentified table type in: ", file_path)
                                            # Just in case there are no weird tables that do not match any of the other criteria...
                    with open(file_path, 'w') as output_file:
                        output_file.write(str(soup))