# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}

user_input = input("Enter a word: ").upper()

nato_phonetic_code = [alphabet_dict[word] for word in user_input if word in alphabet_dict]

print(nato_phonetic_code)
