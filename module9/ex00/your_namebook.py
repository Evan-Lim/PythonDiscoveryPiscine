#!/usr/bin/env python3

class Person:
	def array_of_names_class(dict_persons):
		arr = []
		for key, value in dict_persons.items():
			arr.append(key.capitalize() + " " + value.capitalize())
		return arr

array_of_names = Person.array_of_names_class

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))
