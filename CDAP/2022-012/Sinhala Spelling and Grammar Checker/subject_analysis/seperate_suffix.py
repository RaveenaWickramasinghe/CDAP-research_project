import re

from numpy import not_equal
import rules.suffix_rules as rules

# word = input("Word : ")
word = "මම"
# print(len(word))
# print(word.endswith("ඔහු"))

start = 0
startJ = 1
result = ""

def identifyPerson_SingularPlural(key, value, person): 

    if key == "s":                       
        for k in range(len(value)):           
            if word.endswith(value[k]) == True :                
                result = "Singular"
                print(person, result )
                return result
                                      
    else :    
        for l in range(len(value)):
            if word.endswith(value[l]) == True :               
                result = "Plural"
                print(person ,result )
                return result


  
for i in range(start, rules.Rules.__len__()):
    finalresult = ""
    #  print(rules.Rules, "\n")
    for j in range(startJ , list(rules.Rules[i].items())[1].__len__()):
        # print(list(rules.Rules[i].items())[0][1])
        # print(list(rules.Rules[i].items())[1][0])   
        mapN = (list(rules.Rules[i].values())[1])[0]    
        print(mapN, "\n")       
        for key,value in mapN.items() :
            if finalresult == "":
                finalresult = identifyPerson_SingularPlural(key, value, list(rules.Rules[i].items())[1][0] )
                
            elif finalresult != "":
                break

            
        
                        

    

# print(re.findall(r'\w\W?', word))

# def split(word):
#     return [char for char in word]

# print(word)     
# print(split(word))
# word_length = 0
# for c in word: # traverse the string “educative”
#     word_length +=1 #increment the counter
# print ("Word length : " ,  word_length) # outputs the length (9) of the string “educative”

# def suffix(word_length, character_length, word ):
#     k = word_length
#     while k <= character_length:
#         pre_base_word = word [: -k]
#         suffix = word[-k:]
#         if suffix in nouns_suffixes_list:
#             return suffix
#         return pre_base_word
#         k = k - 1

