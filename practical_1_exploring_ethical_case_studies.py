import pandas as pd

data = {
    "Student": ["Asha", "Rahul", "Priya", "Amit", "Neha", "Vikas"],
    "Gender": ["F", "M", "F", "M", "F", "M"],
    "Score": [85, 80, 90, 75, 82, 88],
}

df = pd.DataFrame(data)
df["Decision"] = df["Score"].apply(
    lambda score: "Selected" if score >= 80 else "Rejected"
)

print("Student Selection Results:")
print(df)

selection_rate = df.groupby("Gender")["Decision"].apply(
    lambda decisions: (decisions == "Selected").mean() * 100
)

print("\nSelection Rate by Gender:")
print(selection_rate)

print("\nSelected Students:")
print(df[df["Decision"] == "Selected"])

print("\nRejected Students:")
print(df[df["Decision"] == "Rejected"])
