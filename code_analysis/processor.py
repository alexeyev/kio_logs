__author__ = 'alexeyev'

#todo: throw away and use tree.py with main processor
#todo: remove hardcode and use rules

import tree, sys,os

data_dir = sys.argv[1]
dest_dir = sys.argv[2]

print os.listdir(data_dir)

for file in [f for f in os.listdir(data_dir) if f.endswith(".csv")]:
    print "\nProcessing " + file
    dir_name = dest_dir + "/" + file.replace(".", "-")
    try:
        os.mkdir(dir_name)
    except:
        pass
    read_file = open(data_dir + "/" + file, "r")
    counter = 0
    for line in read_file:
        data = line.split(";")[2:]
        if data[0].startswith("blocks: new record") and data[- 1].strip() <> "":
            code_tree = tree.Tree(data[-1].strip(), "*", "_").to_graphviz_format()
            code_tree.draw(dir_name + "/record-%04d.png" % counter, prog="dot")
            counter += 1
