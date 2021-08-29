cities_and_towns = {"İstanbul":"Beşiktaş","Ankara":"Çankaya"}
print(cities_and_towns)
print(cities_and_towns["İstanbul"])
print(cities_and_towns["Ankara"])

print(type(cities_and_towns))
print(type(cities_and_towns["İstanbul"]))

print(cities_and_towns.get("Eskişehir","Not Found"))
print(cities_and_towns.get("Florida","Not Found"))

print(cities_and_towns.keys())
print(cities_and_towns.values())

cities_and_towns["Bursa"] = "İnegöl"
print(cities_and_towns)


#instead of creating this list
person_data_list = ["Matt", 178, 2000]
print(person_data_list)

#we can create a more meaningful dictionary
person_data_dict1 = {"Name": "Matt", "Height": 178, "Date of Birth": 2000}
print(person_data_dict1)
print(person_data_dict1["Name"])

#combining lists and dictionaries
football_teams = {
	"Galatasaray": ["Red", "Yellow"],
	"Beşiktaş": ["Black", "White"]
}

person_data_dict2 = {"Name": "J", "Height": 167, "Date of Birth": 1995}
person_data_dict3 = {"Name": "F", "Height": 195, "Date of Birth": 1986}

people = [person_data_dict1, person_data_dict2, person_data_dict3]
print(people)
print(people[0])

for person in people:
	print(person.get("Height"))

#for person in people:
#	print(person["Height"])


