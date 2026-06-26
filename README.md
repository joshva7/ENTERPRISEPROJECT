# HR Recruitment Automation System

A Python-based automation project that simplifies the recruitment process by reading candidate data from an Excel file, validating business rules, and generating recruitment reports.

---

## Project Overview

The Human Resources (HR) department receives hundreds of job applications every month. Manual screening is time-consuming and may result in duplicate records, human errors, and delayed recruitment.

This project automates the candidate screening process based on predefined business rules and generates reports for HR.

---

## Features

- Read candidate data from Excel
- Qualification validation
- Experience validation
- Salary validation
- Email validation
- Exception handling
- Error logging
- Generate recruitment reports
- Dashboard generation
- Modular Python architecture

---

## Business Rules

### Qualification Validation

Eligible Qualifications:

- Degree
- Diploma
- Postgraduate

---

### Experience Validation

Minimum Experience:

- 2 Years

---

### Salary Validation

Expected Salary must be less than or equal to the company budget.

---

### Email Validation

Checks whether the email contains:

- @
- .

---

## Project Structure

```
DitProject/

│
├── documentation/
│     └── Project_Documentation.docx
│
├── input/
│     └── Input_Data.xlsx
│
├── logs/
│     └── error_log.txt
│
├── output/
│     ├── Dashboard_Report.xlsx
│     ├── Error_Report.xlsx
│     └── Final_Report.xlsx
│
└── src/
      ├── main.py
      ├── validation.py
      ├── business_rules.py
      ├── dashboard.py
      ├── report_generator.py
      └── logger.py
```

---

## Technologies Used

- Python 3
- OpenPyXL
- Exception Handling
- File Handling
- Modular Programming

---

## Output Files

- Final_Report.xlsx
- Error_Report.xlsx
- Dashboard_Report.xlsx
- error_log.txt

---

## Dashboard Output

```
Recruitment Dashboard

Total Applicants
Eligible Candidates
Rejected Candidates
Errors
```

---

## How to Run

### Install Dependency

```bash
pip install openpyxl
```

### Run Project

```bash
cd src

python main.py
```

---

## Sample Input

```
Candidate_ID
Candidate_Name
Qualification
Experience
Skill_Set
Expected_Salary
Email_ID
Mobile_Number
```

---

## Future Enhancements

- Resume PDF Screening
- AI Candidate Ranking
- Email Notification
- HR Management Dashboard
- Database Integration
- Web Application using Flask/Django

---

## Author

Pradeesh Kumar

GitHub:
https://github.com/joshva7
