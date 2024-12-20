import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# cara membaca dataset
dataset = pd.read_csv("./dataset_traffic_accident_prediction1.csv")

# Eksplorasi Dataset

# menampilkan 5 data teratas
# print(dataset.head())

# menampilkan jumlah baris dan kolom
# print(dataset.shape)

# Statistik seperti mean, median, dll.
# print(dataset.describe())

# Melihat kolom dengan nilai kosong
# print(dataset.isnull().sum())

print(dataset.info())

# PROCESS PREPROCESSING DATA

# menghapus data yang kosong
# dataset.dropna(inplace=True)

# menghapus data yang duplikat
# dataset.drop_duplicates(inplace=True)


