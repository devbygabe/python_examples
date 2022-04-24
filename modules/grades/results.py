"""
Functions for calculating results.
"""


A_LIMIT = 70
B_LIMIT = 60
C_LIMIT = 50
D_LIMIT = 40
E_LIMIT = 30


def get_grade(score):
    """Accepts a score and returns letter version."""
    if score >= A_LIMIT:
        return "A"
    elif score >= B_LIMIT:
        return "B"
    elif score >= C_LIMIT:
        return "C"
    elif score >= D_LIMIT:
        return "D"
    elif score >= E_LIMIT:
        return "E"

    return "F"
