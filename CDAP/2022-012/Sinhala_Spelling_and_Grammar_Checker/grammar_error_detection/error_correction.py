from asyncio.windows_events import NULL
import nltk
import suggestions as rules
suggestion='NP_LP_SIN'
verb = "යමු"
input_sentence = "මම පාසල් යමු"
start = 0
startJ = 0
 
def identify_suggestions(suggestions, verb,input_sentence):
  for i in range(start, rules.Suggestions.__len__()):
    for k,v in list(rules.Suggestions[i].items()):
      if v == suggestions:
        print(k)
        get_suffixes(k,verb,input_sentence)


def get_suffixes(rule,verb,input_sentence):
  words = list(verb)
  suffix_1 = words[-2] 
  suffix_2 = words[-1]  
  extracted_suffix = suffix_1+suffix_2
  arr = []
  suffixList =[]
  for i in range(start, rules.Suffixes.__len__()):
    for k,v in list(rules.Suffixes[i].items()):
      if v == rule:
        print(k)
        suffixList.append(k)
              
  for suffix in suffixList:
    arr.append(verb.replace(extracted_suffix, suffix))
  
  print(arr)
  words = nltk.word_tokenize(input_sentence)
  first_word = input_sentence.split()[0]
  print("Subject :",first_word)
  last_word = words[-1]
  print("Verb :", last_word)
  print(words)  
  #for loop to read the suffix list array
  for i in range (start, len(arr)):
    words[-1] = arr[i]
    print(words)
    print(" ".join(words))
    #return(" ".join(words))
        
        

#calling the method 
#identify_suggestions(suggestion,verb,input_sentence)

