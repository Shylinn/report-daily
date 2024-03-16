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
merged_df.to_excel('Total.xlsx', index=False)