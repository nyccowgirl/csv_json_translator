"""
Write a CSV-to-JSON translator that expects a path to a CSV file as argument, 
and for each line, prints out a JSON object encapsulating that record

$ python3 file.py file.csv [-h] [-d <p | s | sc | t>]
"""

import csv, json, sys

"""NOTE: This could be done in more pythonic way without all the 'fluff' of different
functions/exception handling and main() as follows: 

    # if no headers
    reader = csv.reader(open(sys.argv[1], 'r'))

"""
# Comment out next two lines for csv with header and simple code
# reader = csv.DictReader(open(sys.argv[1], 'r', encoding = 'utf-8'))
# print(json.dumps([row for row in reader], indent = 2))


def read_file():
    """Opens the file designated by user and checks whether file name was provided."""
    # usage statement, with optional flags for header and delimiter 
    # (limited to common ones for csv)
    usage = ("usage: " + sys.argv[0] + " csvfile [-h] [-d <p | s | sc | t>)]"
            "\n\t-h: csv file contains header (default is no header)"
            "\n\t-d p | s | sc | t: delimiter as p (pipe), s (space), sc (semicolon) or t (tab)"
            "\n\t(default delimiter is comma)")

    # Checks if file is provided. If not, program is aborted.
    if len(sys.argv) < 2:
        raise(SystemExit)(f"csv file must be provided in the command line."
            f"\n{usage}")

    # Checks if file exists and is csv. If not, program is aborted.
    try:
        filename = sys.argv[1]
        if filename.endswith('.csv'):
            csv_file = open(filename, 'r', encoding = 'utf-8')

            # Process optional flags in command line for header and/or delimiter
            opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
            args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

            header = ('y' if "-h" in opts else 'n')

            try:
                # Process argument for flag -d
                if "-d" in opts:
                    if args[1] == 'p':
                        separator = '|'
                    elif args[1] == 's':
                        separator = ' '
                    elif args[1] == 'sc':
                        separator = ';'
                    elif args[1] == 't':
                        separator = '\t'
                else:
                    separator = ','
            except:
                # Program is aborted if flag -d was not followed with valid delimiter
                raise(SystemExit)(f"-d: No valid delimiter provided"
                    f"\n{usage}")
        else:
            raise(SystemExit)(f"{filename}: No csv file"
            f"\n{usage}")
    except FileNotFoundError:
        raise(SystemExit)(f"{filename}: No such file or directory"
            f"\n{usage}")
    return csv_file, separator, header

def translate_csv_json(csvf, delim, head):
    """Reads csv file and prints out each row as JSON object."""
    # Accounts for whether csv file has header row and/or modified delimiter.
    if head == 'y':
        reader = csv.DictReader(csvf, delimiter = delim)
    else:
        reader = csv.reader(csvf, delimiter = delim)

    print(json.dumps([row for row in reader], indent = 2))


if __name__ == '__main__':
    f, sep, head = read_file()
    translate_csv_json(f, sep, head)
    f.close()