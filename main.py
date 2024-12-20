import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

# cara membaca dataset
dataset = pd.read_csv("./dataset_traffic_accident_prediction1.csv")

# ========================================
# Eksplorasi Dataset
# ========================================

# Baris check data sesudah index 798
# print(dataset.iloc[798])  

# menampilkan 5 data teratas
# print(dataset.head())

# menampilkan jumlah baris dan kolom
# print(dataset.shape)

# Statistik seperti mean, median, dll.
# print(dataset.describe())

# Melihat kolom dengan nilai kosong
# print(dataset.isnull().sum())

# ========================================
# PROCESS PREPROCESSING DATA
# ========================================

# mengisi data yang kosong dengan nilai rata-rata
# dataset["kolom"] = dataset['Kolom'].fillna(dataset['Kolom'].mean())

# menghapus data yang kosong
# dataset.dropna(inplace=True)

# menghapus data yang duplikat
# dataset.drop_duplicates(inplace=True)

# mengubah data object menjadi numerik
# dataset = pd.get_dummies(dataset, columns=["Weather", "Road_Type", "Time_of_Day", "Road_Condition", "Vehicle_Type", "Road_Light_Condition"],drop_first=True)

# mengubah data object menjadi numerik tapi tetap satu kolom dan diurutkan berdasaarkan abjad
# dataset["Accident_Severity"] = le.fit_transform(dataset["Accident_Severity"])

# mengubah data object menjadi numerik yang kita mau
# accident_severity_order = {"Low": 1, "Moderate": 2, "High": 3}
# dataset["Accident_Severity"] = dataset["Accident_Severity"].map(accident_severity_order)

dataset = pd.get_dummies(dataset, columns=["Weather", "Road_Type", "Time_of_Day", "Road_Condition", "Vehicle_Type", "Road_Light_Condition"],drop_first=True)
accident_severity_order = {"Low": 1, "Moderate": 2, "High": 3}
dataset["Accident_Severity"] = dataset["Accident_Severity"].map(accident_severity_order)
dataset["Accident_Severity"] = dataset["Accident_Severity"].fillna(0)

dataset['Traffic_Density'] = dataset['Traffic_Density'].fillna(dataset['Traffic_Density'].mean())
dataset['Speed_Limit'] = dataset['Speed_Limit'].fillna(dataset['Speed_Limit'].mean())
dataset['Number_of_Vehicles'] = dataset['Number_of_Vehicles'].fillna(dataset['Number_of_Vehicles'].mean())
dataset['Driver_Alcohol'] = dataset['Driver_Alcohol'].fillna(dataset['Driver_Alcohol'].mean())
dataset['Driver_Age'] = dataset['Driver_Age'].fillna(dataset['Driver_Age'].mean())
dataset['Driver_Experience'] = dataset['Driver_Experience'].fillna(dataset['Driver_Experience'].mean())
dataset['Accident'] = dataset['Accident'].fillna(dataset['Accident'].mean())

print(dataset.info())
# print(dataset["Accident_Severity"].head())



