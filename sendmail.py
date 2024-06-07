
import os, sys

# email sending 
import smtplib
import ssl
from email.message import EmailMessage


import random
import time
# Loading function
def Loading(value=True):
    loading = ['|||||', '/////', '\\\\\\']
    # loading = ['🌟🌟🌟🌟🌟', '💫💫💫💫💫', '✨✨✨✨✨', '🌈🌈🌈🌈🌈', '🌸🌸🌸🌸🌸', '🌼🌼🌼🌼🌼', '🌞🌞🌞🌞🌞', '🌛🌛🌛🌛🌛', '🌟💫✨💫🌟']
    
    while value:
        random.shuffle(loading)  # Shuffle the loading icons randomly
        for i in loading:
            # print(f'Please wait...{i}', end="\r")
            print(f'\rPlease wait...{i}', end="")
            time.sleep(0.1)
        value = False

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

def get_email_subject_body():
    def get_valid_email():
         # To email valid
        while True:
            to_email = input("Enter recipient email: ").replace(' ', '')

            if not to_email:
                print('\nEmail recipient required!')
                continue

            if not any(to_email.endswith(domain) for domain in EMAIL_PROVIDERS):
                print("\nInvalid recipient email. Supported email providers include 'gmail.com', 'yahoo.com', and 'outlook.com'.\nPlease try again.\n")
                continue

            return to_email
        
    def get_valid_subject():
        while True:
            subject = input("Enter email subject: ")

            if not subject:
                print("Subject required!")
                continue
            return subject
        
    def get_valid_message():
         while True:
            body = input("Enter email message: ")

            if not body:
                print("Message required!")
                continue
            return body


    to_email = get_valid_email()
    subject = get_valid_subject()
    body = get_valid_message()


    return to_email, subject, body




def email_sender(to_email, subject, body):
    # message setting area
    message=EmailMessage()
    message['From'] = EMAIL
    message['To'] = to_email
    message['Subject'] = subject
    # message.set_content(body)

    html = f"""
            <h3>{body}</h3>
    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, message.as_string())

    Loading()
    print("\nYour email was sent successfully.")

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
        # print('main code')
        to_email, subject, body = get_email_subject_body()
        email_sender(to_email, subject, body)
    


if __name__ == "__main__":
    main()