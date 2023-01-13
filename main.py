import gzip
import shutil
import os
import subprocess


def extract(filename):
    with gzip.open("pubmed/" + filename + ".pubmed2", 'rb') as f_in:
        with open("xml/" + filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def extract2(path, index):
    with gzip.open(path, 'rb') as f_in:
        with open("xml/pubmed" + str(index) + ".xml", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def unify(index):
    directory = r'C:\Users\marce\PycharmProjects\pubmed\texts\pubmed' + str(index)

    union = open("unions/union" + str(index) + ".txt", "w", encoding="utf-8")

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.txt'):
            with open(f, "r", encoding="utf-8") as file:
                lines = file.readlines()
                union.writelines(lines)
            os.remove(f)

    union.close()


def reduce():
    directory = r'C:\Users\marce\PycharmProjects\pubmed\unions'

    union = open("pubmed1-100" + ".txt", "w", encoding="utf-8")

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.txt'):
            with open(f, "r", encoding="utf-8") as file:
                lines = file.readlines()
                union.writelines(lines)
            os.remove(f)

    union.close()


# pubmed_dir = r'C:\Users\marce\PycharmProjects\pubmed\pubmed2'
# xml_dir = r'C:\Users\marce\PycharmProjects\pubmed\xml\pubmed'
# i = 15
# for pubmed in os.listdir(pubmed_dir):
#     print(i)
#     pub = os.path.join(pubmed_dir, pubmed)
#     extract2(pub, i)
#
#     subprocess.run(["python", "extractTIABs.py", "xml/pubmed" + str(i) + ".xml" ], shell=True)
#     unify(i)
#     os.remove(xml_dir + str(i) + ".xml")
#     i = i + 1

#reduce()
