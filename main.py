import os
from config import info
import time

#log info
print(f' author: {info["author"]} \n version: {info["version"]} \n program name: {info["program_name"]} \n description: {info["description"]} \n gitHub link: {info["gitHub_link"]}')

#open documentation
print('read documentation befre use')
time.sleep(1)
try:
	os.startfile(os.getcwd() + '/documentation.txt')
except:
	print(f'i not found the documentation')
#selecting a folder
papka = input("please specify the full path to the folder where you want to sort files: ")
papka = papka + "/"


#creating folders
if not os.path.isdir(papka + "img"):
     os.mkdir(papka + "img")
if not os.path.isdir(papka + "text_files"):
     os.mkdir(papka + "text_files")
if not os.path.isdir(papka + "audio"):
     os.mkdir(papka + "audio")
if not os.path.isdir(papka + "programs"):
     os.mkdir(papka + "programs")
if not os.path.isdir(papka + "video"):
     os.mkdir(papka + "video")
if not os.path.isdir(papka + "archives"):
     os.mkdir(papka + "archives")

#main process
for i in os.listdir(path=papka):
	#log files
	print(i)
	#sorting text files
	if '.txt' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	elif '.doc' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	elif '.docm' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	elif '.docx' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	elif '.pdf' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	elif '.dotx' in i:
		os.replace(papka + i, papka + '/text_files/' + i)
	elif '.rtf' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	elif '.xml' in i:
		os.replace(papka + i, papka + 'text_files/' + i)
	#sorting images
	elif '.png' in i:
		os.replace(papka + i, papka + 'img/' + i)
	elif '.jpg' in i:
		os.replace(papka + i, papka + 'img/' + i)
	elif '.jpeg' in i:
		os.replace(papka + i, papka + 'img/' +  i)
	elif '.gif' in i:
		os.replace(papka + i, papka + 'img/' + i)
	elif '.webp' in i:
		os.replace(papka + i, papka + 'img/' + i)
	#sorting archives
	elif '.zip' in i:
		os.replace(papka + i, papka + 'archives/' + i)
	elif '.rar' in i:
		os.replace(papka + i, papka + 'archives/' + i)
	#sorting programs
	elif '.exe' in i:
		os.replace(papka + i, papka + 'programs/' + i)
	elif '.msi' in i:
		os.replace(papka + i, papka + 'programs/' + i)
	#sorting music
	elif '.mp3' in i:
		os.replace(papka + i, papka + 'audio/' + i)
	elif '.waw' in i:
		os.replace(papka + i, papka + 'audio/' + i)
	#sorting video
	elif '.mp4' in i:
		os.replace(papka + i, papka + 'video/' + i)
	elif '.avi' in i:
		os.replace(papka + i, papka + 'video/' + i)
	elif '.wmv' in i:
		os.replace(papka + i, papka + 'video/' + i)
	elif '.mpg' in i:
		os.replace(papka + i, papka + 'video/' + i)


print('i have sorted all file \nif forgot somethink please sorted self, bye')
input('press Enter to end the program')