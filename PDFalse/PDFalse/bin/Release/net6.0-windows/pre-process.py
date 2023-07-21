import pandas as pd
import numpy as np

df = pd.read_csv("result.csv")

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
df.to_csv("result_pre_processed.csv",index=False)