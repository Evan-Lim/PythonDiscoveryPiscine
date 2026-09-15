#!/usr/bin/env python3

class FamousWomen:
	def famous_births_class(dict_data):
		val = [v for v in dict_data.values() if isinstance(v, dict)]
		sorted_val = sorted(val, key=lambda item: item["date_of_birth"])
		for i in sorted_val:
			print(f"{i['name']} is a great scientist born in {i['date_of_birth']}.")

famous_births = FamousWomen.famous_births_class

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
