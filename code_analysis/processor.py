__author__ = 'alexeyev'

#todo: throw away and use tree.py with main processor
#todo: remove hardcode and use rules

import tree, sys, os, re, logging

data_dir = sys.argv[1]
dest_dir = sys.argv[2]

def clean_data(data):
    data = re.sub(r"\s", "", data)
    return re.sub(r"[^\dRTPL\)\(]", "*", data)

for file in [f for f in os.listdir(data_dir) if f.endswith(".csv")]:
    print "\nProcessing " + file
    dir_name = dest_dir + "/" + file.replace(".", "-")
    try:
        os.mkdir(dir_name)
    except:
        continue
        #pass
    read_file = open(data_dir + "/" + file, "r")
    counter = 0
    for line in read_file:
        data = line.split(";")[2:]
        if data[0].startswith("blocks: new record") and data[4].strip() <> "":
            print data
            try:
                code_tree = tree.Tree(clean_data(data[4]), "*", "_").to_graphviz_format()
                code_tree.draw(dir_name + "/record-%04d.png" % counter, prog="dot")
            except Exception:
                print("Could not build tree for " + str(read_file) + " : " + str(data))
            counter += 1
