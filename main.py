# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:10:57 2020

@author: siddarthaThentu
"""

import re
import numpy as np
import pandas as pd
from collections import Counter

def load_data_from_file(filename):
    #reading file contents
    with open(filename,"r") as fp:
        contents = fp.read()
    #return list of words  
    words = re.findall("\w+",contents.lower())
    return words

def get_probs(word_list):
    
    count_dict = Counter(word_list)
    total_words = sum(count_dict.values())
    prob_dict = {i:count_dict[i]/total_words for i in count_dict}
    return prob_dict

def split_word(word):
    
    split_list = [(word[:i],word[i:]) for i in range(len(word)+1)]
    return split_list

def delete_letter(word,verbose=False):
    
    split_list = split_word(word)
    delete_list = [L+R[1:] for (L,R) in split_list if R]
    if verbose:
        print("List of all possible deletions:\n")
        print(delete_list)
    return delete_list

def switch_letter(word,verbose=False):
    
    split_list = split_word(word)
    switch_list = [L+R[1]+R[0]+R[2:] for (L,R) in split_list if len(R)>=2]
    if verbose:
        print("List of all switch possibilities:\n")
        print(switch_list)
    return switch_list

def replace_letter(word,verbose=False):
    
    split_list = split_word(word)
    replace_list = []
    for (L,R) in split_list:
        if R:
            for char in alphabet:
                if char!=R[0]:
                    replace_list.append(L+char+R[1:])
    
    replace_list = sorted(list(set(replace_list))) 
    if verbose:
        print("List of all replaced words:\n")
        print(replace_list)
    
    return replace_list

def insert_letter(word,verbose=False):
    
    split_list = split_word(word)
    insert_list = [L+char+R for (L,R) in split_list for char in alphabet]
    if verbose:
        print("List of all inserted words:\n")
        print(insert_list)   
    return insert_list

def edit_one_letter(word,allow_switches=True):
    
    edit_one_set = set(delete_letter(word)+replace_letter(word)+insert_letter(word))
    if allow_switches:
        edit_one_set = edit_one_set.union(switch_letter(word))
    return edit_one_set
    
def edit_two_letter(word,allow_switches=True):
    
    edit_two_set = set()
    for eachWord in edit_one_letter(word):
        edit_two_set = edit_two_set.union(edit_one_letter(eachWord))
    return edit_two_set
                         
def get_corrections(word,prob_dict,vocab,n=2,verbose=False):
    
    all_suggestions = edit_one_letter(word) or edit_two_letter(word);
    valid_suggestions = all_suggestions.intersection(vocab)
    suggest_list = [(item,prob_dict[item]) for item in valid_suggestions]
    if verbose:
        print("Entered Word = ",word,"\nSuggestions = ",suggest_list)
    return suggest_list

alphabet = "abcdefghijklmnopqrstuvwxyz"

word_list = load_data_from_file("shakespeare.txt")
vocab = set(word_list)
print("Length of our vocabulary = ",len(vocab))

input_word = input("Please enter a word :: ")

prob_dict = get_probs(word_list)

result = get_corrections(input_word,prob_dict,vocab,n=2,verbose=True)
    
    
                
    
    


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    