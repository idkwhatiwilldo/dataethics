import pandas as pd

data = {
    "Student": ["Asha", "Rahul", "Priya", "Amit"],
    "Attendance": [90, 60, 85, 55],
    "Marks": [80, 45, 75, 40],
}

df = pd.DataFrame(data)

df["Support_Required"] = (
    (df["Attendance"] < 75) | (df["Marks"] < 50)
)

print(df)

risks_and_mitigation = pd.DataFrame({
    "Risk": [
        "Incorrect prediction",
        "Privacy violation",
        "Bias",
        "Wrong decision",
    ],
    "Mitigation": [
        "Teacher verification",
        "Protect and anonymize data",
        "Regular fairness testing",
        "Keep human in the loop",
    ],
})

print("\nPotential Risks and Mitigation:")
print(risks_and_mitigation.to_string(index=False))
