import pandas as pd

data = {
    "Stakeholder": [
        "Government",
        "AI Developer",
        "Police",
        "Citizens",
        "Technology Company",
    ],
    "Responsibility": [
        "Ensure legal and ethical use",
        "Develop accurate and fair AI",
        "Use the system responsibly",
        "Protect privacy and report misuse",
        "Protect data and system security",
    ],
}

df = pd.DataFrame(data)
print("AI Stakeholder Map:\n")
print(df.to_string(index=False))
