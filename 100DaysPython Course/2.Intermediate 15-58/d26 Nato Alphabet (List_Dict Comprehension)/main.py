import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_dict = pandas.read_csv(
    "d26 Nato Alphabet (List_Dict Comprehension)\\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_dict.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Word: ").upper()
list_word = list(word)
result = [phonetic_dict[letter] for letter in word]
print(result)
