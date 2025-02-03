import pandas as pd
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

# Load the synthetic data
df = pd.read_csv("data/synthetic_data.csv")

# Encode categorical variables
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df["Treatment_Group"] = df["Treatment_Group"].map({"Control": 0, "Treatment": 1})

# Define features and target
X = df[["Age", "Gender", "Biomarker_Level", "Treatment_Group"]]
y = df["Outcome"]

# Define the parameter grid for XGBoost
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 7],
    "learning_rate": [0.01, 0.1, 0.2],
    "subsample": [0.8, 0.9, 1.0],
    "colsample_bytree": [0.8, 0.9, 1.0]
}

# Initialize GridSearchCV
grid_search = GridSearchCV(
    estimator=XGBClassifier(random_state=123, use_label_encoder=False, eval_metric="logloss"),
    param_grid=param_grid,
    scoring="accuracy",
    cv=5,
    n_jobs=-1
)

# Perform grid search
grid_search.fit(X, y)

# Print the best parameters and accuracy
print("Best Parameters:", grid_search.best_params_)
print("Best Accuracy:", grid_search.best_score_)
