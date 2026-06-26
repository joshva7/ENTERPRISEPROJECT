from openpyxl import Workbook

def show_dashboard(shortlisted,rejected,errors):

    total = len(shortlisted)+len(rejected)+len(errors)

    print("\nRECRUITMENT DASHBOARD")
    print("---------------------------")
    print("Total Applicants :",total)
    print("Eligible :",len(shortlisted))
    print("Rejected :",len(rejected))
    print("Errors :",len(errors))

    wb = Workbook()

    ws = wb.active

    ws.append(["Metric","Value"])

    ws.append(["Total Applicants",total])
    ws.append(["Eligible",len(shortlisted)])
    ws.append(["Rejected",len(rejected)])
    ws.append(["Errors",len(errors)])

    wb.save("../output/Dashboard_Report.xlsx")