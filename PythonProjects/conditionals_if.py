answer = input("Do you want to hear a joke?\n")

#positive_responses = ["Yes","yes","Y","y"]
#negative_responses = ["No","no","N","n"]

positive_responses = ["yes","y"]
negative_responses = ["no","n"]

#if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
#if answer in positive_responses:
if answer.lower() in positive_responses:
	print("Joke")

#elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
#if answer in negative_responses:
if answer.lower() in negative_responses:
	print("No Joke")

else:
	print("Please type 'Yes' or 'No' next time.")