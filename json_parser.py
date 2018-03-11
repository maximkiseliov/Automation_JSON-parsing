import json

file = open("files/json_file.json", "r")
string = file.read()
celtics = json.loads(string)

for i in celtics:
    print("Player id:", i,
          "\nFirstname:", celtics[i]['firstname'],
          "\nLastname:", celtics[i]['lastname'],
          "\nJersey #:", celtics[i]['jersey'],
          "\nSalary $:", celtics[i]['salary'],
          "\nNumber of Trophies:", celtics[i]['trophies'],
          "\n")
