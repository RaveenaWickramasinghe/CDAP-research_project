from asyncio.windows_events import NULL
import re

from numpy import not_equal
import rules.suffix_rules as rules

# word = "වැවිලිකරුවන්"

start = 0
startJ = 1
result = ""

# funtion to identify the number and peson
def identifyPerson_SingularPlural(word, key, value, person, patternNumber):
     
    if patternNumber == 'Pattern-O1' or patternNumber == 'Pattern-O2':
        if key == "s":                       
            for k in range(len(value)):           
                if word == value[k] :                
                    result = key            
                    return [person,result]
                                      
        elif key == "p" :    
            for l in range(len(value)):
                if word == value[l] :               
                    result = key
                    return [person,result]
    elif patternNumber == 'Pattern-O3':
        if key == "s":                       
            for k in range(len(value)):           
                if word.endswith(value[k]) == True :                
                    result = key             
                    return [person, result]
                                        
        elif key == "p" :    
            for l in range(len(value)):
                if word.endswith(value[l]) == True :               
                    result = key
                    return [person, result]

def main_rules_number_person(word):
    finalresult = None 
    for i in range(start, rules.Rules.__len__()):

        for j in range(startJ , list(rules.Rules[i].items())[1].__len__()):
        
            # Map of singular plural suffixes with key value pairs
            mapN = (list(rules.Rules[i].values())[1])[0]    
            
            # for loop for iterating the items of the mapN which contains two keys singular plural
            for key,value in mapN.items() :         
            
                if finalresult == None :
                    # map of pattern values.. eg: 'Pattern-01'
                    mapPattern = list(rules.Rules[i].items())[0][1]
                    # map of persons  
                    mapPerson = list(rules.Rules[i].items())[1][0]  

                    # Method calling and passing the specific key, values, 
                    finalresult = identifyPerson_SingularPlural(word, key, value, mapPerson, mapPattern)               
                    
                elif finalresult != None:                                     
                    break     
   
    return finalresult
   
                

    

