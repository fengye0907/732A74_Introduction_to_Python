#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import sys
import os
import io
import re
import string
from nltk.corpus import stopwords
from collections import Counter

def main(argv):

    
     #main function that is been called at the end
  

   filepath =str(argv[1])
   
   

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   with io.open(filepath,encoding="utf-8") as f :
       data = f.read() 
   border_msg("Wellcome to text analyzer")
   print("\n")
   print("Take a moment while we calculate your results........")
   print("\n")
   CleanString=clean_file(data)
   #
   letters_frequency=letter_fr(CleanString)
   total_word_count=word_count(CleanString)
   unique_word_count=unique_words(CleanString)
   
   print("The frequency of letters are: ")
   print('Letter : Frequency')
   for key, value in sorted(letters_frequency.items(),key=lambda t: t[1],reverse=True):
       print("{0} : {1}".format(key, value))
   
   print("\n")   
   print("The number of words in the file is : ",total_word_count)
   print("\n")
   print("Number of unique words is: ",unique_word_count)
   print("\n")
   CommonFollowing=words_follow(CleanString,5,3)
   
   for key,value in CommonFollowing.items():
      print ("common word : {0} ".format(key))
      for val in value:
         print ("---follow word : {0}".format(val))
   
 
   

   try :
        print("\n")
        write_to_file(argv[2],letters_frequency,total_word_count,unique_word_count,CommonFollowing)
        time.sleep(1)
        print("\n")
        print("Your file is ready.")
   except:
        print("\n")
        print("Exiting text analyser...")
        time.sleep(3)
        sys.exit()

   

def clean_file(file):   


    #function that takes a string
    #and turns to lowercase,remove punctuation,
    #stop words and returns clean string


   stops = set(stopwords.words("english"))
   text=file.lower()
   #text=text.replace("“","")
   text=re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,*]", "", text)
   text_no_punctuation=(re.sub('[%s]' % string.punctuation,'',text))
   text_words=re.sub(r'[0-9]+', '', text_no_punctuation)
   #pattern = re.compile(r'\b(' + r'|'.join(StopWords) + r')\b\s*')
   #meaningfull_words = pattern.sub('', text_words)
   text_list=text_words.split()
   meaningful_words = [w for w in text_list if not w in stops]
   

   return (" ".join( meaningful_words))


def letter_fr(file):


    #function that takes a string
    #and returns the frequency of words



    c = Counter()
    for line in file:
        l=line.lower().strip()
        
        c += Counter( x for x in l.strip() if x.isalpha() )
        
    return c
    

def word_count(file):


    #function that takes a string 
    #and returns number of total words


   num_words=len(file.split())
##    num_words=0
##    for line in file:
##        l = line.split()
##        num_words += len(l)
        
   return num_words  
    

def unique_words(file):


    #function that takes a string
        #and returns number of unique words


    word_count = {}
    words=file.split()
    for word in words:
       count = word_count.get(word, 0)
       count += 1
       word_count[word] = count
       #collections.Counter(file.strip())
    unique = [w for w in word_count if word_count[w] == 1]   
    return len(unique) 
    
def words_follow(file,max_common,max_follow):

    #function that takes a string
    #and an integer and returns
    #5 most common words and the n words that follow them


   words=file.split()
   counter_words=Counter(words).most_common(max_common)
   common_words=[w[0] for w in counter_words]


   tar_list=list()
   for word in common_words :
      pattern=str(word)+' '+'(\w+ {1})'
      m = re.compile(pattern)
      all_words=m.findall((file))
      top_words=Counter(all_words).most_common(max_follow)
      tar_list.append(top_words)
     

   zipp=dict(zip(counter_words,tar_list))
   
   return zipp

def border_msg(msg):

    #function that takes a string
    #and draws a box outside


    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)


def write_to_file(input_file,letters_frequency,total_word_count,unique_word_count,CommonFollowing):

    print("Writing your file.....")
    
    time.sleep(2)

    with open(str(input_file), 'w+') as f:
    
        f.writelines("The frequency of letters are: ")
        f.writelines("\n")
        f.writelines('Letter : Frequency')
        f.writelines("\n")
        for key, value in sorted(letters_frequency.items(),key=lambda t: t[1],reverse=True):
            f.writelines("{0} : {1}".format(key, value))
            f.writelines("\n")
   
        f.writelines("\n") 
        f.writelines("The number of words in the file is: {0} ".format(total_word_count))
        f.writelines("\n")
        f.writelines("Number of unique words is: {0}".format(unique_word_count))
        f.writelines("\n")
        for key,value in CommonFollowing.items():
            f.writelines("\n")
            f.writelines("common word : {0} ".format(key))
            for val in value:
                f.writelines("\n")
                f.writelines("---follow word : {0}".format(val))
        



if __name__ == '__main__':
   main(sys.argv)








