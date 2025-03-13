## Adult-Income-Dataset
A machine learning project on the Adult Income dataset from the USA. In this dataset, I have implemented classification model algorithms to predict if an individual earns an annual salary of USD 50000 or not.

### Overview

This project focuses on predicting income levels based on demographic and employment-related attributes using the UCI Adult Income dataset. The goal is to classify individuals into two income categories:

1. Less than or equal to 50K

2. Greater than 50K

This is a binary classification problem, and various machine learning models were implemented to achieve high accuracy.

### Workflow Summary

**1. Data Collection & Preprocessing**

The dataset was loaded and inspected for missing values.

Data cleaning techniques such as handling null values, duplicates, and inconsistent data formats were applied.

Categorical features were encoded using One-Hot Encoding and Label Encoding.

The dataset was scaled using StandardScaler to improve model performance.

**2. Exploratory Data Analysis (EDA)**

*Univariate Analysis:* Distribution of categorical and numerical features.

*Bivariate Analysis:* Relationship between income level and other features.

*Class Distribution:* Checked for data imbalance.

*Correlation Analysis:* Identified relationships between different variables.

*Feature Selection:* Used Mutual Information (MI) and Chi-Square tests to select important features.

**3. Handling Imbalanced Data**

The dataset was imbalanced, so SMOTE (Synthetic Minority Oversampling Technique) was applied to balance the classes.

**4. Model Training & Evaluation**

The dataset was split into training (80%) and testing (20%) sets. Multiple machine learning models were implemented and compared:

**XGBoost** achieved the highest AUC-ROC score of 0.95, making it the best-performing model. It scored an accuracy of **86.93%**

Confusion matrices and classification reports were generated for all models.

**5. Model Deployment using Streamlit**

The XGBoost model was saved using joblib. A Streamlit web application was built to allow users to input demographic data and predict income levels.
The app was designed with a user-friendly interface for easy interaction.

**Key Features of the Project**

✔️ End-to-end machine learning pipeline from data preprocessing to model deployment.

✔️ Multiple model evaluation for best performance comparison.

✔️ SMOTE applied to handle imbalanced data.

✔️ AUC-ROC Curve Analysis for model performance evaluation.

✔️ Interactive Streamlit Web App for real-time predictions.

**Next Steps**

1. Hyperparameter tuning to further improve accuracy.
2. Feature engineering for better data representation.
3. Deploying the model on cloud platforms like AWS or Heroku.
