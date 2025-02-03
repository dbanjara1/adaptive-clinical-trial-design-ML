# Adaptive Clinical Trial Design using Machine Learning

This project demonstrates how machine learning can be applied to adaptive clinical trial design. It includes synthetic data generation, model training, and hyperparameter tuning to predict patient outcomes and optimize trial parameters.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [License](#license)

## Project Overview

Predicting Patient Outcomes

Objective: Use machine learning to predict whether a patient will respond to treatment (Outcome = 1) or not (Outcome = 0).

Impact:
✅ Early identification of non-responders, allowing adaptive modifications.
✅ Personalized treatment adjustments, improving efficacy.
2️⃣ Dynamic Treatment Reallocation

Objective: Identify which patient subgroups benefit most from treatment.

Impact:
✅ More patients receive effective treatments instead of being randomly assigned.
✅ Ethical benefits—fewer patients exposed to ineffective therapies.
3️⃣ Early Stopping Decisions

Objective: Predict if a trial is likely to fail or succeed before full completion.

Impact:
✅ Trials can stop early if treatment is ineffective, saving resources.
✅ If a strong positive signal is detected, trials can be accelerated.

🧑‍🔬 What This Dataset Contains

Patient Demographics: Age, gender, ethnicity, etc.

Medical History: Pre-existing conditions, prior treatments, etc.

Treatment Details: Drug dosage, treatment duration, etc.

Biomarkers: Multiple biomarkers (e.g., blood pressure, cholesterol levels, etc.).

Adverse Events: Occurrence of adverse events during the trial.

Outcome: Primary outcome (e.g., response to treatment).

## Folder Structure

adaptive-clinical-trial/
├── README.md
├── data/
│ ├── synthetic_data.csv
├── scripts/
│ ├── data_generation.py
│ ├── model_training.py
│ ├── hyperparameter_tuning.py
├── models/
│ ├── best_xgboost_model.pkl
├── notebooks/
│ ├── exploratory_analysis.ipynb
├── requirements.txt
├── LICENSE

Copy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dbanjara1/adaptive-clinical-trial-design-ML.git
   cd adaptive-clinical-trial
Install the required Python packages:

bash
Copy
pip install -r requirements.txt
Usage
1. Generate Synthetic Data
Run the data_generation.py script to generate synthetic clinical trial data:

bash
Copy
python scripts/data_generation.py

2. Train and Evaluate Models
Run the model_training.py script to train and evaluate machine learning models:

bash
Copy
python scripts/model_training.py

3. Hyperparameter Tuning
Run the hyperparameter_tuning.py script to optimize model hyperparameters:

bash
Copy
python scripts/hyperparameter_tuning.py

4. Exploratory Data Analysis
Open the exploratory_analysis.ipynb notebook to explore the dataset and visualize results.

## Results

Best Model: XGBoost with an accuracy of 75% on the test set.

Feature Importance: Biomarker level and treatment group were the most important features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
