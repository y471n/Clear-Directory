import glob
import os

def main():

	file_type = '*.mp3'
	working_directory = '.'
 	all_file_types = getFileTypes(working_directory)        

	for file_type in all_file_types: 
		extension = '.' + file_type

		file_directory_name = make_directory(extension, working_directory)
		move_to_directory(file_directory_name, working_directory, extension)

def getFileTypes(working_directory):
	file_types = []
	for item in os.listdir(working_directory):
		if os.path.isfile(item):
		    file_type = item.split('.')[-1]
		    if file_type not in file_types:
			file_types.append(file_type)
	
	return file_types


def make_directory(file_type, working_directory):

	directory_exists = 'false'
	file_directory_name = file_type.split('.')[1]
	file_directory_name = file_directory_name + '_files'

	# Check if directory to store files already exists
	for item in os.listdir(working_directory):
		if os.path.isdir(item) and item.lower() == file_directory_name.lower():
				directory_exists = 'true'

	# If directory does not exists make the directory
	if directory_exists != 'true':
		print 'Created a new directory : ' + file_directory_name
		os.mkdir(file_directory_name.lower())
	
	return file_directory_name

def move_to_directory(file_directory_name, working_directory, file_type):
	type_of_files = '*' + file_type
	for item in glob.glob(type_of_files):
		destination = working_directory + '/' + file_directory_name + '/' + item
		if not os.path.exists(destination):
			os.rename(item,destination)
			print 'Moved file: ' + item + ' to ' + destination
		else:
			print os.getcwd() + destination[1:] + " file already exists, not moving"
		
    	
if __name__ == '__main__':
	main()
