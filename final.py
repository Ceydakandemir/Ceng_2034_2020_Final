#CEYDA NUR KANDEMİR

# !!! YOU SHOULD OPEN A NEW FOLDER AND RUN IT IN THE FOLDER !!!

import os
import requests
from hashlib import md5
from multiprocessing import Pool
import uuid
from itertools import product

def childProcess():
	child = os.fork()
	if(child>0):
		print("Parent process is ", os.getpid())
		os.wait()
	elif(child==0):
		print("Child process is ", os.getpid())
		return True
		
def downloadFile(url, file_name = None):
	r = requests.get(url, allow_redirects= True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)
		
		
def hashCode(photo):
	with open(photo, "rb") as p:
		photoHash = md5(p.read()).hexdigest()
	return photoHash


def find_duplicates(h, h2):

	if h[0] != h2[0]:
		if h[1] == h2[1]:
			print(h[0]," And ", h2[0]," are the same.")

def multiProc_download_duplicates():
	if (childProcess() == True):
		
		processPool = Pool()

		url = [
			"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
			"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
			"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
			"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
			"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg" ]
		
		print("Files are downloading...")
		processPool.map(downloadFile, url)
		print("All files are downloaded..")
		

		
		currentDirectory = os.listdir()

		
		filteredCurrentDirectory = []
		
		for item in currentDirectory:
			if item == "final.py":
				pass
			else:
				filteredCurrentDirectory.append((item, hashCode(item)))

		processPool.starmap(find_duplicates, product(filteredCurrentDirectory, repeat=2))
	
	


multiProc_download_duplicates()
	

	
	





	





	



	





	


