#Insigh Data Engineering Fellows Program- Coding Challenge
#created by Wei
#! /usr/bin/env python
import os
import copy

def caculate_median(lst):
    '''get the median from a list of number'''
    lst.sort()
    if len(lst)==0:
        #for file content is empty
        return 0
    if len(lst)%2==0:
        #for list's length is even
        median=(lst[len(lst)/2-1]+lst[len(lst)/2])/2.0
    else:
        #for list's length is odd
        median= lst[len(lst)/2]
    return median
     
def count_word_line(lst):
    ''''count word per line return a list object'''
    word_in_line=[]
    for line in lst:
        #skip if there is an empty line
        if not line=='\n':
            word_list=line.split()
            word_in_line.append(len(word_list))
    return word_in_line
        
    
def get_median():
    wc_output=[]
    wc_input=[]
    file_list=[file for file in os.listdir("./wc_input") if file.endswith(".txt")]

    for filename in file_list:
        #get all the files in wc_input directory
        filename=str('./wc_input/'+filename)
        f=open(filename,'r')
        #combine file content to one string list
        wc_input=wc_input+f.readlines()
        f.close()
    #caculate number of words in every line
    words_num_list= count_word_line(wc_input)

    stop=1
    while not stop==len(words_num_list):
        stop+=1
        #simulate adding line for getting median
        wc_output.append(caculate_median(words_num_list[:stop]))
    #write results
    filename='./wc_output/med_result.txt'
    f=open(filename,'w')
    for median in wc_output:
        median_out=str(median)+'\n'
        f.writelines(median_out)
    f.close()
    return wc_output

if __name__ == '__main__':

    print'my_running_median result:',get_median()


