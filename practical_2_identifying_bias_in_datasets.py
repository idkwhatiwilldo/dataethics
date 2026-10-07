import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Gender": ["F", "M", "F", "M", "F", "M", "F", "M"],
    "Age": [22, 25, 23, 45, 24, 46, 21, 50],
    "Race": ["Asian", "Asian", "Asian", "White", "Asian", "White", "Black", "White"],
}

df = pd.DataFrame(data)

print("Gender Distribution:")
print(df["Gender"].value_counts())

print("\nRace Distribution:")
print(df["Race"].value_counts())

print("\nAge Statistics:")
print(df["Age"].describe())

df["Race"].value_counts().plot(kind="bar")
plt.title("Race Distribution")
plt.xlabel("Race")
plt.ylabel("Number of People")
plt.tight_layout()
plt.show()
