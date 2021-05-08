"""
Write a CSV-to-JSON translator that expects a path to a CSV file as argument, 
and for each line, prints out a JSON object encapsulating that record

$ python3 csv_json.py your_file.csv
"""

import csv, json, sys


def read_file():
    """Opens the file designated by user and checks whether file name was provided."""
    
    if len(sys.argv) < 2:
        raise(SystemExit)("Filename must be provided on the command line as follows:\n$ python3 this_file.py your_file.csv")

    # Checks whether file exists and is csv. If not, program is aborted.
    try:
        filename = sys.argv[1]
        if filename.endswith('.csv'):
            # Comment in/out appropriate format depending on whether file is binary or not
            # csv_file = open(filename, 'rb')
            csv_file = open(filename, 'r', encoding = 'utf-8')
        else:
            raise(SystemExit)(f"The {filename} file is not csv format. Please try another file as follows:\n$ python3 this_file.py your_file.csv")
    except FileNotFoundError:
        raise(SystemExit)(f"The {filename} file does not exist. Please try another file as follows:\n$ python3 this_file.py your_file.csv")

    return csv_file

def translate_csv_json(csvf, delim, head):
    """Reads csv file and prints out each row as JSON object."""
    # Account for whether csv file has header row. Modify delimiter or header,
    # if necessary in main().
    if head == 'n':
        reader = csv.reader(csvf, delimiter = delim)       # without header row
    else:
        reader = csv.DictReader(csvf, delimiter = delim)      # with header row
    print(json.dumps([row for row in reader], indent = 2))


if __name__ == '__main__':
    f = read_file()
    # Commented out as course policy would not allow input() function, so modify
    # delimiter and header, if necessary.
    # separater = input("Enter the delimiter: ")
    # header = input("Is there a header row (y/n)? ")
    separater = ','
    header = 'y'
    translate_csv_json(f, separater, header)
    f.close()