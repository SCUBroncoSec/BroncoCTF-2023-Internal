
USERNAME = "login_lover"
PASSWORD = "thisisalongandunbreakablepassword"
Q1 = "gizmo"
Q2 = "fey"
Q3 = "leavenworth"

def validate_user(u, p) -> bool:
    return u == USERNAME and p == PASSWORD

def validate_security_questions(u, q1, q2, q3) -> bool:
    return u == USERNAME and q1 == Q1 and q2 == Q2 and q3 == Q3