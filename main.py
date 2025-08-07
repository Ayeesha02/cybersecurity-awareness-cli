from utils.phishing_simulator import phishing_simulator
from utils.password_checker import password_checker
from utils.tips import tips


def main():
    
    while True:
        print("\nWelcome to Simple Cyber Security awareness tool!\n")
        print("1. Check Password Strength:")
        print("2. Simulate Phishing Attack:")
        print("3. Tips for Cyber Security Awareness:")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            user_password = input("Enter a password to check its strength: ")
            password_checker(user_password)
        elif choice == "2":
            phishing_simulator()
        elif choice == "3":
            tips()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()