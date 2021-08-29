digits_list = [0,1,2,3,4,5,6,7,8,9]
company_list = ["Google", "Tesla", "Microsoft"]
random_list = [1, "Google", ["Google", 1, "Microsoft"], 2, 3, 96/3]

for number in digits_list:
	print("This is count", number)

for company in company_list:
	print("This is company", company)

for i in random_list:
	print("This is", i)

print(digits_list)

company_list.append("Amazon")
print(company_list)

random_list.remove(2)
print(random_list)

#squaring the digits_list with for loop
for number in digits_list:
	print(number,"squared is", number*number)

#same thing with different method
#for number in list(range(0,10)):
	#print(number,"squared is", number ** 2)


#cubing the digits_list with for loop
for number in digits_list:
	print(number,"cubed is", number ** 3)

#creating the digits_list clone with less expressions
digits_list_clone = list(range(0,10))
print(digits_list_clone)

first_digit = digits_list[0]
print(first_digit)

second_company = company_list[1]
print(second_company)

third_random = random_list[2]
print(third_random)

last_random = random_list[-1]
print(last_random)

second_last_random = random_list[-2]
print(second_last_random)
#random_list[-3]=> 3rd last random and goes like that

#this line prints the amount of items inside list
print(len(digits_list))
print(len(company_list))
print(len(random_list))

#this line print the type which is "list"
print(type(digits_list))
print(type(company_list))
print(type(random_list))


