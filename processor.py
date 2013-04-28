"""
Logs converter.

arg # 1 -- rules file
arg # 2 -- directory with logs
arg # 3 -- directory with converted logs

Code is designed to be descriptive.
Conversion is blocks-problem-oriented.
"""

import sys, os, datetime, automata

rules = {}
auto_rules = {}
for line in open(sys.argv[1], "r"):
    # comments
    if line.startswith("#"):
        continue
    # automata rules
    if line.startswith("$"):
        pair = line[1:].strip().split("$")
        auto_rules[pair[0]] = pair[1]
        continue
    pair = line.strip().split("$")
    rules[pair[0]] = pair[1]
print "Rules:"
print rules
print "Automata rules:"
print auto_rules

print
print "Processing logs..."

data_dir = sys.argv[2]
dest_dir = sys.argv[3]

for file in [f for f in os.listdir(data_dir) if f.endswith(".csv")]:
    print "\nProcessing " + file
    a = automata.Automata(auto_rules)
    read_file = open(data_dir + "/" + file, "r")
    dest_file = open(dest_dir + "/" + file, "w+")
    counter = 1
    for line in read_file:
        splitted_line = line.strip().split(";")
        record = [splitted_line[0], splitted_line[1], ";".join(splitted_line[2:])]
        acq_date = datetime.datetime.strptime(record[1], "%a %b %d %H:%M:%S GMT+0400 %Y")
        message = record[2]
        response = ""
        if not message in rules:
            response = a.process(message)
        else:
            response = rules[message]
        dest_file.write(str(counter) + ";" + str(acq_date) + ";" + response + "\n")
        counter += 1
    read_file.close()
    dest_file.close()
