import os
from bs4 import BeautifulSoup

def is_bullet(paragraph):
    if paragraph['class'] == ['FM_Bullet']:
        return True
    else:
        return False


path = 'C:\\work\\test_files'

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith('.htm')):
            file_path = os.path.join(root,file)
            with open (file_path, encoding='utf-8') as soup_html:
                soup = BeautifulSoup(soup_html, 'lxml')
                paras = soup.find_all('p')
                for i, p in enumerate(paras):
                    if is_bullet(p):
                        if (i > 0 and not is_bullet(paras[i-1])) or i == 0: # If it's the first bullet in this list...
                            ul = soup.new_tag('ul') # ...make a new unordered list
                            p.insert_after(ul) # ...and add it after the current paragraph
                        li = soup.new_tag('li')
                        li.append(p)
                        ul.append(li) # Make the paragraph into a list item and add it to the unordered list
            with open(file_path, 'w') as output_file:
                output_file.write(str(soup))