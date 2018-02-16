import os

def rename_files():
	table = str.maketrans(dict.fromkeys('0123456789'))
	path = os.getcwd() + "\images"
	file_list = os.listdir(r"" + path)

	os.chdir(path)

	for file_name in file_list:	
		os.rename(file_name,file_name.translate(table))
		
rename_files()