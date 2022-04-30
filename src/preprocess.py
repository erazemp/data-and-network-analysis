import ast
import csv
import glob
import json


def csv_to_json(csv_filename, json_filename, nested_col_list):
    jsonArray = []

    # read csv file
    with open(csv_filename, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # convert nested json
            for nested_col in nested_col_list:
                # check for empty string
                if row[nested_col] and row[nested_col] != "null":
                    # we use ast instead of json.loads, since some string have unescaped characters
                    row[nested_col] = ast.literal_eval(row[nested_col])

            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(json_filename, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


if __name__ == '__main__':
    for file in glob.glob("../data/events/*.csv"):
        file = file.replace(".csv", "")
        print(file)
        csv_to_json(f'{file}.csv', f'{file}.json', ["tags", "positions", "tagsList"])

    for file in glob.glob("../data/matches/*.csv"):
        file = file.replace(".csv", "")
        csv_to_json(f'{file}.csv', f'{file}.json',
                    ["teamsData", "referees", "team1.formation", "team1.formation.bench", "team1.formation.lineup", "team1.formation.substitutions",
                     "team2.formation", "team2.formation.bench", "team2.formation.lineup", "team2.formation.substitutions"])

    csv_to_json("../data/players.csv", "../data/players.json", ["passportArea", "role", "birthArea"])
    csv_to_json("../data/competitions.csv", "../data/competitions.json", ["area"])
    csv_to_json("../data/teams.csv", "../data/teams.json", ["area"])
