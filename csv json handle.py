import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # print(data)

    data = data.keys()
    data_remastered = string_concatenation_for_csv(data)
    keys = data_remastered.keys()
    print(data_remastered)
    print(keys)


    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=':')
        for key, val in data_remastered.items():
            writer.writerow((str(key), val))

    print(f"CSV file {csv_file} has been created successfully")


def string_concatenation_for_csv(data):
    huge_dict = dict()

    for key in data:
        for i in key:
            bool = True
            if not (ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z')): #or i in " -"):
                bool = False
                break
            # if i in "0123456789":
            #     bool = False
            #     break

        if type(key) == int:
            bool = False

        if bool:
            handle_dir(huge_dict, key)

    return huge_dict

def handle_dir(huge_dict, string):
    print("string is", string)
    if len(string) < 4 or len(string) > 19:
        return

    # for key in huge_dict:
    #     if key == str(len(string)):
    #         huge_dict[key].add(string)
    #         return

    if len(string) in huge_dict.keys():
        huge_dict[len(string)].add(string.lower())
    else:
        huge_dict[len(string)] = set()
        huge_dict[len(string)].add(string.lower())

    return


if __name__ == "__main__":
    json_to_csv("wordsapi_sample.json", "words.csv")