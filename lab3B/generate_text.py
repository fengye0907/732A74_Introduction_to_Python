from text_stats import clean_file
import sys
import os
import io
import re
import random
from collections import Counter


#main function that is been called at the end
def main(argv):
    
    # the path of txt file
   filepath =str(argv[1])

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   user_word=str(argv[2]).lower()
   max_words=int(argv[3]) 

  
   with io.open(filepath,encoding="utf-8") as f :
       data = f.read() 

   CleanString=clean_file(data)
   
   #print(successors(CleanString,user_word))
   print(generator(CleanString,user_word,max_words))
     


def generator(data,given_word,max_words):
    cur_word=given_word
    msg=str()
    s=successors(data,given_word)
    #print(s)   # neighbors with their probabilitier
    counter=0
    while(s[0] and counter<=max_words):
        cur_word = random.choices(population=s[0],weights=s[1],k=1)
        
        #print(cur_word)
        indx=s[0].index(cur_word[0])
        #print(indx)
        msg = msg + " " + cur_word[0]
        s[0].pop(indx)            # replace = True
        s[1].pop(indx)
        counter+=1
    return(msg)    
        

def successors(data,word):
    f=data.split()
    index = [i for i,v in enumerate(f) if v == word]
    neighbors=[f[x+1] for x in index]
    #unique_neighbors=list(set(neighbors))	
    count_neighbors=Counter(neighbors)
    val_counts=list(count_neighbors.values())
    val_counts=[x/sum(count_neighbors.values()) for x in val_counts]
    key_counts=[x for x in count_neighbors.keys()]

    return([key_counts,val_counts])

    

if __name__=="__main__":
    main(sys.argv)
