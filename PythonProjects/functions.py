def greet(name):
	return f"Hey {name}!"

name = input("What is your name?\n")
print(greet(name))

def age_in_dog_years(age):
	return age * 7

age = int(input("How old are you?\n"))
print(f"Your age in dog years is {age_in_dog_years(age)}.")

def concatenate(word_one, word_two):
	return word_one+word_two

word_one = input("Type me the first word to concatenate.\n")
word_two = input("Type me the second word to concatenate.\n")

print(concatenate(word_one, word_two))

#can override functions like this for one time
print(concatenate(word_two = word_one, word_one = word_two))

print(concatenate(word_one, word_two))

sentence = input("What is the sentence that you want to uppercase and reverse?\n")

def uppercase_and_reverse_string(sentence):
	uppercase_sentence = sentence.upper()
	return uppercase_sentence[::-1]

print(uppercase_and_reverse_string(sentence))