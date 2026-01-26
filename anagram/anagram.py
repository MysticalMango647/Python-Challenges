'''
code an anagram where the same amount of letters are in 2 words
challegnge make the user input and do validation
'''

def check_for_anagram(word1, word2):
    word1 = list(word1.lower())
    word1.sort()
    word2 = list(word2.lower())
    word2.sort()

    print (word1)
    print (word2)
    return (word1 == word2)
#print(check_for_anagram("pyThon", "typhon"))

def check_for_anagram_2(word1, word2):
    word1 = list(word1.lower())
    word2 = list(word2.lower())
    return (sorted(word1)==sorted(word2))

#print(check_for_anagram_2('abcd','dcba'))

#Challenge create an application

user_input = input("Enter a word: ")
library = ['python', 'typhoon', 'sunny', 'windy']

def check_for_anagram_3(user_input, library):
    for word in library:
        if sorted(user_input.lower()) == sorted(word.lower()):
            print(word)

check_for_anagram_3(user_input, library)