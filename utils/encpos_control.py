# coding: utf-8

import click
import grammalecte
from lxml import etree
import json
from collections import Counter
import csv
from os import listdir
from os.path import isfile, join
from os import walk
import collections
import re
from unicodedata import normalize

# Différent path pour trouver les données nécessairs à l'exécution de ces tests
path_image = "/path/to/imgdir/"
path_text = "/path/to/xmldir/"
list_apo_error = []

# Affiche la liste des positions encore non livrés par le prestataire :
def check_files_folder (name, list_file):
    '''
    :param name:
    :param list_file:
    :return: Affiche pour une année ou une décennie la liste des positions non livrées par le prestataire
    '''
    list_nfile = []
    for nfile in list_file:
        list_nfile.append(nfile.split(".")[0])
    #Vérifie si tous les fichiers xml appellent toutes les dossiers existants
    if name[-1] == "*":
        for x in range(0, 10):
            list_dir_controle = []
            for root, dirs, files in walk("{}/ENCPOS/{}".format(path_image, name[:-1]+str(x))):
                for d in dirs:
                    if d != "TIFF" and d != "PDF":
                        list_dir_controle.append(d)
            list_diff = list(set(list_dir_controle) - set(list_nfile))
            print("199{}: positions manquantes :".format(x) + str(sorted(list_diff)))

    else:
        list_dir_controle = []
        for root, dirs, files in walk("{}/ENCPOS/{}".format(path_image, list_file[0].split("_")[1])):
            for d in dirs:
                if d != "TIFF" and d != "PDF":
                    list_dir_controle.append(d)
        list_diff = (list(set(list_dir_controle) - set(list_nfile)))
        print(("{}: positions manquantes :".format(list_file[0].split("_")[1]) + str(sorted(list_diff))))


# Fonction de vérification du motif de nommage des fichiers livrés
def control_files_name(list_file):
    list_wrong_files_names = ["Nom de fichier invalide"]
    for file in list_file :
        f = file.split(".")[0]
        if not (f.split("_")[0] == "ENCPOS" and f.split("_")[1].isdigit() and len(f.split("_")[1]) == 4 and ((len(f.split("_")[2]) == 2 and f.split("_")[2].isdigit()) or f.split("_")[2] == "PREV" or f.split("_")[2] == "NEXT")):
            list_wrong_files_names.append(file)
            list_file.remove(file)
    return list_file, list_wrong_files_names


# Vérifie si les fichiers testés existe dans le fichier de recollement de la BEC
def check_files_exist(list_files, d_recollement):
    list_file_missing = ["Nom de fichier non présent dans le fichier de recollement"]
    for files in list_files:
        if files.split(".")[0] not in d_recollement:
            list_file_missing.append(files)
    return list_file_missing


#Renvoie la qualité de l'ocr du fichier xml
def ocrquality(xml_file):
    list_error_gram = []
    list_error_spell = []
    list_unknown_word = []
    list_minus_word = []
    list_error_punct = 0
    xslt = etree.parse("encpos2txt.xsl")
    transform = etree.XSLT(xslt)
    text_file = transform(xml_file)
    text_file = str(text_file)
    oGrammarChecker = grammalecte.GrammarChecker("fr")
    #renvoie le fichier json des erreurs du fichier
    result_error = oGrammarChecker.generateParagraphAsJSON(0, text_file, bEmptyIfNoErrors=True)
    data_store = json.loads(result_error)
    with open("GrammarCheck.json", "w") as  f_write:
        json.dump(data_store, f_write)
    for error in data_store.get("lGrammarErrors"):
        #Ajoute la valeur de l'erreur de grammaire dans une liste
        list_error_punct += 1
        list_error_gram.append(error.get("sType"))
    for error in data_store.get("lSpellingErrors"):
        # Ajoute la valeur de l'erreur d'orthographe'dans une liste
        list_error_spell.append(error.get("sType"))
        if not error.get("sValue")[0].isupper():
            list_minus_word.append(error.get("sValue"))
        else:
            list_unknown_word.append(error.get("sValue"))
    #transforme la liste en dictionnaire pour connaitre le nombre des différents types d'erreur
    dict_error_spell = dict(Counter(list_error_spell))
    dict_error_gram = dict(Counter(list_error_gram))
    dict_unknow_world = dict(Counter(list_unknown_word))
    dict_minus_world = dict(Counter(list_minus_word))
    del dict_minus_world["xml"]
    number_minus_world = sum(value for value in dict_minus_world.values())
    #renvoie une liste avec les différents dictionnaires sous forme de string
    return [str(dict_error_spell), str(dict_unknow_world), str(dict_minus_world), str(number_minus_world), str(dict_error_gram)]


def apostrophe_error(xml_file):
    xslt = etree.parse("encpos2txt.xsl")
    transform = etree.XSLT(xslt)
    text_file = transform(xml_file)
    text_file = str(text_file)
    list_word_text = re.split("[ \t]", text_file)
    list_word_error = []
    for word in list_word_text:
        if word is not "":
            if word[-1] == "'" or word[-1] == "’" or word[-1] == '"':
                list_word_error.append(normalize('NFKD', word))
    return list_word_error



