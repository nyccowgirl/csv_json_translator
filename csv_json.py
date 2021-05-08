"""
Write a CSV-to-JSON translator that expects a path to a CSV file as argument, 
and for each line, prints out a JSON object encapsulating that record
"""

import csv, json, sys


def read_file():
    """Opens the file designated by user and checks whether file name was provided."""
    
    if len(sys.argv) < 2:
        raise(SystemExit)("Filename must be provided on the command line.")

    # Checks whether file exists and is csv. If not, program is aborted.
    try:
        filename = sys.argv[1]
        if filename.endswith('.csv'):
            # Comment in/out appropriate format depending on whether file is binary or not
            # csv_file = open(filename, 'rb')
            csv_file = open(filename, 'r', encoding = 'utf-8')
        else:
            raise(SystemExit)(f"The {filename} file is not csv format. Please try another file.")
    except FileNotFoundError:
        raise(SystemExit)(f"The {filename} file does not exist. Please try another file.")

    return csv_file

def translate_csv_json(csvf, delim):
    """Reads csv file and prints out each row as JSON object."""
    # Comment in/out depending on whether csv file has header row. Modify delimiter,
    # if necessary in main().
    # reader = csv.reader(csvf, delimiter = delim)       # without header row
    reader = csv.DictReader(csvf, delimiter = delim)       # with header row
    print(json.dumps([row for row in reader], indent = 2))


if __name__ == '__main__':
    f = read_file()
    # Commented out as course policy would not allow input() function, so modify
    # delimiter if necessary.
    # separater = input("Enter the delimiter: ")
    separater = ','
    translate_csv_json(f, separater)
    f.close()