import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the synthetic data
df = pd.read_csv("data/synthetic_data.csv")

# Encode categorical variables
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df["Treatment_Group"] = df["Treatment_Group"].map({"Control": 0, "Treatment": 1})

# Define features and target
X = df[["Age", "Gender", "Biomarker_Level", "Treatment_Group"]]
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
