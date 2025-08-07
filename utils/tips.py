def tips():
    tips_list = [
        "1. Always use strong and unique passwords for each of your accounts.\n",
        "2. Enable two-factor authentication (2FA) wherever possible.\n",
        "3. Be cautious of unsolicited emails or messages asking for personal information.\n",
        "4. Regularly update your software and applications to protect against vulnerabilities.\n",
        "5. Avoid clicking on suspicious links or downloading attachments from unknown sources.\n",
        "6. Use a reputable antivirus program and keep it updated.\n",
        "7. Regularly back up your important data to a secure location.\n",
        "8. Be aware of phishing scams and learn how to recognize them.\n",
        "9. Use a password manager to securely store and manage your passwords.\n",
        "10. Educate yourself about the latest cyber threats and how to protect against them.\n",
        "11. Monitor your financial accounts regularly for unauthorized transactions.\n",
        "12. Be cautious when using public Wi-Fi networks; use a VPN if necessary.\n",
        "13. Review your privacy settings on social media platforms to control who can see your information.\n",
        "14. Log out of accounts when using shared or public computers.\n",
        "15. Report any suspicious activity or potential security breaches to the relevant authorities.\n"
    ]

    print ("\nTips for Cyber Security Awareness:")
    print("====================================")

    for tip in tips_list:
        print(tip)
        user_input = input("Press any key to see the next tip or type 'exit' to quit: ").strip().lower()
        if user_input == 'exit':
            print("Exiting tips...")
            break

    print("\nAll done! Stay safe online!!!")
