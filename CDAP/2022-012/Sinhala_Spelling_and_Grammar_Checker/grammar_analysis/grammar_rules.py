# Numbers
    # s - singular
    # p - Plural

#person
    # 1st person - ප්‍රථම
    # 2nd person - මධ්‍යම
    # 3rd person - උත්තම
  
def grammar_rule_1(subject ):
  # Grammar rule 1
  if subject == 'ඒක' | subject == 's':
    verb = 'ඒක'
    print("If subject is Singular: ",subject)
    print("Then Verb is singular: ",verb)
  
  # Grammar rule 2
  elif subject == 'බහු' | subject == 'p':
    verb = 'බහු'
    print("Subject is Plural: ",subject)
    print("Then Verb is Plural : ",verb)

def grammar_rule_2(subject):
  # Grammar rule 3
  if subject == 'උත්තම පුරුෂ' | subject == '3rd person':
    verb = 'උත්තම පුරුෂ'
    print("If Subject is in 3rd person : ",subject)
    print("Then the Verb is in 3rd Person : ",verb)
  
  # Grammar rule 4 
  elif subject == 'මධ්‍යම පුරුෂ' | subject == '2nd person':
    verb = 'මධ්‍යම පුරුෂ'
    print("If Subject is in 2nd person : ",subject)
    print("Then the Verb is in 2nd Person : ",verb)
  
  # Grammar rule 5
  elif subject == 'ප්‍රථම පුරුෂ' | subject == '1st person':
    verb = 'ප්‍රථම පුරුෂ'
    print("If Subject is in 1st person : ",subject)
    print("Then the Verb is in 1st Person : ",verb)
      
def grammar_rule_3(subject,suffix):
  # Grammar rule 6
  if subject == 'අප්‍රාණවාචි' | subject == 'නපුංසක' | subject == 'අචේතනවාචී': 
    if subject == 'ඒක' | subject == 'බහු':
      verb = 'ඒක | Singular'
      print("Subject : ",subject)
      print("Verb must be kept singular : ",verb)
    
    # Grammar rule 7
    elif suffix == 'ඔ' | suffix == 'හු':
      verb = 'බහු | Plural'
      print("Subject : ",subject)
      print("Verb must be kept Plural : ",verb)
  
def grammar_rule_4(subject):
  # Grammar rule 8
  if subject == 'පෙළ' | subject == 'රළ' | subject == 'මුළු' | subject == 'දෙන' | subject == 'රංචුව' | subject == 'පිරිස' | subject == 'කාණ්ඩය' |  subject == 'නඩය' |  subject == 'ගුල' | subject=='හමුදාව' | subject=='පන්තිය' :   
    if subject == 'ඒක' | subject == 'බහු':
      verb = 'ඒක | Singular'
      print("Subject : ",subject)
      print("Verb must be kept Singular : ",verb)
  
    # Grammar rule 9
    elif subject == 'සචේතන' | subject == 'ප්‍රාණවාචි':
      verb = 'බහු | Plural'
      print("Subject : ",subject)
      print("Verb must be kept Plural : ",verb) 
      
def grammar_rule_5(subject):
    # Grammar rules 10
  if subject == 'වහන්සේ':
    verb = 'සේක'
    print("Subject : ",subject)
    print("Verb becomes සේක : ",verb) 
    
  else:
    verb = 'බහු | Plural'
    print("Subject : ",subject)
    print("Verb must be kept Plural : ",verb) 
    
def grammar_rule_6(suffix, subject):
    # Grammar rule 11
  if suffix == 'දෑ':
    verb = 'දෑය'
    print("Subject : ",subject)
    print("Verb : ",verb) 
    
  else:
    verb = 'බහු | Plural'
    print("Subject : ",subject)
    print("Verb must be kept Plural : ",verb) 
      
def grammar_rule_7(subject, suffix):
  # Grammar rule 12
  if suffix == 'පා':
    verb = 'බහු | Plural'
    print("Subject : ",subject)
    print("Verb must be kept Plural : ",verb)     
    
def grammar_rule_8(suffix, subject):
  # Grammar rule 13
  if suffix == 'ඩි' | suffix == 'ණ්ඩි':
    verb = 'බහු | Plural'
    print("Subject : ",subject)
    print("Verb must be kept Plural : ",verb) 
  
def grammar_rule_9(suffix, subject):
  # Grammar rule 14
  if suffix == 'ආණ' | suffix == 'අණු' | suffix == 'අණි':
    verb = 'බහු | Plural'
    print("Subject : ",subject)
    print("Verb must be kept Plural : ",verb) 

def grammar_rule_10(suffix, subject):
  # Grammar rule 15
  if suffix == 'අයෙක්' | suffix == 'කෙනෙක්' | suffix == 'ඇතැමෙක්' | suffix == 'කවුරු' | suffix == 'කවරහු' | suffix == 'කිසිවෙක්' | suffix == 'ඇතැම්හු':
    verb = 'බහු | Plural'
    print("Subject : ",subject)
    print("Verb must be kept Plural : ",verb) 
  
  # Grammar rule 16
  else:
    verb = 'ඒක | Singular'
    print("Subject : ",subject)
    print("Verb must be kept Singular : ",verb)
  
def grammar_rule_11(subject, sentence_tense):
  # Grammar rule 17
  if subject == 'ඒක' | subject == 's' & subject == 'ස්ත්‍රී':
    if sentence_tense == 'අතීත':
      verb = 'බහු | Plural'
      print("Subject : ",subject)
      print("Verb must be kept Plural : ",verb) 
  
  
  # Grammar rule 18
  # Grammar rule 19
  # Grammar rule 20
  # Grammar rule 21
  # Grammar rule 22
  # Grammar rule 23
  # Grammar rule 24
  # Grammar rule 25
  
  
  
  
    
    
  
    
  
    
  
    
    
    
  
  