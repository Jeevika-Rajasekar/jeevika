# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consontants(paragraph):
    number_of_vowels= 0
    number_of_consonants = 0 
    for i in paragraph:
        if i.isalpha() == True:
            if i == "a" or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                number_of_vowels +=1
            else:
                number_of_consonants += 1
    return(number_of_vowels, number_of_consonants)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    list_of_sentences= paragraph.replace('!','.').replace('?','.').split(". ") #replaces other punctuation marks with periods, so the paragraph can be split into sentences based on the periods. 
    number_of_sentences = 0
    total_consonants = 0
    total_vowels = 0
    for sentence in list_of_sentences: 
        counting_vowels_and_consontants(sentence) #finds number of vowels and consonants in each sentence
        number_of_sentences += 1 #finds number of sentences in total
        result =[counting_vowels_and_consontants(sentence)]

        for (vowels, consonants) in result: #this for loop finds the total number of vowels and consonants in the entire paragraph
            total_vowels += vowels
            total_consonants += consonants
        
        average_vowels = total_vowels/number_of_sentences
        average_consonants = total_consonants/number_of_sentences


    return(number_of_sentences, average_vowels, average_consonants)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 

paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(f"The average vowels per sentence of the paragraph is {average_vowels_and_consonants(paragraph)[1]}")
print(f"The average consonants per sentence of the paragraph is {average_vowels_and_consonants(paragraph)[2]}")