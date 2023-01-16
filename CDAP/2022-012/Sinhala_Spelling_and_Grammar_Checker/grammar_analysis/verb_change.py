import re
from numpy import not_equal
import verb_subject as rules
# import subject_analysis.seperate_suffix as suffix_rules
# Splitting the words in the sentence

start = 0
startJ = 1
result = ""

#def identifyTense(key, value, tense): 


def change_verb():
  input_sentence = input("Sentence : ")
  words = input_sentence.split()
  numberOfWords = len(words)
  print ("The number of words in Sentence : " +  str(numberOfWords))
  print("Words: ", words)
  length = len(words)
  verb = words[-1]
  print("ක්‍රියා පදය : ", verb)

  tense = input("Tense of Verb / Sentence : ")
  print("Tense : ", tense)
  
  
change_verb()