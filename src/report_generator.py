from openpyxl import Workbook

def save_report(shortlisted,rejected,errors):

    wb = Workbook()

    ws = wb.active
    ws.title = "Final Report"

    ws.append([
        "Candidate_ID",
        "Candidate_Name",
        "Status"
    ])

    for i in shortlisted:
        ws.append([
            i["Candidate_ID"],
            i["Candidate_Name"],
            "Eligible"
        ])

    for i in rejected:
        ws.append([
            i["Candidate_ID"],
            i["Candidate_Name"],
            "Rejected"
        ])

    wb.save("../output/Final_Report.xlsx")


    wb2 = Workbook()

    ws2 = wb2.active

    ws2.title = "Errors"

    ws2.append([
        "Candidate_ID",
        "Candidate_Name",
        "Error"
    ])

    for i in errors:

        ws2.append([
            i["Candidate_ID"],
            i["Candidate_Name"],
            i["Error"]
        ])

    wb2.save("../output/Error_Report.xlsx")