{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3c3bebb1-1494-41ef-aa22-1e2cc850bda2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-14 05:26:40.151 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\nms31\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "# Load the saved XGBoost model\n",
    "model = joblib.load(\"xgboost_model.pkl\")\n",
    "\n",
    "# Streamlit UI\n",
    "def main():\n",
    "    st.title(\"Income Prediction using XGBoost\")\n",
    "    st.write(\"Enter the details below to predict whether a person earns more than $50K per year.\")\n",
    "    \n",
    "    # User input fields\n",
    "    education = st.selectbox(\"Education Level\", [\"Bachelors\", \"HS-grad\", \"Masters\", \"Doctorate\", \"Some-college\"])\n",
    "    marital_status = st.selectbox(\"Marital Status\", [\"Married\", \"Single\", \"Divorced\"])\n",
    "    occupation = st.selectbox(\"Occupation\", [\"Tech-support\", \"Sales\", \"Craft-repair\", \"Other-service\", \"Exec-managerial\"])\n",
    "    relationship = st.selectbox(\"Relationship\", [\"Husband\", \"Not-in-family\", \"Own-child\", \"Unmarried\"])\n",
    "    native_country = st.selectbox(\"Country\", [\"United-States\", \"Mexico\", \"India\", \"Canada\", \"Philippines\"])\n",
    "    age = st.slider(\"Age\", 18, 90, 30)\n",
    "    hours_per_week = st.slider(\"Hours per Week\", 1, 80, 40)\n",
    "    \n",
    "    # Convert inputs to model-friendly format (Dummy variables may be needed)\n",
    "    input_data = pd.DataFrame({\n",
    "        \"age\": [age],\n",
    "        \"hours_per_week\": [hours_per_week],\n",
    "        \"education_Bachelors\": [1 if education == \"Bachelors\" else 0],\n",
    "        \"education_HS-grad\": [1 if education == \"HS-grad\" else 0],\n",
    "        \"education_Masters\": [1 if education == \"Masters\" else 0],\n",
    "        \"education_Doctorate\": [1 if education == \"Doctorate\" else 0],\n",
    "        \"education_Some-college\": [1 if education == \"Some-college\" else 0],\n",
    "        \"marital_status_Married\": [1 if marital_status == \"Married\" else 0],\n",
    "        \"marital_status_Single\": [1 if marital_status == \"Single\" else 0],\n",
    "        \"marital_status_Divorced\": [1 if marital_status == \"Divorced\" else 0],\n",
    "        \"occupation_Tech-support\": [1 if occupation == \"Tech-support\" else 0],\n",
    "        \"occupation_Sales\": [1 if occupation == \"Sales\" else 0],\n",
    "        \"occupation_Craft-repair\": [1 if occupation == \"Craft-repair\" else 0],\n",
    "        \"occupation_Other-service\": [1 if occupation == \"Other-service\" else 0],\n",
    "        \"occupation_Exec-managerial\": [1 if occupation == \"Exec-managerial\" else 0],\n",
    "        \"relationship_Husband\": [1 if relationship == \"Husband\" else 0],\n",
    "        \"relationship_Not-in-family\": [1 if relationship == \"Not-in-family\" else 0],\n",
    "        \"relationship_Own-child\": [1 if relationship == \"Own-child\" else 0],\n",
    "        \"relationship_Unmarried\": [1 if relationship == \"Unmarried\" else 0],\n",
    "        \"native_country_United-States\": [1 if native_country == \"United-States\" else 0],\n",
    "        \"native_country_Mexico\": [1 if native_country == \"Mexico\" else 0],\n",
    "        \"native_country_India\": [1 if native_country == \"India\" else 0],\n",
    "        \"native_country_Canada\": [1 if native_country == \"Canada\" else 0],\n",
    "        \"native_country_Philippines\": [1 if native_country == \"Philippines\" else 0],\n",
    "    })\n",
    "    \n",
    "    # Predict button\n",
    "    if st.button(\"Predict Income\"):\n",
    "        prediction = model.predict(input_data)[0]\n",
    "        if prediction == 1:\n",
    "            st.success(\"The model predicts that the person earns more than $50K per year.\")\n",
    "        else:\n",
    "            st.error(\"The model predicts that the person earns less than or equal to $50K per year.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "24fccde9-a73b-4920-89ea-1591deee8ab3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
