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

for j in path:
        print("test")
        print(j)
        f = j
        try:
                doc = fitz.open(f)
                
        except:
                continue

        metadata = doc.metadata
        

        #title
        if metadata:
                title = metadata['title']
        else:
                title = ""
        if not title:
                title = ""
        # print("title is "+str(title))

        #whether file is encrypted
        isEncrypted = metadata['encryption']
        if(not isEncrypted):
                isEncrypted = 0
        else:
                isEncrypted = 1
        #number of objects
        objects = doc.xref_length()
        # print("object is "+str(object))

        # printing number of pages in pdf file
        numPages = doc.page_count
        # print("numpages is "+str(numPages))

        #extracted size
        pdfsize = int(os.path.getsize(f)/1000)
        # print("pdfsize is "+str(pdfsize))

        #extracted text
        found = "No"
        text = ""
        embedcount = doc.embfile_count()
        # print("embedcount is "+str(embedcount))
        
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
        # print("file contains text " + str(found))
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
        # print("image no is "+str(imgcount)+"\n")




        #writing the features in a csv file
        res.loc[i] = [pdfsize, len(str(metadata).encode('utf-8'))] + [numPages] + [objects] + [len(title)] + [isEncrypted] + [embedcount] + [imgcount] + [found] +['']
        i +=1
res = res.drop(res.columns[9], axis = 1)
# print("general features extracted successfully...")
# print("extracting structural features...")       
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
                # print(out)
                head = re.search(r'PDF-Header: (.*)', out).group(1)
                numbers = [int(x) for x in re.findall(r'\s\d+\n', out)]
                # print(numbers)
                res[header[0]][i] = head
                for j in range(1,22):
                        res[header[j]][i] = numbers[j]
                i = i + 1

        d = time.time() - t0    
        # print("duration: %.2f s." % d)
os.chdir('../')
print(tabulate(res, headers='keys', tablefmt='fancy_grid'))
res.to_csv(os.path.relpath("result.csv",start=os.curdir),index=False)

###########################################################################
#
#
# PRE PROCESS
#
#
###########################################################################

import pandas as pd
import numpy as np

df = res

#Filling Null Value with zero
df.fillna(0, inplace = True)

#Converting -1 to integer
integer_column = ["images", "text", "header","obj","endobj","endstream","xref","startxref","pageno","JS","Javascript","AA","OpenAction","Acroform","JBIG2Decode","RichMedia","launch","EmbeddedFile","XFA"]
df[integer_column] = df[integer_column].applymap(lambda x: -1 if x == '-1' else x)

#fixing data with parentheses
parentheses_column = ["images","endstream","pageno","JS","Javascript","AA","OpenAction","Acroform","JBIG2Decode","RichMedia","launch","EmbeddedFile","XFA"]
def get_parentheses(x):
  try :
    if '(' in x:
      matches = re.findall(r"\d+(?=\()", x)
      return int(matches[0])
    else:
      return x
  except:
    return x

df[parentheses_column] = df[parentheses_column].applymap(lambda x: get_parentheses(x))

#Fixing version in header data
head = {'%PDF-0.1': 1, '%PDF-0.2': 2, '%PDF-0.3': 3, '%PDF-0.4': 4, '%PDF-0.5': 5, '%PDF-0.6': 6, '%PDF-0.7': 7, '%PDF-0.8': 8, '%PDF-0.9': 9, '%PDF-0.10': 10, '%PDF-1.1': 11, '%PDF-1.2': 12, '%PDF-1.3': 13, '%PDF-1.4': 14, '%PDF-1.5': 15, '%PDF-1.6': 16, '%PDF-1.7': 17, '%PDF-1.8': 18, '%PDF-1.9': 19, '%PDF-2.0': 20, '%PDF-2.1': 21, '%PDF-2.2': 22, '%PDF-2.3': 23, '%PDF-2.4': 24}

def match_header(x):
  head_match = None
  for i in head.keys():
    if i in x:
      head_match = i
      break
  
  if head_match == None:
    return -1

  return head[head_match]   

df[['header']] = df[['header']].applymap(lambda x: match_header(x))

#Convert other data other data to -1
other = ["obj","endobj","endstream","xref","startxref","pageno","Javascript"]
def other_data(col):
  other_data_value = []
  df_test[col].str.isnumeric() 
  df_temp_numeric = df_test[col].str.isnumeric()
  df_temp_numeric = pd.concat({col:df[col],'value':df_temp_numeric},axis=1)
  for i in df_temp_numeric.query("`value` == False").value_counts().index:
    other_data_value.append(i[0])
  return other_data_value

def replace_other_data(x):
  if x in other_data_value:
    return -1
  else:
    return x 

# other_data_value = []
# for col in other:
#   s_numeric = pd.to_numeric(df[col], errors='coerce')
#   # Check which values are not numeric
#   non_numeric_values = df[col][s_numeric.isna()]
#   other_data_value.append(non_numeric_values.value_counts().index[0])

# for i in other:
#   df[i] = df[i].map(lambda x: replace_other_data(x))

# One hot encode Text
text_column = ['text_-1','text_0','text_1'] 
df_text = pd.DataFrame(columns=text_column)
df = pd.concat([df, df_text], axis=1)
df[text_column] = 0

if df['text'][0] == 'No':
  df['text_0'] = 1
elif df['text'][0] == 'Yes':
  df['text_1'] = 1
else:
  df['text_-1'] = 1
df = df.drop('text',axis=1)

pecilan = ["_Pro_Rodeo_Pix_","_Pro_Rodeo_Pix_'","(most"]
df['obj'] = df['obj'].map(lambda x: -1 if x in pecilan else x)
# df.to_csv("result_pre_processed.csv",index=False)

###########################################################################
#
#
# Predict
#
#
###########################################################################

import joblib
import sys
import xgboost as xgb

# file = sys.argv[1]
# Load the model from the file
model = joblib.load('model_gb.pkl')

# df = pd.read_csv(file)
result = model.predict(df)
print(result[0])




