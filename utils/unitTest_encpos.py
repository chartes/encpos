import os
from lxml import etree
import csv

path_to_encposdict = "../data/encpos.tsv"
input_path = "../data"

def error_encpos(xml, file):
    schema = etree.RelaxNG(etree.parse("./Test/encpos.rng"))
    validate_schema = schema.validate(xml)
    if validate_schema is False:
        print(schema.error_log)
        return [file,validate_schema ,schema.error_log]
    else:
        return []

def writer_csv(name, listoutput):
    with open("{0}.csv".format(name), 'w') as myfile:
        wr = csv.writer(myfile)
        for line in listoutput:
            wr.writerow(line)

def main():
    """
        Update the TEIHeader of all the XML files in the different folder of the input path
    """
    dpos = {}
    dirspos = [f for f in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, f))]
    List_error_log = [["id", "ValidRNG",'NumberOfMistake']]
    with open(path_to_encposdict, 'r', newline='') as meta:
        reader = csv.DictReader(meta, delimiter='\t', dialect="unix")
        for line in reader:
            dpos[line["id"]] = line
    for dir in dirspos:
        files = [f for f in os.listdir(os.path.join(input_path, dir)) if "xml" in f]
        for i, file in enumerate(files):
            if "PREV" in file or "NEXT" in file:
                continue
            else:
                xml = etree.parse(os.path.join(input_path, dir, file))
                List_error_log.append(error_encpos(xml, file))
    writer_csv("ListErrorLog", List_error_log)

if __name__ == "__main__":
    main()
