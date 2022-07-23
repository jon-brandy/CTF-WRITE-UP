import os
import tarfile

os.system("clear") 

# for loop from 1000 to 0, decrementing by 1
for i in range(1000, 0, -1): 
	filename = str(i) + '.tar' #Get the name of the file
	result = tarfile.open(filename) #Open the file
	result.extractall() # extract all the files
	result.close() #Close the file
