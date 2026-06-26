from business_rules import check_candidate
from logger import write_log

def validate_candidate(row):

    try:

        candidate = {
            "Candidate_ID": row[0],
            "Candidate_Name": row[1],
            "Qualification": row[2],
            "Experience": row[3],
            "Skill_Set": row[4],
            "Expected_Salary": row[5],
            "Email_ID": row[6],
            "Mobile_Number": row[7]
        }

        return check_candidate(candidate)

    except Exception as e:

        write_log(str(e))

        return {
            "status":"Error",
            "Candidate_ID":row[0],
            "Candidate_Name":row[1],
            "Error":str(e)
        }