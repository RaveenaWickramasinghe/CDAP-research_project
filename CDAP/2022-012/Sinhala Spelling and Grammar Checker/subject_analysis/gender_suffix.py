from asyncio.windows_events import NULL
import rules.suffix_rules as rules

word = "පුතුව"
start = 0
startJ = 0

# gender_result = NULL
def identify_gender (word):

    gender_result = NULL   
    for i in range(start, rules.Gender.__len__()):    
        # print(rules.Gender[i])      
        if gender_result == NULL:             
            for key,value in list(rules.Gender[i].items()) :
                if gender_result == NULL:
                # print(list(rules.Gender[i].keys()))
                # print(list(rules.Gender[i].values()))
                    for k in range(len(value)):
                        # print(value[k]) 
                        if gender_result == NULL:                              
                            if word.endswith(value[k]) == True : 
                                gender_result = key
                                print(value[k])
                                # print(key)
                                break 
                        else:
                            break
                else:
                    break
        else:
            break

    if gender_result != NULL:        
        print (gender_result)
        return gender_result
    else:
        gender_result = "No"
        print(gender_result)
        return gender_result 


identify_gender(word)

