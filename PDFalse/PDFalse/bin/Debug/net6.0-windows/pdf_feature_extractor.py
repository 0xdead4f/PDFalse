import csv
import sys
import fitz
import os
import subprocess
import pandas as pd
import time
import os
import signal
import re
from tabulate import tabulate

from fitz import TextPage
dir = os.getcwd()
path = []
try:
        path.append(sys.argv[1])
except:
        print("Usage: $python3 pdf-feature_extractor.py [PATH]")
        os._exit(1)
# if(not os.path.isabs(path)):      #if the given path is not absolute, we should convert it to one
#          #print("the path is path is "+str(path))
#          #print("dir is "+str(dir))
#          path = os.path.join(dir,path)
#          print("the path is not absolute and the new path is "+str(path))
# if(os.path.isdir(path)):
#         res = pd.DataFrame(columns=('pdfsize','metadata size', 'pages','xref length','title characters','isEncrypted','embedded files','images','text',''))
# else:
#         print("specify a valid pdf folder path as an argument")
#         sys.exit()
i = 0
res = pd.DataFrame(columns=('pdfsize','metadata size', 'pages','xref Length','title characters','isEncrypted','embedded files','images','text',''))

def sig_handler(signum, frame):
    print("segfault")


for j in path:
        print(j)
        f = j
        print("===========================================================")
        print("Extracting file : ",f)
        print("===========================================================")
        #pdfFileObj = open(f,'rb')
        try:
                doc = fitz.open(f)
                #print("fitz "+str(doc.xrefLength))
                #file = open(f, 'rb')
        except:
                continue
        #metadata
        metadata = doc.metadata
        print("metadata is "+str(metadata))

        #title
        if metadata:
                title = metadata['title']
        else:
                title = ""
        if not title:
                title = ""
        print("title is "+str(title))

        #whether file is encrypted
        isEncrypted = metadata['encryption']
        if(not isEncrypted):
                isEncrypted = 0
        else:
                isEncrypted = 1
        #number of objects
        objects = doc.xref_length()
        print("object is "+str(object))

        # printing number of pages in pdf file
        numPages = doc.page_count
        print("numpages is "+str(numPages))

        #extracted size
        pdfsize = int(os.path.getsize(f)/1000)
        print("pdfsize is "+str(pdfsize))

        #extracted text
        found = "No"
        text = ""
        embedcount = doc.embfile_count()
        print("embedcount is "+str(embedcount))
        
        try:
                for page in doc:
                        text += page.get_text()
                        if (len(text) > 100):
                                found = "Yes"
                                break
        except:
         #       break
                 found = "unclear"
                 res.loc[i] = [pdfsize, len(str(metadata).encode('utf-8'))] + [numPages] + [objects] + [len(title)] + [isEncrypted] + [embedcount] + [-1] + [found] +['']
                 i +=1
                 continue
        print("file contains text " + str(found))
        # number of embedded files
        

        
        #number of images
        imgcount = 0
        try:
                for k in range(len(doc)):
                        try:
                                # print(doc.get_page_images(k))
                                imgcount = len(doc.get_page_images(k)) + imgcount
                        except:  
                                imgcount = -1
                                break
                 

        except:
                continue
        print("image no is "+str(imgcount)+"\n")




        #writing the features in a csv file
        res.loc[i] = [pdfsize, len(str(metadata).encode('utf-8'))] + [numPages] + [objects] + [len(title)] + [isEncrypted] + [embedcount] + [imgcount] + [found] +['']
        i +=1
# res.to_csv(os.path.relpath("result.csv",start=os.curdir))
res = res.drop(res.columns[9], axis = 1)
print("general features extracted successfully...")
print("extracting structural features...")        #extracting structural features using pdfid
var =  str(r"tr '\n' ','")
command = ""
header = ['header','obj','endobj','stream','endstream','xref','trailer','startxref','pageno' ,'encrypt','ObjStm','JS','Javascript','AA','OpenAction','Acroform','JBIG2Decode','RichMedia','launch','EmbeddedFile','XFA','Colors']
df = pd.DataFrame(columns=header)
res = pd.concat([res, df], axis=1)


with open(os.path.relpath("pdfid/output.csv"),'w',encoding='UTF8') as output:
        output.write(','.join(header))
        os.chdir('pdfid')
        t0 = time.time()
        i = 0
        for j in path:
                f = j
                out = subprocess.check_output(f"python pdfid.py {f}", shell=True, universal_newlines=True)
                print(out)
                head = re.search(r'PDF-Header: (.*)', out).group(1)
                numbers = [int(x) for x in re.findall(r'\s\d+\n', out)]
                print(numbers)
                res[header[0]][i] = head
                for j in range(1,22):
                        res[header[j]][i] = numbers[j]
                i = i + 1

        d = time.time() - t0    
        print("duration: %.2f s." % d)
os.chdir('../')
print(tabulate(res, headers='keys', tablefmt='fancy_grid'))
res.to_csv(os.path.relpath("result.csv",start=os.curdir),index=False)










