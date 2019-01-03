import os, shutil, sys
from ftplib import FTP

# IN CASE YOU WANT TO HARDCODE THE LOCATIONS, UNCOMMENT THE FOLLOWING 2 LINES AND SET IS_HARDCODED TO True
source_file = r"D:\ioana\ehlpdhtm.js"
file_dest = r"/test/"
hardcoded = True

ftp = FTP("10.19.111.40")
try:
	print("Logging in...")
	# Replace the credentials with real ones
	ftp.login("user", "password")
except:
	print("Failed to login. Exiting.")
	sys.exit()

# If you don't want to use hardcoded values, ask for user input
if not hardcoded:
	is_file = False
	# Ask for the file to copy and make sure the input is a valid file
	while not is_file:
		source_file = str(input(r"What file do you want to copy? Input a full location (e.g. C:\work\file.js)."))
		if not os.path.isfile(source_file):
			print("That's not a valid file. Please try again.")
		else:
			is_file = True
	# Ask for the target folder on the FTP server and make sure the input is valid
	while True:
		file_dest = str(input(
			r"To the subfolders of which FTP folder do you want to copy the file? Input a location relative to the root of the server (e.g. /fusioncapital_sophis/help_72_/mergedProjects/."))
		try:
			ftp.cwd(file_dest)
			break
		except:
			print("That's not a valid folder. Please try again.")
else:
	ftp.cwd(file_dest)
try:
	ftp_content = ftp.nlst()
except:
	print("No files in directory (probably)")
for dir_target in ftp_content: # does not work if the folder contains files as well as folders
	dir_target = file_dest + "/" + dir_target
	ftp.cwd(dir_target)
	ftp.storbinary("STOR " + os.path.basename(source_file), open(source_file, 'rb'))
