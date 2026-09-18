import json

#Take our routine.
#Turn it into data that JSON understands.
#Open data/routine.json.
#Write the data into it.

def save_routine(routine):
    with open('data/routine.json', 'w') as file:
        json.dump(routine.items, file, indent=4)

def load_routine():
    with open('data/routine.json', 'r') as file:
        return json.load(file)
