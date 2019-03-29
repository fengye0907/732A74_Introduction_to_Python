#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import io
import re
import string
from nltk.corpus import stopwords
from collections import Counter



#main function that is been called at the end
def main(argv):
    
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
   letters_fr=letter_fr(CleanString)

   print("The frequency of letters are: ")
   print('Letter : Frequency')
   for key, value in sorted(letters_fr.items(), key=lambda t: t[1], reverse=True):
       print("{0} : {1}".format(key, value))
   
   print("\n")   
   print("The number of words in the file is : ",word_count(CleanString))
   print("\n")
   print("Number of unique words is: ",unique_words(CleanString))
   print("\n")
   words_follow(CleanString, 3)



#function that takes a string
#and turns to lowercase,remove punctuation,
#stop words and returns clean string
def clean_file(data):  
    
   stops = set(stopwords.words("english"))
   text=data.lower()                                                  # change all words in lower letters
   text=text.replace("“"," ")                                      # remove special signs
   text=text.replace("’"," ") 
   text=re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,*]", "", text)
   text_no_punctuation=(re.sub('[%s]' % string.punctuation,'',text))     # remove s
   text_words=re.sub(r'[0-9]+', '', text_no_punctuation)
   #pattern = re.compile(r'\b(' + r'|'.join(StopWords) + r')\b\s*')
   #meaningfull_words = pattern.sub('', text_words)
   text_list=text_words.split()
   meaningful_words = [w for w in text_list if not w in stops]
   
   return (" ".join( meaningful_words))



#function that takes a string
#and returns the frequency of words
def letter_fr(data):
    c = Counter()
    for line in data:
        l=line.lower().strip()
        c += Counter( x for x in l.strip() if x.isalpha() )
        
    return c


#function that takes a string 
#and returns number of total words
def word_count(data):
    num_words=len(data.split())
    return num_words  

    
#function that takes a string and 
#returns number of unique words
def unique_words(data):    
    word_count = {}
    words=data.split()
    for word in words:
       count = word_count.get(word, 0)
       count += 1
       word_count[word] = count
    unique = [w for w in word_count if word_count[w] == 1]   
    return len(unique) 
    
    
    
#function that takes a string
#and an integer and returns
#5 most common words and 
#the n (default=3) words that follow them
def words_follow(data, n):
   words=data.split()
   counter_words=Counter(words).most_common(5)
   common_words=[w[0] for w in counter_words]

   tar_list=list()
   for word in common_words :
      pattern=str(word)+' '+'(\w+ {1})'
      m = re.compile(pattern)
      all_words=m.findall((data))
      top_words=Counter(all_words).most_common(n)
      tar_list.append(top_words)
        
   zipp=dict(zip(counter_words,tar_list))

   for key,value in zipp.items():
      print("\n")
      print ("common word : {0} ".format(key))
      for val in value:
         print ("---follow word : {0}".format(val))



#function that takes a string
#and draws a box outside
def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)



if __name__ == '__main__':  
   main(sys.argv)

"""
We rewrite all the words in lower letters, and remove all the special signs. 
We also consider e.g. "Gutenberg's" as "Gutenberg" "s", and remove "s" later
 in our code.

The most frequent data structures we use are list and dictionaries, becuase
they are easy to modify and provided by our function, such as Counter().

"""






