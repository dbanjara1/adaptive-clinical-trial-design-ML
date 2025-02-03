from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import numpy as np

# Define the XGBoost model with optimal hyperparameters
best_model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42,
    eval_metric="logloss"
)

# Set up Stratified K-Fold Cross-Validation (5 folds)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Store the accuracy scores for each fold
cv_scores = []

# Perform the cross-validation manually
for train_index, val_index in cv.split(X, y):
    # Split the data
    X_train, X_val = X.iloc[train_index], X.iloc[val_index]
    y_train, y_val = y.iloc[train_index], y.iloc[val_index]
    
    # Train the model on the training data
    best_model.fit(X_train, y_train)
    
    # Make predictions on the validation data
    y_pred = best_model.predict(X_val)
    
    # Evaluate the model performance using accuracy score
    score = accuracy_score(y_val, y_pred)
    cv_scores.append(score)

# Print the cross-validation results
print("Cross-Validation Accuracy Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))
print("Standard Deviation:", np.std(cv_scores))
