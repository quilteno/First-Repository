import json

name = input("Type your name")
filename = 'names.json'
with open(names.json,"w") as f:
    json.dump(name,f)
    print()