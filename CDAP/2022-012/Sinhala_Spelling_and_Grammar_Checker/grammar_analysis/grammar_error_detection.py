from asyncio.windows_events import NULL
import re

import subject_tense as rules

start = 0
startJ = 0

def get_lists():
    # Read the list of Subject List coming from Subject Analysis
    for i in range(start, rules.Subject_List.__len__()):    
        print(rules.Subject_List[i])
        
        for key,value in list(rules.Subject_List[i].items()) :
            print(list(rules.Subject_List[i].keys()))
            print(list(rules.Subject_List[i].values()))

            for k in range(len(value)):
                subjects = print(value[k]) 

    # Read the Tense List from the POS Taggig output
    for i in range(start, rules.Tense_list.__len__()):    
        print(rules.Tense_list[i])
        
        for key,value in list(rules.Tense_list[i].items()) :
            print(list(rules.Tense_list[i].keys()))
            print(list(rules.Tense_list[i].values()))

            for k in range(len(value)):
                tenses = print(value[k])
 
    # if subjects == tenses:
    #     print("Grammatically correct.")
    #     print("The tense of the verb matches with its subject.")
    # else:
    #     print("Grammatically Incorrect!!")
        

get_lists()

def check_grammar_errors():
    #return the subject list and tense list
    get_lists()
    
    

    
