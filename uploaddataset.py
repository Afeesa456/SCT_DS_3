from google.colab import files
import pandas as pd

uploaded = files.upload()

df = pd.read_csv("bank-full.csv", sep=";") 
df.head()
