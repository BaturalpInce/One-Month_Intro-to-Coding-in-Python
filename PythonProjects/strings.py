#strings = (' '), (" "), (""" """) all the same


people_quote = 'I love listening music.'
print(people_quote)

text_quote = "aaaaaaaa"
print(text_quote)

lorem_quote = """lorem ipsum"""
print(lorem_quote)


quote = 'a person said: "kid\'s computer"'
print(quote)

name = "Matt"
orphan_fee = 300
lunch_fee = 25

total = orphan_fee + lunch_fee

#print(name, "the total will be", total) 
print(f"{name} the total will be £{total}.")
print(f"{name} the total will be £{total:.3f}.")