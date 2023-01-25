information = {
    "name": "",
    "hours": "",
    "rate": "",
    "gsis": "",
    "philhealth": "",
    "housing": "",
    "tax": "",
}

prompt = {
    "name": "Enter Employee Name: ",
    "hours": "Enter number of Hours Rendered: ",
    "rate": "Enter rate per hour: ",
    "gsis": "GSIS Premium: ",
    "philhealth": "Philhealth: ",
    "housing": "Housing Loan: ",
    "tax": "Tax Rate: ",
}


def validate(value, key):
    if key == "name":
        return value
    if key == "hours":
        try:
            return float(value)
        except ValueError:
            print(
                "\033[31m", "\nInvalid Hours input. Please enter a number.", "\033[0m"
            )
            return ""
    if key == "rate":
        try:
            return float(value)
        except ValueError:
            print("\033[31m", "\nInvalid Rate input. Please enter a number.", "\033[0m")
            return ""
    if key == "gsis":
        try:
            return float(value)
        except ValueError:
            print(
                "\033[31m",
                "\nInvalid GSIS Premium input. Please enter a number.",
                "\033[0m",
            )
            return ""
    if key == "philhealth":
        try:
            return float(value)
        except ValueError:
            print(
                "\033[31m",
                "\nInvalid Philhealth input. Please enter a number.",
                "\033[0m",
            )
            return ""
    if key == "housing":
        try:
            return float(value)
        except ValueError:
            print(
                "\033[31m",
                "\nInvalid Housing Loan input. Please enter a number.",
                "\033[0m",
            )
            return ""
    if key == "tax":
        try:
            return float(value)
        except ValueError:
            print(
                "\033[31m",
                "\nInvalid Tax Rate input. Please enter a number.",
                "\033[0m",
            )
            return ""


for key in information:
    while information[key] == "":
        information[key] = validate(input(prompt[key]), key)

calculations = {
    "gross": information["hours"] * information["rate"],
    "tax": (information["hours"] * information["rate"]) * (information["tax"] / 100),
    "deductions": information["gsis"]
    + information["philhealth"]
    + information["housing"],
    "net": (information["hours"] * information["rate"])
    - (information["gsis"] + information["philhealth"] + information["housing"])
    - (information["hours"] * information["rate"]) * (information["tax"] / 100),
}

print(
    f"""====================================
Gross Salary: {int(calculations["gross"])}
Total Deductions: {calculations["deductions"] + calculations["tax"]}
Net Salary: {calculations["net"]}
"""
)
