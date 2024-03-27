import subprocess
import os
import pandas as pd
import warnings
warnings.simplefilter("ignore")
file_path1 = "D:\\Report 3 ngày\\ghep.py"
file_path2="D:\\Report 3 ngày\\Titkok\\ghep.py"
file_path3="D:\\Report 3 ngày\\Twitter\\ghep.py"

subprocess.run(["python", file_path1])
subprocess.run(["python", file_path2])
subprocess.run(["python", file_path3])

df1 = pd.read_excel('D:\\Report 3 ngày\\Chi-phí-3-ngày.xlsx')
df2 = pd.read_excel('D:\\Report 3 ngày\\Tiktok 3 ngày.xlsx')
df3 = pd.read_excel('D:\\Report 3 ngày\\Twitter 3 ngày.xlsx')

merged_df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
merged_df = merged_df[~((merged_df['Campaign name'].str.contains('total', case=False, na=False)) | (merged_df['Attribution setting'] == 0))]
merged_df.to_excel('Total.xlsx', index=False)