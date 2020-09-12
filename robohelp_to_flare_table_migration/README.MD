# RoboHelp to Flare Table Migration

## Background
The scripts in this section are based on the BeautifulSoup4 library and were used in a RoboHelp to Flare migration. 

One part of the challenge came from the fact that RoboHelp does not use <thead> and <tbody> tags and Flare needs those tags to properly apply its flavor of table styles. The other part of the challenge came from the inconsistency of the styles used in the RoboHelp projects being migrated.

## Scripts
The main scripts are meant to be used in sequence:
* **1_identify_table.py**

Most tables in the input files set did not have any class tags applied, so this script identifies each type of table based on a set of criteria, then applies the correct class. The classes are then used for two purposes: to decide whether the tables need headers and to choose the correct Flare stylesheet to associate.

* **2_add_thead_tbody.py**

This script applies <thead>, <th> and <tbody> tags to the tables; depending on the classes set by the first script, some tables get a heading row and some don't.

* **3_replace_table_tag.py**

In Flare, each table style is defined in a separate CSS file. For Flare to be able to apply a style to a table, the table needs to have a class (called `Table-NameOfCSS`) and a style (in the format `mc-table-style: url('relative_path_to_CSS_file')`). Because the files with tables may be at various levels of the hierarchy, the script calculates the relative path from the HTML file to the CSS file, then applies the Flare class and style to each table that has a specific class.

The other scripts were used for troubleshooting:
* **search_for_undefined_tables.py** - outputs the number of tables that do *not* have a specific class applied
* **find_mismatched_tbody.py** - outputs a list of tables that have <tbody> tags without </tbody> or the other way around (to asses the damage after a bad search and replace)