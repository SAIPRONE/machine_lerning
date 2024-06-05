# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:15:09 2024

@author: Helal Fadi 2312951
"""
#%% LOADING & PREPROCESSING THE DATA

import pandas as pd

# Load the dataset
file_path = 'house-votes-84.data'
column_names = ['party', 'handicapped-infants', 'water-project-cost-sharing', 
                'adoption-of-the-budget-resolution', 'physician-fee-freeze', 'el-salvador-aid', 
                'religious-groups-in-schools', 'anti-satellite-test-ban', 'aid-to-nicaraguan-contras', 
                'mx-missile', 'immigration', 'synfuels-corporation-cutback', 'education-spending', 
                'superfund-right-to-sue', 'crime', 'duty-free-exports', 
                'export-administration-act-south-africa']

# Read the data into a DataFrame, specifying there's no header in the file and naming the columns
df = pd.read_csv(file_path, header=None, names=column_names)

# Preprocess the data: Convert 'y' to 1, 'n' to -1, and '?' to 0 
df.replace({'y': 1, 'n': -1, '?': 0}, inplace=True)

# Display the first few rows of the preprocessed DataFrame to verify that all correct.
df.head()

#%% KNN ClASSIFIER APPLICATION
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Prepare the data
X = df.drop('party', axis=1)  # Features
y = df['party']  # Target variable

# Encode the target variable
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Initialize the kNN classifier
knn = KNeighborsClassifier(n_neighbors=1)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Scenario 1: Congressman who would answer 'y' to all legal questions
yes_votes = [[1] * X.shape[1]]  # A list of lists with all 1s
yes_man_proba = knn.predict_proba(yes_votes)
yes_man_party = encoder.inverse_transform(knn.predict(yes_votes))

# Scenario 2: Congressman with mixed votes 'y,y,y,n,n,n,n,y,y,n,y,n,n,y,y,y'
mixed_votes = [[1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1]]
mystery_man_proba = knn.predict_proba(mixed_votes)
mystery_man_party = encoder.inverse_transform(knn.predict(mixed_votes))

# Scenario 3: Congressman 100% sure to be a Republican (using training data with known Republicans)
republican_index = y_train == encoder.transform(['republican'])[0]
re_votes = X_train[republican_index].iloc[0].values.reshape(1, -1)  # Using the first known Republican's votes
re_man_proba = knn.predict_proba(re_votes)
re_man_party = encoder.inverse_transform(knn.predict(re_votes))

#%% PLOTING
(yes_man_party[0], max(yes_man_proba[0])), (mystery_man_party[0], max(mystery_man_proba[0])), (re_man_party[0], max(re_man_proba[0]))
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(df.drop('party', axis=1), cmap='coolwarm', cbar_kws={'label': 'Vote'})
heatmap.set_title('Voting Behavior Heatmap')
plt.show()
