import os
import click
from lxml import etree
import csv


path_to_encposdict = "../data/encpos.tsv"
input_path = "../data"
output_path = "./Test"
citation_bibl =  "<temp><title>Positions des thèses soutenues par les élèves de la promotion de {promotion_year} pour obtenir le diplôme d’archiviste paléographe</title>, <publisher>École des chartes</publisher>, <pubPlace>Paris</pubPlace>, <date>{promotion_year}</date>, <biblScope>p. {pagination}</biblScope>.</temp>"

def injectTEIHeader(xml):
    """

    :param xml: Tree of the xml files in input
    :return: Tree with the new TEIHeader
    """
    template = etree.parse("./templateTEIHeader.xml")
    header = xml.find("//ti:teiHeader", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
    header.getparent().remove(header)
    TEI = xml.xpath("//ti:TEI", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
    TEI[0].insert(0, template.getroot())
    return xml

def updateTeiHeader(xml, dir ,file, dict):
    """

    :param xml: Tree with the new TEI Header
    :param dir: Directory of the files
    :param file: The name of the files
    :param dict: dictionnary with the metadata
    :return: the XML with the TEIHeader with the metadata update
    """
    id = file.replace(".xml","")
    metadata = dict[id]
    
    #Delete all the attrib
    for table in xml.xpath('//ti:TEI[@*]', namespaces={"ti": 'htt://www.tei-c.org/ns/1.0'}):
        table.attrib.clear()
    TEI = xml.xpath("//ti:TEI", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
    TEI[0].attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fre"
    TEI[0].attrib["{http://www.w3.org/XML/1998/namespace}id"] = id

    if "<" in metadata["title_rich"]:
        titleetree = "<temp>"+metadata['title_rich']+"</temp>"
        titleetree = etree.fromstring(titleetree)
        lowercapitalse = titleetree.xpath("//small")
        for lo in lowercapitalse:
            lo.text = lo.text.lower()
        italics = titleetree.findall("i")
        for italic in italics:
            italic.tag = "hi"
            italic.attrib["rend"] = "i"
        sups = titleetree.findall("sup")
        for sup in sups:
            sup.tag = "hi"
            sup.attrib["rend"] = "sup"
        smalls = titleetree.findall("small")
        for small in smalls:
            small.tag = "hi"
            small.attrib["rend"] = "sc"
        title = xml.find("//titleStmt/title", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
        title.text =""
        title.insert(0, titleetree)
        etree.strip_tags(title, 'temp')

    else:
        title = xml.find("//titleStmt/title", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
        title.text = metadata["title_rich"]
    author = xml.find("//titleStmt/author", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
    if metadata["author_fullname_label"] != "":
        author.text = metadata["author_fullname_label"]
    else:
        author.getparent().remove(author)
    dateCreation = xml.find("//profileDesc/creation/date", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
    dateCreation.attrib["when"] = metadata["promotion_year"]
    if metadata["promotion_year"] == "":
        facs = xml.find("//sourceDesc", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
        facs.attrib["facs"] = "https://raw.githubusercontent.com/chartes/encpos/metadata/data/{0}/{1}.PDF".format(dir,id)
        return xml
    elif int(metadata["promotion_year"]) < 2000 :
        facs = xml.find("//sourceDesc", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
        facs.attrib["facs"] = "https://raw.githubusercontent.com/chartes/encpos/metadata/data/{0}/{1}.PDF".format(dir,id)
    if metadata["author_idref_ppn"] != "":
        author.attrib["ref"] = "https://www.idref.fr/{0}".format(metadata["author_idref_ppn"])
    SourceDesc = xml.find("//sourceDesc/bibl", namespaces={"ti": 'http://www.tei-c.org/ns/1.0'})
    if metadata["pagination"] != "" :
        pagination = etree.fromstring(citation_bibl.replace("{promotion_year}", metadata["promotion_year"]).replace("p. {pagination}", "p. {0}".format(metadata['pagination'])))
        SourceDesc.insert(0, pagination)
        etree.strip_tags(SourceDesc, 'temp')
    else:
        pagination = etree.fromstring(citation_bibl.replace("{promotion_year}", metadata["promotion_year"]).replace(", <biblScope>p. {pagination}</biblScope>", ""))
        SourceDesc.insert(0, pagination)
        etree.strip_tags(SourceDesc, 'temp')
    return xml

def write_to_file(file, dir, ouputtree):
    filepath = os.path.join(output_path, dir,file)
    if not os.path.exists(os.path.join(output_path, dir)):
        os.makedirs(os.path.join(output_path, dir))
    with open(filepath, 'w') as f:
        tree_str = etree.tostring(ouputtree, pretty_print=True, encoding="unicode")
        f.write(tree_str)

@click.command()
@click.option('--a', type=str, help='Enter the name of the only folder ')
def main(a):
    """
        Update the TEIHeader of all the XML files in the different folder of the input path
    """
    dirspos = [f for f in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, f))]
    dpos = {}
    with open(path_to_encposdict, 'r', newline='') as meta:
        reader = csv.DictReader(meta, delimiter='\t', dialect="unix")
        for line in reader:
            if a == None :
                dpos[line["id"]] = line
            elif line["promotion_year"] == a:
                dpos[line["id"]] = line
    if a == None :
        for dir in dirspos:
            files = [f for f in os.listdir(os.path.join(input_path, dir)) if "xml" in f]
            for i, file in enumerate(files):
                xml = etree.parse(os.path.join(input_path, dir,file))
                correctxml = injectTEIHeader(xml)
                correctxml = updateTeiHeader(correctxml, dir, file, dpos)
                write_to_file(file, dir, correctxml)
    else:
        files = [f for f in os.listdir(os.path.join(input_path, a)) if "xml" in f]
        for i, file in enumerate(files):
            xml = etree.parse(os.path.join(input_path, a, file))
            correctxml = injectTEIHeader(xml)
            correctxml = updateTeiHeader(correctxml, a, file, dpos)
            write_to_file(file, a, correctxml)




if __name__ == "__main__":
    main()

