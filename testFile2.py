import os
import json

# SAFE: Fix for insecure deserialization
def load_user_data(data):
    return json.loads(data)

# VULNERABLE: Command injection via unsanitized input
def run_command(user_input):
    # This is unsafe: user can inject arbitrary shell commands
    os.system("echo Hello && " + user_input)

# USAGE
if __name__ == "__main__":
    user_data_input = input("Paste your serialized data (JSON): ")
    user_data = load_user_data(user_data_input)
    
    command_input = input("Enter command to run: ")
    run_command(command_input)
