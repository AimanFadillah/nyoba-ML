import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
scaler = MinMaxScaler()
dataset = pd.read_csv("./diabetes_prediction_dataset.csv")
dataset = pd.get_dummies(dataset, columns=["gender", "smoking_history"])

columns_to_scale = ["blood_glucose_level", "HbA1c_level", "bmi", "age"]
dataset[columns_to_scale] = scaler.fit_transform(dataset[columns_to_scale])

print(dataset.head())

x = dataset.drop("diabetes", axis=1)
y = dataset["diabetes"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(x_train.info())

model.fit(x_train, y_train)

def get_user_input():
    gender = input("Masukkan gender (Male/Female/Other): ")
    smoking_history = input("Masukkan riwayat merokok (No Info/current/ever/former/never/no current): ")
    age = float(input("Masukkan usia: "))
    bmi = float(input("Masukkan BMI: "))
    blood_glucose_level = float(input("Masukkan level gula darah: "))
    HbA1c_level = float(input("Masukkan level HbA1c: "))

    input_data = pd.DataFrame({
        "gender": [gender],
        "smoking_history": [smoking_history],
        "age": [age],
        "bmi": [bmi],
        "blood_glucose_level": [blood_glucose_level],
        "HbA1c_level": [HbA1c_level],
    })

    input_data = pd.get_dummies(input_data, columns=["gender", "smoking_history"])
    input_data = input_data.reindex(columns=x.columns, fill_value=0)

    input_data[columns_to_scale] = scaler.transform(input_data[columns_to_scale])

    print(input_data.head())

    return input_data

user_input = get_user_input()
prediction = model.predict_proba(user_input)
print(f"Probabilitas diabetes: {prediction[0, 1] * 100:.2f}%")
