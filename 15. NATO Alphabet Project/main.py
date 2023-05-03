import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict()) 
#El resultado de esto es tener un diccionario para "letter" y otro para "code".

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)
# Aca como resultado tengo el match entre letter y code. 

word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

