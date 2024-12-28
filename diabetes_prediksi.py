import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
scaler = MinMaxScaler()
dataset = pd.read_csv("./diabetes_prediction_dataset.csv")
dataset = pd.get_dummies(dataset,columns=["gender","smoking_history"])

dataset[["blood_glucose_level"]] = scaler.fit_transform(dataset[["blood_glucose_level"]])
dataset[["HbA1c_level"]] = scaler.fit_transform(dataset[["HbA1c_level"]])
dataset[["bmi"]] = scaler.fit_transform(dataset[["bmi"]])
dataset[["age"]] = scaler.fit_transform(dataset[["age"]])

x = dataset.drop("diabetes",axis=1)
y = dataset["diabetes"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model.fit(x_train,y_train)

y_pred = model.predict_proba(x_test)

print(f"{y_pred[0, 1] * 100:.2f}%")




