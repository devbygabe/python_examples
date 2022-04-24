"""
Script for processing a students grades
"""

from grades.predict import predict_score
from grades.results import get_grade


score_history = [80, 90, 70, 100]
predicted_score = predict_score(score_history)

predicted_grade = get_grade(predicted_score)
print(f"The student's predicted grade is: {predicted_grade}")
