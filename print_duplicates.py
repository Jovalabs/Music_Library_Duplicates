import csv
import re
import os


IN_FILE = 'part2.csv'

CLEAN_FILE = 'part2_clean.csv'


all_source_files = set()


duplicates = set()


with open(IN_FILE, 'r') as in_f, open(CLEAN_FILE, 'w') as out_f:
    contents = in_f.read()
    clean_contents = contents.replace('\0', '')
    out_f.write(clean_contents)

with open(CLEAN_FILE, 'r') as handle:
    reader = csv.DictReader(handle, quotechar='"')
    for row in reader:
        source_file = row['SourceFile']
        all_source_files.add(source_file)


# Check for duplicates:

for source_file in all_source_files:
    (path, extension) = os.path.splitext(source_file)

    if re.match('.* \d+$', path):
        potential_match = path.rsplit(' ', 1)[0] + extension

        if potential_match in all_source_files:
            duplicates.add(source_file)


for duplicate in sorted(duplicates):
    print duplicate
