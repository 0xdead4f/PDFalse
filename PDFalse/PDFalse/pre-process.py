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
def match_header(x):
  match = False
  try:
    match = re.fullmatch(r"\t%PDF-\d.\d", x)
  except:
    return -1

  if match:
    header = re.findall(r"\t%PDF-\d.\d", x)
    return header[0]
  else:
    return -1

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

pecilan = ["_Pro_Rodeo_Pix_","_Pro_Rodeo_Pix_'","(most"]
df['obj'] = df['obj'].map(lambda x: -1 if x in pecilan else x)
df.to_csv("result_pre_processed.csv",index=False)