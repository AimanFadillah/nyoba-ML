import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt

model = RandomForestClassifier()
le = LabelEncoder()
scaler = MinMaxScaler()
# >> Cara membaca dataset
dataset = pd.read_csv("./dataset_traffic_accident_prediction1.csv")

# ========================================
# Eksplorasi Dataset
# ========================================

# >> Baris check data sesudah index 798
# print(dataset.iloc[798])  

# >> menampilkan 5 data teratas
# print(dataset.head())

# >> menampilkan jumlah baris dan kolom
# print(dataset.shape)

# >> Statistik seperti mean, median, dll.
# print(dataset.describe())

# >> Melihat kolom dengan nilai kosong
# print(dataset.isnull().sum())

# ========================================
# PROCESS PREPROCESSING DATA
# ========================================

# >> mengisi data yang kosong dengan nilai rata-rata
# dataset["kolom"] = dataset['Kolom'].fillna(dataset['Kolom'].mean())

# >> menghapus data yang kosong
# dataset.dropna(inplace=True)

# >> menghapus data yang duplikat
# dataset.drop_duplicates(inplace=True)

# >> mengubah data object menjadi numerik
# dataset = pd.get_dummies(dataset, columns=["Weather", "Road_Type", "Time_of_Day", "Road_Condition", "Vehicle_Type", "Road_Light_Condition"],drop_first=True)

# >> mengubah data object menjadi numerik tapi tetap satu kolom dan diurutkan berdasarkan abjad
# dataset["Accident_Severity"] = le.fit_transform(dataset["Accident_Severity"])

# >> mengubah data object menjadi numerik yang kita mau
# accident_severity_order = {"Low": 1, "Moderate": 2, "High": 3}
# dataset["Accident_Severity"] = dataset["Accident_Severity"].map(accident_severity_order)

# >> Mengubah nilai ke skala tertentu (misalnya 0 hingga 1) [Normalisasi dan standarisasi]
# dataset[['Fitur']] = scaler.fit_transform(dataset[['Fitur']])

# >> membuat fitur baru atau column baru
# dataset['Bulan'] = dataset['Tanggal'].dt.month

# >> menghapus kolom yang tidak diperlukan
# dataset.drop(['Kolom'], axis=1, inplace=True)

# >> memasukkan semua kolom kecuali label yang dipilih
# X = dataset.drop('label', axis=1)

# >> memasukkan kolom yang dipilih
# X = dataset[['Luas_Rumah', 'Jumlah_Kamar']]

# >> untuk ngecheck apakah pola data sudah bener atau belum
# sns.boxplot(x=dataset['Traffic_Density'])
# plt.show()

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
dataset["Accident"] = dataset["Accident"].fillna(0)

dataset.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)

dataset[['Traffic_Density']] = scaler.fit_transform(dataset[['Traffic_Density']])
dataset[['Speed_Limit']] = scaler.fit_transform(dataset[['Speed_Limit']])
dataset[['Number_of_Vehicles']] = scaler.fit_transform(dataset[['Number_of_Vehicles']])
dataset[['Driver_Alcohol']] = scaler.fit_transform(dataset[['Driver_Alcohol']])
dataset[['Driver_Age']] = scaler.fit_transform(dataset[['Driver_Age']])
dataset[['Driver_Experience']] = scaler.fit_transform(dataset[['Driver_Experience']])
dataset[['Accident_Severity']] = scaler.fit_transform(dataset[['Accident_Severity']])

# ========================================
# TRAINING DATA dan TESTING DATA
# ========================================

x = dataset.drop('Accident', axis=1)
y = dataset["Accident"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

# >> Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy}')

# >> Menampilkan confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# >> Menampilkan laporan klasifikasi (precision, recall, f1-score)
print("Classification Report:")
print(classification_report(y_test, y_pred))




