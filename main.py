import gzip
import shutil
import os
import subprocess


def extract(filename):
    with gzip.open("gz/" + filename + ".gz", 'rb') as f_in:
        with open("xml/" + filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


#extract("pubmed23n0001.xml")
#subprocess.run(["python", "extractTIABs.py", "xml/pubmed23n0001.xml"], shell=True)

directory = r'C:\Users\marce\PycharmProjects\pubmed\texts'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.txt'):
        print(f)

