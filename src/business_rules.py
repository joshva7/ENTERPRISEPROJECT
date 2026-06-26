company_budget = 50000

valid_qualification = [
    "Degree",
    "Diploma",
    "Postgraduate"
]


def check_candidate(candidate):

    if candidate["Qualification"] not in valid_qualification:
        candidate["status"]="Rejected"
        return candidate

    if candidate["Experience"] < 2:
        candidate["status"]="Rejected"
        return candidate

    if candidate["Expected_Salary"] > company_budget:
        candidate["status"]="Rejected"
        return candidate

    email = candidate["Email_ID"]

    if "@" not in email or "." not in email:
        raise Exception("Invalid Email")

    candidate["status"]="Eligible"

    return candidate