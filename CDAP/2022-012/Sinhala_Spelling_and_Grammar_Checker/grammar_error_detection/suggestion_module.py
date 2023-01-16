from asyncio.windows_events import NULL
import suggestions as rules
# verb="මට"
start = 0
startJ = 0


def verb_suffix(verb):

    word = NULL   
    for i in range(start, rules.Rules.__len__()):    
      for key,value in list(rules.Rules[i].items()) :
        if word == NULL:
          for k in range(len(value)):
            if word == NULL: 
              if value[k] == verb : 
                word = key
                print(value[k])
                        # print(key)
                break 
              else:
                break
            else:
              break
          else:
            break

    if word != NULL:        
        print (word)
        return word
    else:
        word = "No"
        print(word)
        return word 

# identify_subject_tense(verb)