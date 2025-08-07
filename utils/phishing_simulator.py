import json
from datetime import datetime

from utils.logger import log_event

def phishing_simulator():
    """
    Simulates a phishing attack by generating a fake email and sending it to a target.
    This function is for educational purposes only and should not be used for malicious intent.
    """
    
    emails = [
    {
        "subject": "URGENT: Your account has been suspended",
        "body": "Dear user,\n\nYour bank account has been temporarily suspended due to suspicious activity. Please verify your identity immediately by clicking the link below:\n\nhttp://verify-bank-security.com/login\n\nFailure to act will result in permanent closure.\n\nThank you,\nBank Security Team",
        "is_phishing": True
    },
    {
        "subject": "Action Required: Email storage almost full",
        "body": "Your mailbox is almost full. Upgrade now to prevent email disruptions:\n\nhttp://email-quota-reset.com/upgrade\n\nThank you,\nEmail Admin",
        "is_phishing": True
    },
    {
        "subject": "Team Meeting Agenda - Aug 10",
        "body": "Hi team,\n\nAttached is the agenda for our meeting scheduled on August 10th. Please review it before our call.\n\nBest,\nSarah",
        "is_phishing": False
    },
    {
        "subject": "Win a FREE iPhone 15 Pro!",
        "body": "Congratulations!\n\nYou've been selected to receive a brand-new iPhone 15 Pro. Click the link below to claim your reward:\n\nhttp://free-gifts-now.com/iphone\n\nOffer expires in 24 hours. Don’t miss out!",
        "is_phishing": True
    },
    {
        "subject": "Your Amazon Order #47583927 has shipped",
        "body": "Hello Ayeesha,\n\nYour order for 'Python Programming for Beginners' has shipped. You can track your order using the link below:\n\nhttps://www.amazon.ae/orders\n\nThanks for shopping with us!",
        "is_phishing": False
    }
]
    score = 0 
    print("\nWelcome to the Phishing Simulator!")
    print("\nYou will be presented with a series of emails. Identify which ones are phishing attempts.")

    for email in emails: 
        print("\nSubject:", email["subject"])
        print("Body:", email["body"])

        user_input=input("\nIs this a phishing email? (yes/no): ").strip().lower()

        while user_input not in ["yes", "no"]:
            user_input = input("\nInvalid input. Please enter 'yes' or 'no': ").strip().lower()

        event_type = "phishing_simulation"
        if user_input=="yes" and email["is_phishing"]:
                score += 1
                log_event(event_type, {
                    "email": email["subject"],
                    "result": "Correctly identified phishing email"
                })
        elif user_input=="no" and not email["is_phishing"]:
                score += 1
                log_event(event_type, {
                    "email": email["subject"],
                    "result": "Correctly identified legitimate email"
                })
        else:
                log_event(event_type, {
                    "email": email['subject'],
                    "result": "Failed to identify email"
                })

    print("\nSimulation complete!")
    print("\nYour score:", score, "out of", len(emails))
    log_event(event_type, {
                    "Final result": f"Your score: {score} out of {len(emails)}"
                })