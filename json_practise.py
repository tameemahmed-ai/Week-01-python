import json

# 1. CREATE
person = {
    "name": "Tameem",
    "age": 32,
    "address": {
        "city": "Gaithersburg",
        "state": "Maryland"
    },
    "hobbies": ["boxing", "coding", "travel"]
}

# 2. SAVE
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)
print("Saved to person.json!")

# 3. LOAD
with open("person.json", "r") as file:
    data = json.load(file)
print("Loaded from person.json!")

# 4. ACCESS NESTED
print(f"Name: {data['name']}")
print(f"City: {data['address']['city']}")
print(f"First hobby: {data['hobbies'][0]}")
