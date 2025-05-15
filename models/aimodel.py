import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib


cancer = load_breast_cancer()


X,y  = load_breast_cancer(return_X_y=True)
# print(X.shape)
X = X[:, :-20]
model = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


smote = SMOTE()
X_res, y_res = smote.fit_resample(X_train_scaled, y_train)





model.fit(X_res, y_res)


# y_pred = model.predict_proba(X_test_scaled)
# y_percent = y_pred*100
# for i in range(10):
#     print(y_percent[i,0])

joblib.dump(scaler, 'scaler.pkl')
joblib.dump(model, 'model.pkl')
