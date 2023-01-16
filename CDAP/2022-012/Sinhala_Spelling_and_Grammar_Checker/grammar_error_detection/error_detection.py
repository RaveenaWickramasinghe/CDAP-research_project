import nltk
import codecs
import detect_verb as detect_verb_tense
import error_correction as suggested_verb_tense
from asyncio.windows_events import NULL

# import suggestions as verb_rules

load_grammar = nltk.data.load('file:C:/Users/49176/Desktop/CDAP/2022-012/Sinhala_Spelling_and_Grammar_Checker/grammar_error_detection/grammar.cfg')
file_input = codecs.open('C:/Users/49176/Desktop/CDAP/2022-012/Sinhala_Spelling_and_Grammar_Checker/grammar_error_detection/sentences.txt', 'r', 'utf-8-sig')
print("Grammar Error Detection for Sinhala Language")

start = 0
startJ = 0

#Function to detect the grammatical errors in a sentence
input_sentence = input("Sentence : ")
def grammar_detection(input_sentence):
        # for sent in input_sentence:
                sent_split = input_sentence.split()
                rd_parser = nltk.RecursiveDescentParser(load_grammar)
                if(list(rd_parser.parse(sent_split))==[]):
                        print("Error !!  The Sentence is Grammatically Incorrect")
                        words = nltk.word_tokenize(input_sentence)
                        first_word = input_sentence.split()[0]
                        print("Subject :",first_word)
                        last_word = words[-1]
                        print("Verb :", last_word)
                        print("Sentence", input_sentence)
                        print(words)
                        subject_tense = detect_verb_tense.identify_subject_tense(first_word)
                        correct_sentence = suggested_verb_tense.identify_suggestions(subject_tense,last_word,input_sentence)
                        return "Error !!  The Sentence is Grammatically Incorrect", correct_sentence
                else:
                        print("The Sentence is Grammatically Correct")
                        print(input_sentence)
                        print("Parse tree: ")
                        for tree_struc in rd_parser.parse(sent_split):
                                s = str(tree_struc)
                                print (s)
                        print("Corrected sentence : ", input_sentence)
                        words = nltk.word_tokenize(input_sentence)
                        first_word = input_sentence.split()[0]
                        print("Subject :",first_word)
                        last_word = words[-1]
                        print("Verb :", last_word)
                        subject_tense = detect_verb_tense.identify_subject_tense(first_word)
                        suggest_rules = suggested_verb_tense.identify_suggestions(subject_tense,last_word,input_sentence)
                        return "The Sentence is Grammatically Correct", input_sentence
               
              
   
        
# Function which returns last word
def lastWord(string):
    # taking empty string
    newstring = ""
    # calculating length of string
    length = len(string)
    # traversing from last
    for i in range(length-1, 0, -1):
        # if space is occurred then return
        if(string[i] == " "):
            # return reverse of newstring
            return newstring[::-1]
        else:
            newstring = newstring + string[i]


#Calling the grammar_detection() function
#grammar_detection()
grammar_detection(input_sentence)