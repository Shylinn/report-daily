import subprocess
import os
import pandas as pd
import warnings
warnings.simplefilter("ignore")


file_path1 = "D:\\Report 1 ngày\\ghep.py"
file_path2="D:\\Report 1 ngày\\Titkok\\ghep.py"
file_path3="D:\\Report 1 ngày\\Twitter\\ghep.py"

subprocess.run(["python", file_path1])
subprocess.run(["python", file_path2])
subprocess.run(["python", file_path3])

df1 = pd.read_excel('D:\\Report 1 ngày\\Chi-phí-1-ngày.xlsx')
df2 = pd.read_excel('D:\\Report 1 ngày\\Tiktok 1 ngày.xlsx')
df3 = pd.read_excel('D:\\Report 1 ngày\\Twitter 1 ngày.xlsx')

merged_df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
merged_df = merged_df[~((merged_df['Campaign name'].str.contains('total', case=False, na=False)) | (merged_df['Attribution setting'] == 0))]
merged_df.to_excel('Total.xlsx', index=False)
df = pd.read_excel('Total.xlsx')
filtered_df = df[['Account name', 'Reach', 'Campaign delivery']].loc[df['Campaign delivery'].str.lower().isin(['active', 'Active'])]
filtered_df = filtered_df.drop_duplicates(subset=['Account name', 'Reach', 'Campaign delivery'])
with pd.ExcelWriter('Total.xlsx', engine='openpyxl', mode='a') as writer:
    filtered_df.to_excel(writer, sheet_name='Sheet2', index=False)
new_df = pd.read_excel('Total.xlsx', sheet_name='Sheet2')
acc_data_df = new_df['Reach'].drop_duplicates()
with pd.ExcelWriter('Total.xlsx', engine='openpyxl', mode='a') as writer:
    acc_data_df.to_excel(writer, sheet_name='Sheet3', index=False)
demo = pd.read_excel('Total.xlsx', sheet_name='Sheet3')
newfiltered_df=pd.read_excel('Total.xlsx',sheet_name='Sheet2')
def checkAcc(maCamp):
   
    row_phuhop=newfiltered_df.loc[newfiltered_df["Reach"]==maCamp,"Account name"]
    return ", ".join(map(str, row_phuhop))
demo['Acc']=demo['Reach'].apply(checkAcc)

with pd.ExcelWriter('Total.xlsx', engine='openpyxl', mode='a') as writer:
    demo.to_excel(writer, sheet_name='Account', index=False)


