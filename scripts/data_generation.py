## **Scripts**

### **1. `data_generation.py`**
```python
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(123)

# Number of patients
n_patients = 1000

# Generate synthetic data
data = {
    "Patient_ID": np.arange(1, n_patients + 1),
    "Age": np.random.randint(18, 80, size=n_patients),
    "Gender": np.random.choice(["Male", "Female"], size=n_patients, p=[0.5, 0.5]),
    "Ethnicity": np.random.choice(["Caucasian", "African American", "Asian", "Hispanic"], size=n_patients),
    "BMI": np.round(np.random.normal(25, 5, size=n_patients), 1),  # Body Mass Index
    "Smoking_Status": np.random.choice(["Never", "Former", "Current"], size=n_patients),
    "Diabetes": np.random.choice([0, 1], size=n_patients, p=[0.8, 0.2]),  # 0 = No, 1 = Yes
    "Hypertension": np.random.choice([0, 1], size=n_patients, p=[0.7, 0.3]),  # 0 = No, 1 = Yes
    "Prior_Treatments": np.random.randint(0, 5, size=n_patients),  # Number of prior treatments
    "Treatment_Group": np.random.choice(["Placebo", "Low Dose", "High Dose"], size=n_patients),
    "Treatment_Duration": np.random.randint(30, 365, size=n_patients),  # Days
    "Biomarker_1": np.random.normal(50, 10, size=n_patients),  # Example: Blood pressure
    "Biomarker_2": np.random.normal(100, 20, size=n_patients),  # Example: Cholesterol level
    "Biomarker_3": np.random.normal(5, 1, size=n_patients),  # Example: Glucose level
    "Adverse_Event": np.random.choice([0, 1], size=n_patients, p=[0.85, 0.15]),  # 0 = No, 1 = Yes
    "Outcome": np.random.choice([0, 1], size=n_patients, p=[0.6, 0.4])  # 0 = No response, 1 = Response
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/adaptive_clinical_trial_data.csv", index=False)

print("Synthetic dataset generated and saved to data/adaptive_clinical_trial_data.csv.")

print(df.head())