# check si la pagination a le bon ordre et si elle correspond au fichier de recollement
def pagination (xml_file, namespaces, d_recollement, name_file):
    '''

    :param xml_file: le fichier xml complet
    :param namespaces:
    :param d_recollement:
    :param name_file: nom du fichier xml
    :return: Renvoie une liste contenant en 1 si les pages sont dans le bon ordre 2 si la première et dernière page correspond au norme
    '''
    list_return = []
    listcontrol = []
    for page in xml_file.xpath("//tei:pb/@n", namespaces=namespaces):
        listcontrol.append(int(page))
    flag = 0
    i = 1
    while i < len(listcontrol):

        if listcontrol[i] < listcontrol[i - 1]:
            flag = 1
        i += 1
    if not flag:
        list_return.append(True)
    else:
        list_return.append(False)
    dict_file = d_recollement.get(name_file.split(".")[0])
    try :
        print(dict_file.get("num:pp"))
    except:
        print(name_file.split(".")[0])
    num_pair = int(dict_file.get("benc:pp").split("-")[-1]) % 2
    print(num_pair)
        #Test première page est la même et que la dernière est la même ou que la dernière est la même +1 si elle est pair
    if dict_file.get("benc:pp").split("-")[0] != str(listcontrol[0]):
        list_return.append("premier page non ok")
    elif (num_pair == 1 and int(dict_file.get("benc:pp").split("-")[-1]) + 1 != listcontrol[-1]) or (num_pair == 0 and dict_file.get("benc:pp").split("-")[-1] != str(listcontrol[-1])):
        list_return.append("dernière page non ok")
    else :
        list_return.append("True")
    return list_return


# Test que le fichier contient plus de 2 pages
def number_page(xml_file, namespaces):
    list_control = []
    list_return = []
    for page in xml_file.xpath("//tei:pb/@n", namespaces=namespaces):
        list_control.append(int(page))
    if len(list_control) < 3:
        list_return.append("La position de thèse à moins de deux pages")
    else:
        list_return.append("La position ")
    return list_return


# Contrôle que le fichier contient plus de 3 titres d'interligne
def check_number_head(xml_file, namespaces):
    counter_control = 0
    for page in xml_file.xpath("//tei:body/tei:div/tei:head", namespaces=namespaces):
        counter_control += 1
    if counter_control < 4:
        return "False"
    else:
        return "True"

    
# Validation XML des fichiers livrés et vérification des appels au schéma et à la transformation
def structure_xml(xml_file):
    '''
    :param xml_file:
    :return:la liste contient: 1. l'appel au model, 2 le fichier est-il valide
    '''
    list_rep = []
    schema_present = str(etree.tostring(xml_file))
    #Ajouter l'appel à la transformation html
    if not '<?xml-model href="../encpos.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>' in schema_present:
        list_rep.append(False)
    else:
        list_rep.append(True)
    if not '<?xml-stylesheet type="text/xsl" href="../../../hteiml/xsl/tei2html.xsl"?>' in schema_present:
        list_rep.append(False)
    else:
        list_rep.append(True)
    schema = etree.RelaxNG(etree.parse("../encpos.rng"))
    list_rep.append(schema.validate(xml_file))
    #ajouter le nombre d'erreur de validation
    return list_rep



#Contrôle la présence d'une balise auteur et d'une balise titre et compare la balise auteur avec celle du fichier de recollement
def metadata_xml (xml_file, namespaces, d_recollement, name_file):
    '''

    :param xml_file:
    :param namespaces:
    :param d_recollement:
    :param name_file:
    :return: liste renvoie 1. nom d'auteur ok 2. nom de titre
    '''
    list_rep = []
    dict_file = d_recollement.get(name_file.split(".")[0])
    try:
        author = xml_file.find("//tei:author", namespaces=namespaces)
        list_rep.append(True)
    except:
        list_rep.append(False)
    try:
        title = xml_file.find("//tei:title", namespaces=namespaces)
        list_rep.append(True)
    except:
        list_rep.append(False)
    if author.text == "{} {}".format(dict_file.get("site:prenom"), dict_file.get("site:nom")):
        list_rep.append(True)
    else:
        list_rep.append(False)
        try:
            name_author = "{} {}".format(dict_file.get("site:prenom"), dict_file.get("site:nom")) + " - " + author.text
            list_rep.append(name_author)
        except:
            list_rep.append("")
    return list_rep


