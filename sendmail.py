
import os, sys

EMAIL_PROVIDERS = ['@gmail.com', '@yahoo.com', '@outlook.com']  # Add other familiar email hosts here

# For development purpose
DEVELOPMENT = False # means production
config_file = 'config.py' # means production
config_path = ''
if os.path.exists('dev_config.py'): # development condition
    from dev_config import EMAIL, PASSWORD
    DEVELOPMENT = True
    config_file = 'dev_config.py'
    config_path = os.path.join(os.path.dirname(__file__), config_file)
else: # production condition
    from config import EMAIL, PASSWORD
    # config_file = 'config.py'
    config_path = os.path.join(os.path.dirname(__file__), config_file)



def help():
    commands = f"\n-help, -h : Help command\n-reset, -r : Resetting your current email and password"
    
    print(commands)

def config():
    while True:
        if EMAIL == '' or PASSWORD == '':
            print('Please configure your Email and Password:-')
        else:
            print('Please reset your Email and Password:-')
            
        email = input("Enter you Email: ").replace(' ', '') # Remove all spaces from the input string.
        psd = input("Enter you Password: ")

        if email == '' or psd == '':
            print('\nEmail and Password required')
            continue

        elif not any(email.endswith(domain) for domain in EMAIL_PROVIDERS):
            print("\nInvalid email, only supports email providers like 'abc@gmail.com', 'abc@yahoo.com', 'abc@outlook.com'.\nPlease try again.\n")
            continue

        else:
            # config_file = 'dev_config.py' if DEVELOPMENT else 'config.py'
            config_path = os.path.join(os.path.dirname(__file__), config_file)
            
            with open(config_path, 'w') as file:
                file.write(f"EMAIL = '{email}'\nPASSWORD = '{psd}'")

            if EMAIL == '' or PASSWORD == '':
                print('Your Email and Password have been successfully added.')
                exit(0)
                # break
            else:
                print('You have successfully updated your Email and Password.')
                exit(0)
                # break
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