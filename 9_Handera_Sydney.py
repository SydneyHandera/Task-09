###Aufgabe 9###
###TEAM WORK!!! Team members: Nele Münzberg, Sydney Handera, Jeannine Fuss###

#import necessary packages
import nltk
import numpy as np
from nltk import *
import nltk.tokenize
from nltk.probability import *
from nltk.draw import *	
import os
from os import listdir, path
from os.path import isfile, join
import glob
import sys
###data_path needs to be changed according to the user
###corpus used is the inaugural corpus from nltk plus the two speeches of Obama and Trump
###the corpus is saved from moodle

data_path = "/Users/Handera/Desktop/American-Inaugural-Address-Corpus-1961-2017/"

###saving whole corpus into a variable
for filename in glob.glob(os.path.join(data_path, '*.txt')): #save every file that ends with ".txt" into the variable "filename"
  with open(filename, 'r') as f: #open the files individually with a loop as "f"
    text = f.read() # read the files with read() into the variable "text"
    print (filename) #print the filenames to check if every file is read
    print (text) #print all the files as one whole text

###make all words lower case
words = [w.lower() for w in text]

###list of punctuation marks to exclude them in the corpus
pctmarks = [',','.','-','--',';',':','``','?','!','"','"','(',')','\\','']

###loop to extract only words without pctmarks
wordswopm = [w for w in words if w not in pctmarks]	# for loop to exclude words in our list from our corpus

###type-token ratio
###save the ttr to the variable "ttr"
ttr = len(set(wordswopm))/(len(wordswopm))
print(ttr*100) #multiply with 100 to get percentage


file = open("9_Handera_Sydney_TTR.txt", "w") #open a new file 
file.write(str(ttr)) #write the results of the ttr into the new file
#the ttr variable needs to be converted into a string with str()
file.close() #close the newly added file to finish


for filename in glob.glob(os.path.join(data_path, '*.txt')): #for loop same as above
	with open(filename, 'r') as f:
		file_content = f.read()
		tokens = word_tokenize(file_content) #tokenize the text, in this case saved in file_content

		textlist = nltk.Text(tokens) #save the tokenized text in "textlist"
		ttr = len(set(textlist))/(len(textlist)) #ttr with tokenized text


		with open('result_ttr.txt', 'a') as result_file: #a new file saving ttr of all individual texts
			tmpout = sys.stdout # temporary output equals the standard output

			sys.stdout = result_file # standard output is displayed in the result_file which is a txt file
		
			print (textlist) # everything which would be displayed in the console is written into the txt file(result_file) 
		
			print() # line
			
			print(ttr) #type-token ratio

			sys.stdout = tmpout



