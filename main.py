import os
from config import info
import time

print(f' author: {info["author"]} \n version: {info["version"]} \n program name: {info["program_name"]} \n description: {info["description"]} \n gitHub link: {info["gitHub_link"]}')

print(f'read documentation before use')
time.sleep(2)
try:
	os.startfile(os.getcwd() + '/documentation.txt')
except:
	print(f'i not found the documentation')
print("if you have already read the documentation click Enter")
input()
if not os.path.isdir("img"):
     os.mkdir("img")
if not os.path.isdir("text_files"):
     os.mkdir("text_files")
if not os.path.isdir("archives"):
     os.mkdir("archives")
if not os.path.isdir("programs"):
     os.mkdir("programs")
if not os.path.isdir("audio"):
     os.mkdir("audio")
for i in os.listdir(path=os.getcwd()):
	print(i)
	if '.txt' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.doc' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.docm' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.docx' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.pdf' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.dotx' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.dotm' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.rtf' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.xml' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/text_files/' + i)
	elif '.png' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/img/' + i)
	elif '.jpg' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/img/' + i)
	elif '.gif' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/img/' + i)
	elif '.webp' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/img/' + i)
	elif '.zip' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/archives/' + i)
	elif '.rar' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/archives/' + i)
	elif '.exe' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/programs/' + i)
	elif '.msi' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/programs/' + i)
	elif '.mp3' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/audio/' + i)
	elif '.waw' in i:
		os.replace(os.getcwd() + '/' + i, os.getcwd() + '/audio/' + i)

print('i have sorted all file \n if forgot somethink please sorted self, bye')