__author__ = 'alexeyev'

"""
    Logs preprocessor eliminating whitespaces in blocks-programs-code.
    Necessary to run before starting tree-printing processor.
"""

import os

data_dir = "../data"
result_dir = "../preprocessed_data"

for file in [f for f in os.listdir(data_dir) if f.endswith(".csv")]:
    print "\nPreprocessing " + file
    read_file = open(data_dir + "/" + file, "r")
    write_file = open(result_dir + "/" + file, "w+")
    counter = 0
    gcounter = 0
    for line in read_file:
        data = line.strip().split(";")
        if len(data) < 3:
            if counter > 0:
                write_file.write(line.strip().replace(" ", "").replace("\r", "").replace("\\", "*"))
        else:
            write_file.write(("\n" if counter <> 0 else "") + line.strip().replace("\r", "").replace("\\", ""))
            gcounter += 1
        counter += 1
    print counter, gcounter
    write_file.close()
    read_file.close()