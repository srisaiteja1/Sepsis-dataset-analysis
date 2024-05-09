import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import ADASYN

# Load your CSV file
input_file = "primary_raw.csv"
output_file = "primary_upscaled_file.csv"
data = pd.read_csv(input_file)

# Separate features (X) and target variable (y)
X = data.drop('hospital_outcome_1alive_0dead', axis=1)  # Adjust 'target_column_name' accordingly
y = data['hospital_outcome_1alive_0dead']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply ADASYN to upsample the minority class
adasyn = ADASYN(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = adasyn.fit_resample(X_train, y_train)

# Concatenate resampled data with the original majority class
upscaled_data = pd.concat([X_resampled, y_resampled], axis=1)

# Save the upscaled data to a CSV file
upscaled_data.to_csv(output_file, index=False)
