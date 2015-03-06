#Insigh Data Engineering Fellows Program- Coding Challenge
#created by Wei
#! /usr/bin/env python
import string
import os
import collections
        
def clear_punctuation(s):
    '''clear punctuation within string'''
    clear_string = ""
    for symbol in s:
        if symbol not in string.punctuation:
            clear_string += symbol
    return clear_string

def count_word(wc_input):
    '''count word frequency '''
    word_frequency={}
    for line in wc_input:
        #split lines
        word_list=line.split()
        for word in word_list:
            #clear punctutaion in each word
            word=clear_punctuation(word)
            word=word.lower()
            #add word and frequecny to a dictionary
            word_frequency[word]=word_frequency.get(word, 0) + 1
    return word_frequency

def write_word_frequency():
    '''read file and write word frequency into another file'''
    # use import library to find all files
    file_list=[file for file in os.listdir("./wc_input") if file.endswith(".txt")]
    wc_input=[]
    for filename in file_list:
        #get all the files in wc_input directory
        filename=str('./wc_input/'+filename)
        f=open(filename,'r')
        #get input content from all the files
        wc_input=wc_input+f.readlines()
        f.close()
    #count word frequency for all lines
    wc_output=count_word(wc_input)
    filename='./wc_output/wc_result.txt'
    f=open(filename,'w')
    #order a dictionary 
    wc_output= collections.OrderedDict(sorted(wc_output.items()))
    print 'my_word_count result:',wc_output
    for key in wc_output.keys():
        line=key+'\t'+str(wc_output[key])+'\n'
        #write output data into a file
        f.write(line)
    f.close()


if __name__ == '__main__':

    write_word_frequency()



