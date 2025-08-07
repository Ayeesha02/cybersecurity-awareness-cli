from utils.logger import log_event


def password_checker(password):
    """
    Check if the password meets the required criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (e.g., !@#$%^&*()-_=+[]{}|;:'",.<>?/)
    
    Args:
        password (str): The password to check.
  returns: 
        Feedback on password strength.
    """
    feedback_score = 0
    feedback = []
    if len(password)<8:
        feedback.append("Password must be at least 8 characters long.")
    else: 
        feedback_score += 1
    if any(char.isupper() for char in password) and  any(char.islower() for char in password):
        feedback_score += 2
    else:
        feedback.append("Password must contain both uppercase and lowercase letters.")
        feedback_score += 1
        
    if any(char.isdigit() for char in password):
        feedback_score += 1
    else:
        feedback.append("Password must contain at least one digit.")
    if any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        feedback_score += 1
    else:
        feedback.append("Password must contain at least one special character.")



    if feedback_score == 5:
        strength = "strong."
    elif feedback_score >= 3:
        strength = "moderate."
    else:
        strength = "weak."

    log_event("password_check", {
    "password": "*" * len(password),
    "feedback_score": feedback_score,
    "strength": strength,
    "feedback": feedback
})

    return print("Feedback Score: ", feedback_score," out of 5", "\nPassword Strength: ",strength, "\nFeedback: ", feedback)

