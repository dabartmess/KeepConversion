# This is a sample Python script.
import argparse
import json
import os
import re
import sys
from pathlib import Path


def getAllFiles(path2, regex_file):
    filelist = {}
    fulldir = ""
    dir = Path(path2)
    print(dir)

    pattern = re.compile(r"takeout_(\d{8})T.*\-/d{3}$", flags=re.IGNORECASE)
    match1 = re.search(pattern, str(path2))
    print(match1)
    for item in os.listdir(path2):
        if "takeout" in item.lower():
            full_path = os.path.join(path2, item)
            if os.path.isdir(full_path):
                match = re.search(r"takeout.*", full_path, flags=re.IGNORECASE)
                print("MATCH:", Path(os.path.join(os.path.join(path2, match.group())), "Takeout/Keep"))
                fulldir = os.path.join(os.path.join(path2, match.group()), "Takeout/Keep")

    matching_files = [
        str(p) for p in Path(fulldir).glob(regex_file) if p.is_file()
    ]

    # print("FILES: ", matching_files)
    return matching_files


def parse_files(filelist):
    list_of_dicts = []
    current_dict = {}

    for file in filelist:
        with open(file, "r") as f:
            json_data = json.loads(f.read())
            # print("JSON:", json_data)

            dict1 = {"color": json_data.get("color"),
                     "title": json_data.get("title"),
                     "content": json_data.get("textContent"),
                     "datetime": json_data.get("userEditedTimestampUsec"),
                     "isPinned": json_data.get("isPinned"),
                     "isArchived": json_data.get("isArchived")}
            print(dict1)

            list_of_dicts.append(dict1)

    return list_of_dicts


if __name__ == '__main__':
    # Press the green button in the gutter to run the script.
    parser = argparse.ArgumentParser(
        description="Convert Thunderbird msgFilterRules.dat to Proton Mail Sieve"
    )
    parser.add_argument("--input", help="Input msgFilterRules.dat file")
    parser.add_argument("-o", "--output", help="Output .sieve file (default: stdout)")

    args = parser.parse_args()

    if args.input is not None and args.output is not None:
        input_path = os.fspath(Path(args.input))
        print("Input path: " + input_path)
        output_path = os.fspath(Path(args.output))
        print("Output path: " + output_path)

    filelist = getAllFiles(input_path, "*.json")
    print(filelist)

    data = parse_files(filelist)
    print(json.dumps(data, indent=2))

    if not Path(args.input).exists():
        #        print("Error: File not found: " + str(args.input), file=sys.stderr)
        print("Error: File not found: " + str(input_path), file=sys.stderr)
        sys.exit(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
