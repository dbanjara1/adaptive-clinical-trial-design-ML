import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the synthetic data
df = pd.read_csv("data/adaptive_clinical_trial_data.csv")

# Encode categorical variables
df = pd.get_dummies(df, columns=["Gender", "Ethnicity", "Smoking_Status", "Treatment_Group"], drop_first=True)

# Define features and target
X = df.drop(columns=["Patient_ID", "Outcome"])
y = df["Outcome"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Train an XGBoost model
model = XGBClassifier(random_state=123, use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))
