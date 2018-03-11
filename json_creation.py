import json

celtics = {}

celtics[1] = {
    'firstname': 'Rajon',
    'lastname': 'Rondo',
    'jersey': '9',
    'salary': 2100000,
    'trophies': None
    }

celtics[2] = {
    'firstname': 'Kevin',
    'lastname': 'Garnett',
    'jersey': '21',
    'salary': 5000000,
    'trophies': 1
    }

celtics[3] = {
    'firstname': 'Paul',
    'lastname': 'Pierce',
    'jersey': '34',
    'salary': 3400000,
    'trophies': 1
    }

file = open("files/json_file.json", "w")
json.dump(celtics, file)
file.close()
