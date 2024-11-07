# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df = pd.read_csv('data/1 NACH_AbsoluteData.xlsx - Sheet1.csv')
woe = pd.read_csv('data/woe_NACH3.csv')
df.columns.get_loc("A_Rank")

for i in [16, 13, 22, 24, 17, 2, 26, 12, 6, 9, 18, 23]:
    for j, var in enumerate(woe['Variable']):
        if var == df.columns[i] :
            df[df.columns[i]] = df[df.columns[i]].replace([woe['Cutoff'][j]], woe['WoE'][j])

X = df.iloc[:, [16, 13, 22, 24, 17, 2, 26, 12, 6, 9, 18, 23]].values
Y = df.iloc[:, -1].values



# Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_test)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)#Logistic Regression
acc = (cm[1][1] + cm[0][0])/(cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])*100
