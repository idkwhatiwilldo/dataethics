import pandas as pd

data = {
    "Gender": ["F", "F", "F", "M", "M", "M"],
    "Actual": [1, 1, 0, 1, 1, 0],
    "Predicted": [1, 1, 1, 1, 0, 0],
}

df = pd.DataFrame(data)

demographic_parity = df.groupby("Gender")["Predicted"].mean()
print("Demographic Parity:")
print(demographic_parity)

equal_opportunity = df.groupby("Gender").apply(
    lambda group: group.loc[group["Actual"] == 1, "Predicted"].mean()
)
print("\nEqual Opportunity (TPR):")
print(equal_opportunity)
