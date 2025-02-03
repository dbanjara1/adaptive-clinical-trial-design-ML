## **Scripts**

### **1. `data_generation.py`**
```python
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(123)

# Generate synthetic data
n_patients = 1000
data = {
    "Patient_ID": np.arange(1, n_patients + 1),
    "Age": np.random.randint(18, 80, size=n_patients),
    "Gender": np.random.choice(["Male", "Female"], size=n_patients),
    "Biomarker_Level": np.random.normal(50, 10, size=n_patients),  # Mean = 50, Std = 10
    "Treatment_Group": np.random.choice(["Treatment", "Control"], size=n_patients),
    "Outcome": np.random.choice([0, 1], size=n_patients, p=[0.6, 0.4])  # 40% response rate
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/synthetic_data.csv", index=False)

print("Synthetic data generated and saved to data/synthetic_data.csv.")
