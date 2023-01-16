import rules.suffix_rules as rules

# word = "පියාණෝ"
start = 0


def identify_honorific (word):
    honorific_result = ""
    for i in range(start, rules.Honorific.__len__()):    
        if word.endswith(rules.Honorific[i]) == True :         
            honorific_result = "Yes"
            break         
    
    if honorific_result != "":
        # print (honorific_result)
        return honorific_result
    else:
        honorific_result = "No"
        # print(honorific_result)
        return honorific_result
