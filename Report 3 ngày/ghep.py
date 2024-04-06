import os
import pandas as pd
import warnings

warnings.simplefilter("ignore")
df = pd.read_excel('My-3-ngày.xlsx')
def tachcamp(str):
    arr = str.split("_")
    max=arr[0]
    for i in range(0,len(arr)):
        if len(arr[i])>len(max):
            max=arr[i]
    return max
def UTM(input_string):
    index = input_string.find("_", 15)
    result = input_string[index + 1:]
    
    result = result.replace('_Nga', '')
    result = result.replace('_Thuy', '')
    result = result.replace('_Thuan', '')
    result = result.replace('_Thienco', '')
    result = result.replace('_Hieu', '')
    return result

# Đổi tên cột
df = df.rename(columns={'Campaign Delivery': 'Campaign delivery'})
df.to_excel('My-3-ngày.xlsx', index=False)

df1 = pd.read_excel('My-3-ngày.xlsx')
df2 = pd.read_excel('TC-3-ngày.xlsx')
df3 = pd.read_excel('Yino-3-ngày.xlsx')
df4 = pd.read_excel('Yino-Tech-3-ngày.xlsx')
merged_df = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)
merged_df.to_excel('Chi-phí-3-ngày.xlsx', index=False)

newdf = pd.read_excel('Chi-phí-3-ngày.xlsx')
newdf['Reach'] = newdf['Campaign name'].apply(tachcamp)
newdf['Impressions']=newdf['Campaign name'].apply(UTM)
for index, row in newdf.iterrows():
    if row['Account name'] == 'Dike - Maximo - Wanderprints 1' or row['Account name'] == 'Dike - Maximo - Wanderprints 2' or row['Account name'] == 'Dike - Maximo - Wanderprints 3' or row['Account name'] == 'Kiet Pets 1' :
        newdf.at[index, 'Attribution setting'] = 1.05 * row['Amount spent (USD)']
    else:
        newdf.at[index, 'Attribution setting'] = row['Amount spent (USD)']
newdf.to_excel('Chi-phí-3-ngày.xlsx', index=False)