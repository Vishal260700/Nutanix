from multiprocessing import Pool
import os
import sys
filedic=[]
important=[]
keep_phrases = sys.argv[1]
keep_phrases = keep_phrases.split(";")
def logger(infile) :
    with open(infile) as f:
        f = f.readlines()
    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                print (line[:-1])
                break
for subdir, dirs, files in os.walk("C:/Users/visha/Desktop/Nutanix Hackathon/hack/public/python/log_simulator/"):
    print(subdir);
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".log"):
        	filedic.append(filepath)
p=Pool(len(filedic))
p.map(logger,filedic)