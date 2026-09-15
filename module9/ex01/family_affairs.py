#!/usr/bin/env python3

class Person:
	def find_the_redheads_class(dict_data):
		arr = []
		filtered_iterator = filter(lambda item: item[1] == "red", dict_data.items())
		return list((dict(filtered_iterator)).keys())

find_the_redheads = Person.find_the_redheads_class

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))
