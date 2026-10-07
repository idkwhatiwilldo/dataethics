import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Priya"],
    "Age": [20, 21, 20],
    "Marks": [85, 78, 90],
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df = df.drop("Name", axis=1)

print("\nProtected Data:")
print(df)
