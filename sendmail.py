
import os, sys

EMAIL_PROVIDERS = ['@gmail.com', '@yahoo.com', '@outlook.com']  # Add other familiar email hosts here

# For development purpose
DEVELOPMENT = False
if os.path.exists('dev_config.py'):
    from dev_config import EMAIL, PASSWORD
    DEVELOPMENT = True
else:
    from config import EMAIL, PASSWORD



def help():
    commands = f"\n-help, -h : Help command\n-reset, -r : Resetting your current email and password"
    
    print(commands)

def config():
    while True:
        print('Please configure your Email and password:-')
        email = input("Enter you Email: ")
        psd = input("Enter you Password: ")

        if email == '' or psd == '':
            print('\nEmail and Password required')
            continue

        elif not any(email.endswith(domain) for domain in EMAIL_PROVIDERS):
            print("\nInvalid email, only supports email providers like 'abc@gmail.com', 'abc@yahoo.com', 'abc@outlook.com'.\nPlease try again.\n")
            continue

        else:
            config_file = 'dev_config.py' if DEVELOPMENT else 'config.py'
            config_path = os.path.join(os.path.dirname(__file__), config_file)
            
            with open(config_path, 'w') as file:
                file.write(f"EMAIL = '{email}'\nPASSWORD = '{psd}'")
            break



def main():
    if EMAIL == '' or PASSWORD == '':
        config()


    # Handling command-line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1]

        # re-setting the email and password
        if command in ('-r', '-reset'):
            config()

        elif command in ('-h', '-help'):
            help()
            sys.exit(0)

        else:
            print("Unknown command. Use -h or -help for the list of available commands.")
            sys.exit(1)


    # print(len(sys.argv))
    
    else:
        print('main code')
    


if __name__ == "__main__":
    main()