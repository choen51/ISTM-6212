#!/usr/bin/env python

"""
Problem 3, Part B
A filter that checks word(s) against 10 stop words and remove the word(s) if they are found to be stop words.
"""

import fileinput

stop_words = ["and","the","across","after","afterwards","again","against","all","almost","alone"]

def process(list1,line2):
    """
    The function accepts 2 input variables: The first is the list of 10 stop words defined above.  
    The second is the text line to be stripped of the stop words.
    """
    
    match_flag = False    
    for item in list1:
        if item in line2:
            match_flag = True
    
    if match_flag == False:
        print(line2)
            
            
for line in fileinput.input():
    process(stop_words,line)



    

