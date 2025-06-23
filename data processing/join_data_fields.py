import pandas as pd

# Load TEST
df = pd.read_csv("Dataset/test.csv")  # Replace with your actual file

# Join the first and second columns (index 0 and 1)
df["joined"] = df.iloc[:, 0].astype(str) + " " + df.iloc[:, 1].astype(str)

# Optional: Save the new CSV with the joined column
df.to_csv("Dataset/test_joined.csv", index=False)

# Load TRAIN
df = pd.read_csv("Dataset/train.csv")  # Replace with your actual file

# Join the first and second columns (index 0 and 1)
df["joined"] = df.iloc[:, 0].astype(str) + " " + df.iloc[:, 1].astype(str)

# Optional: Save the new CSV with the joined column
df.to_csv("Dataset/train_joined.csv", index=False)

# Load VALIDATION
df = pd.read_csv("Dataset/validation.csv")  # Replace with your actual file

# Join the first and second columns (index 0 and 1)
df["joined"] = df.iloc[:, 0].astype(str) + " " + df.iloc[:, 1].astype(str)

# Optional: Save the new CSV with the joined column
df.to_csv("Dataset/validation_joined.csv", index=False)
