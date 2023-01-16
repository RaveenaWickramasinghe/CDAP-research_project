from numpy import append
import person_number_suffix as person_number
import honorific_suffix as honorific
import gender_suffix as gender


subject_arr = ["මම", "ඔබ", "තී", "ගුරුවරිය", "ඇය"]
# subject_arr = ["කෙනෙක්", "මහල්ලා", "ගුරුවරියෝ", "මම", "මම", "යුෂ්මතා", "ඔබලා", "නුඹලා"]
start = 0
initialStartNumberPerson = 0


analyzed_subjects = {}
number_person_result = None
honorific_result = None
gender_result = None


def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    # creating a new empty list
    sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

for i in range (start, len(subject_arr)):
    analysis_features_list = []
  
    # calling the function which identify thr person and the number
    number_person_result = person_number.main_rules_number_person(subject_arr[i])
    # loop for readin the output of the function and appending to the map
    for j in range(initialStartNumberPerson, len(number_person_result)):        
        analysis_features_list.append(number_person_result[j])
    
    # calling the function which identify the honorific
    honorific_result = honorific.identify_honorific(subject_arr[i])
    analysis_features_list.append(honorific_result)

    # calling the function which identify the gender
    gender_result = gender.identify_gender(subject_arr[i])
    analysis_features_list.append(gender_result)

    analyzed_subjects = add_values_in_dict(analyzed_subjects, subject_arr[i], analysis_features_list)
    
print("Analyzed_Subjects = ", analyzed_subjects)