# Controle si toutes les images dans le fichier xml ont été analysées
def check_image(xml_file, namespaces, name_file):
    '''

    :param xml_file:
    :param namespaces:
    :param name_file:
    :return: Renvoie True si toutes les images envoyées ont été numérisées et oscérisées
    '''
    listcontrol = []
    for page in xml_file.xpath("//tei:pb/@facs", namespaces=namespaces):
        listcontrol.append(page.split("/")[-1])
    mypath = "{}/ENCPOS/{}/{}/TIFF/".format(path_image, name_file.split("_")[1],name_file.split(".")[0])
    list_image_brut = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if set(list_image_brut) == set(listcontrol):
        return ("Toutes les images ont été traités")
    elif list_image_brut < listcontrol:
        return ("Manque les images {} dans les images envoyées".format(str(list(set(listcontrol)-set(list_image_brut)))))
    elif list_image_brut > listcontrol:
        return ("Manque les images {} sur le fichier xml".format(str(list(set(list_image_brut)-set(listcontrol)))))


def flat_gen(x):
    def iselement(e):
        return not(isinstance(e, collections.Iterable) and not isinstance(e, str))
    for el in x:
        if iselement(el):
            yield el
        else:
            yield from flat_gen(el)


# Enchaine tous les tests sur un fichier
def test_file(name_file, d_recollement):
    # si le fichier ne peut être parsé, c'est qu'il est non conforme et donc on renvoie directement l'erreur
    try:
        tree = etree.parse("../ENCPOS_{}/{}".format(name_file.split("_")[1], name_file))
    except:
        return list([name_file, "Non-conforme"])
    namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}
    rep_apostrophe_error = apostrophe_error(tree)
    list_apo_error.append(rep_apostrophe_error)
    rep_pagination = pagination(tree, namespaces, d_recollement, name_file)
    rep_check_image = check_image(tree, namespaces, name_file)
    rep_ocr = ocrquality(tree)
    rep_structure = structure_xml(tree)
    rep_number_head = check_number_head(tree, namespaces)
    rep_metadata = metadata_xml(tree, namespaces, d_recollement, name_file)
    return list(flat_gen([name_file,"Conforme", rep_number_head, rep_pagination, rep_check_image, rep_ocr, str(rep_apostrophe_error), rep_structure, rep_metadata]))


def recup_files_xml(name_folder):
    '''
    :param name_folder:
    :return: renvoie la liste des noms des fichiers à traiter
    '''
    #récupère la liste des fichiers xml présent dans le fichier demandé
    list_name = []
    #Si un seul fichier demandé
    if ".xml" in name_folder:
        list_name.append(name_folder)
        #si on demande de traiter une décénnie
    elif name_folder[-1] == "*":
        for x in range(0, 10):
            for root, dirs, files in walk("{}/ENCPOS_{}".format(path_text, name_folder[:-1]+str(x))):
                for name in files:
                    list_name.append(name)
    #Traite une année
    else:
        for root, dirs, files in walk("{}/ENCPOS_{}".format(path_text, name_folder)):
            for name in files:
                list_name.append(name)
    return list_name


def recup_files_recollement ():
    d_recollement = {}
    with open("../data/encpos.tsv",newline='') as tsvfile:
        fichierrecollement = csv.reader(tsvfile, delimiter='\t', quotechar='|')
        flag = True
        for lignerecollement in fichierrecollement:
            tempd = {}
            if flag is True :
                listindex = lignerecollement
                flag = False
            for x in range(len(listindex)):
                try :
                    tempd[listindex[x]] = lignerecollement[x]
                except :
                   continue
            try :
                d_recollement[lignerecollement[0]] = tempd
            except:
                break
    return d_recollement


@click.command()
@click.argument('name')
def main(name):
    list_file = recup_files_xml(name)
    d_recollement = recup_files_recollement()
    #retourne si la liste des noms est dans le fichier de recollement
    list_file, wrong_files_names = control_files_name(list_file)
    if len(list_file) == 0:
        quit()
    list_files_unexist = check_files_exist(list_file, d_recollement)
    check_files_folder(name, list_file)
    list_control = []
    list_control.append(["article","Fichier XML conforme ?", "Nombre d'intertitre > 3", "Suite logique des pages", "1er - dernier page correspond avec le fichier de recollement" ,"Toutes les images envoyés numérisés", "Faute d'orthographe","Liste des fautes d'orthographe commençant par une majuscule","Faute de mots commencant avec une minuscule","Nombre de faute minuscule","Faute de typographie", "Apostrophe problème", "Schéma RNG présent","Schéma tei2html.xsl présent","Fichier valide","Auteur présent", "Titre présent", "Auteur correspond au fichier de recollement", "Auteur recollement - Auteur xml" ])
    for name_file in list_file:
        list_control.append(test_file(name_file, d_recollement))
    flat_list_apo = [item for sublist in list_apo_error for item in sublist]
    dict_error_apo = dict(Counter(flat_list_apo))
    f = open('IsakoFilesChecking_{}.csv'.format(name), 'w')
    with f:
        writer = csv.writer(f)
        for row in list_control:
            writer.writerow(row)

    f = open('Missingfiles_{}.csv'.format(name), 'w')
    with f:
        writer = csv.writer(f)
        writer.writerow(wrong_files_names)
        writer.writerow(list_files_unexist)


if __name__ == "__main__":
    main()
