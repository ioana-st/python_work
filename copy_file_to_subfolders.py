import os, shutil

def copy_file_to_subfolders():
	# IN CASE YOU WANT TO HARDCODE THE LOCATIONS, UNCOMMENT THE FOLLOWING 2 LINES AND SET IS_HARDCODED TO True
	# source_file = "D:\ioana\ehlpdhtm.js"
	# file_dest = r"D:\ioana\help_builds\value_72\mergedProjects"
	is_hardcoded = False
	if not is_hardcoded:
		# get file to copy
		is_file = False
		is_folder = False
		while not is_file:
			source_file = input(r"What file do you want to copy? Input a full location (e.g. C:\work\file.js).")
			if not os.path.isfile(source_file):  # check if the path you entered is actually a file
				print("That's not a valid file. Please try again.")
			else:
				is_file = True
		# get location to whose subfolders to copy
		while not is_folder:
			file_dest = input(r"To the subfolders of which parent folder do you want to copy the file? Input a full location (e.g. C:\work).")
			if not os.path.isdir(file_dest): # check if the path you entered is actually a folder
				print("That's not a valid folder. Please try again.")
			else:
				is_folder = True
	subdirs = os.listdir(file_dest)
	subdirs = [os.path.join(file_dest,subdir) for subdir in subdirs if os.path.isdir(os.path.join(file_dest,subdir))]
	for subdir in subdirs:
		shutil.copy(source_file, subdir)