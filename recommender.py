import json

budget_input = "Under 10L"

with open("budget.json") as f:
    data = json.load(f)

for item in data:
    if item["budget"] == budget_input:
        print("Recommended Cars:", item["cars"])
