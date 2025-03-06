d = {} # empty dict
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
print(eng_to_spa["three"])
eng_to_spa["pineapple"] = "pina" # you can add to the dict
print(eng_to_spa["pineapple"])
eng_to_spa.update({"yes": "si", "no": "no", "i": "yo", "am": "soy",
                   "cuban": "cubano"})
print(eng_to_spa)
print(f"i know {len(eng_to_spa)} spanish words")
sentence = "i am cuban"
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word]+" "
print(f"{sentence} translates to: {translation}")
print(list(eng_to_spa.values()))
print(list(eng_to_spa.keys()))
x = eng_to_spa.pop("pineapple")
print(x)
print(eng_to_spa)

if "car" in eng_to_spa:
    print(eng_to_spa["car"])
else:
    print("i dont know this word")

print(eng_to_spa.get("car", "sorry dont know"))
eng_to_spa.setdefault("one", "sorry dont know")
eng_to_spa.setdefault("monkey", "sorry dont know")
print(eng_to_spa)